from flask import jsonify, request, session, redirect
from app import db
import pymongo


class Filter():
    def filter_tweets(self):
        conditions = {
            "filterby":request.form.getlist('checkbox'),
            "forlikes":request.form.get('likeElements'),
            "forreplies":request.form.get('replyElements'),
            "forretweets":request.form.get('retweetElements'),
            "likenumber":request.form.get('forlike'),
            "replynumber":request.form.get('forreply'),
            "retweetnumber":request.form.get('forretweets'),
        }
        tweets = db.tweets
        output = []

        print(conditions['filterby'])
        self.like=False
        self.reply=False
        self.retweet=False
        for i in conditions['filterby']:
            if i == 'likes':
                self.like=True
            if i == 'replies':
                self.reply = True
            if i == 'retweets':
                self.retweet=True
        if request.method == 'POST':
            if self.like==True and self.reply==False and self.retweet==False:
                results = tweets.find({"likes":{conditions['forlikes']:int(conditions['likenumber'])}}).sort('likes',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.reply==True and self.like==False and self.retweet==False:
                results = tweets.find({"replies":{conditions['forreplies']:int(conditions['replynumber'])}}).sort('replies',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.retweet==True and self.reply==False and self.retweet==False:
                results = tweets.find({"retweet":{conditions['forretweets']:int(conditions['retweetnumber'])}}).sort('retweet',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.retweet==True and self.like == True and self.reply==False:
                results = tweets.find({"retweet":{conditions['forretweets']:int(conditions['retweetnumber'])},"likes":{conditions['forlikes']:int(conditions['likenumber'])}}).sort('likes',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.retweet==True and self.reply == True and self.like==False:
                results = tweets.find({"retweet":{conditions['forretweets']:int(conditions['retweetnumber'])},"replies":{conditions['forreplies']:int(conditions['replynumber'])}}).sort('replies',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.like==True and self.reply == True and self.retweet==False:
                results = tweets.find({"likes":{conditions['forlikes']:int(conditions['likenumber'])},"replies":{conditions['forreplies']:int(conditions['replynumber'])}}).sort('likes',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if self.like==True and self.reply == True and self.retweet == True:
                results = tweets.find({"likes":{conditions['forlikes']:int(conditions['likenumber'])},"replies":{conditions['forreplies']:int(conditions['replynumber'])},"retweet":{conditions['forretweets']:int(conditions['retweetnumber'])}}).sort('likes',pymongo.DESCENDING) #pymongo.cursor
                for value in results:
                    output.append(value)
                # session['results'] = output
            if db.filtered.find_one({"content":{"$exists":1}}):
                db.filtered.delete_many({"content":{"$exists":1}})
            if db.filtered.insert_many(output):
                return jsonify(conditions),200
        

