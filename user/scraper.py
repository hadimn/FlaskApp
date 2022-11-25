from flask import Flask, jsonify, request, session, redirect
import snscrape.modules.twitter as twitterScraper
from app import db
import json
import re
import os
from langdetect import detect


corona = twitterScraper.TwitterHashtagScraper("corona")
lebanon = twitterScraper.TwitterHashtagScraper("lebanon")

corona_tweets = []
lebanon_tweets = []

class Scrape:
    def __init__(self):
        self.store_tweets=[]

    # def lang_detector(self,docs):
    #     lang_list = []
    #     for doc in docs:
    #         lang_list.append(detect(doc))
    #     return lang_list

    def scrapeTitle(self,title,n):
        tweets = twitterScraper.TwitterHashtagScraper(title)
        for i,tweet in enumerate(tweets.get_items()):
            if(i > int(n)) and detect(tweet.content)=="en":
                break
            self.store_tweets.append({"_id":tweet.id,"content":tweet.content,"likes":tweet.likeCount,"replies":tweet.replyCount,"retweet":tweet.retweetCount})
        
        # self.toJson()
        return self.store_tweets
        
    def toJson(self):
        filePath = '/user/json/tweets.json'
        if os.path.exists(filePath):
            os.remove(filePath)
            f=open(f"{filePath}","w")
            j = json.dumps(self.store_tweets)
            f.write(j)
            f.close()
        else:
            f=open(f"{filePath}","w")
            j = json.dumps(self.store_tweets)
            f.write(j)
            f.close()

    def get_tweets(self):
        num = {
            "number":request.form.get('number'),
            "title":request.form.get('title')
        }

        session['num']=num
        # session['tweets']=self.scrapeTitle(session['num']['title'],session['num']['number'])

        if re.findall(r'[#]\w+', session['num']['title']):
            if db.tweets.find_one({"content":{"$exists":1}}):
                db.tweets.delete_many({"content":{"$exists":1}})
                # return jsonify({"error":"tweets already scraped"}),400
            if db.tweets.insert_many(self.scrapeTitle(session['num']['title'],session['num']['number'])):
                return jsonify(num),200
        else:
            return jsonify({"error":"Title must start with #"}),400

