from copy import copy
from user import app #form app file import app var which is the flask object
from flask import render_template,redirect,session,jsonify,request
from user.models import User #from models file that inside user folder import User class
from functools import wraps
from user.scraper import Scrape
from app import db
from user.filter import Filter


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() #we will return signUp method which is inside User class 


#decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

@app.route('/')
def myPage():
    return render_template('myPage.html')

@app.route('/homepage')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login',methods=['POST'])
def login():
    return User().login()


#scraping routes
#------------------
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap
#----------------

@app.route('/scrapepage')
@admin_required
def scraping():
    return render_template('scrapeTweets.html')

@app.route('/tweets')
def tweets():
    tweets1 = db.tweets.aggregate([
        {"$sort":{"likes":-1}},
        {"$limit":200},
        {"$match":{"likes":{"$gt":100}}}
        ])
    tweets = []
    for tweet in tweets1:
        tweets.append(tweet)
    tweets2 = copy(tweets)
    count = len(list(tweets2))
    count2 = db.tweets.count_documents({})
    return render_template('tweets.html',tweets=tweets , count=count2 , count2 = count)

@app.route('/user/scrape',methods=['POST'])
def scrape():
    return Scrape().get_tweets()


# Filter routes
@app.route('/tweets/filter')
def filter():
    filtered = db.filtered.find()
    return render_template('filtering.html',filtered=filtered)

@app.route('/myTweets',methods=['POST','GET'])
def filter_tweet():
    return Filter().filter_tweets()

#charts routes
# db.collection.aggregate{ "$project": {<field>: { $regexFindAll:{"input":"$Field-name", "regex": '/pattern/'} } } }
@app.route('/chart')
def trending():
    data = db.tweets.aggregate([
            {
        "$project": {
        
        "content": {
            "$regexFindAll": {
            "input": "$content",
            "regex": "[#]\\w+"
            },
        }
        }
    },
    {
        "$unwind": "$content"
    },
    {
        "$group": {
        "_id": "$content.match",
        "count": {
            "$sum": 1
        }
        }
    }
        
    ])
    result=[]
    for tweet in data:
        result.append(tweet)
    # print(result) #this just to get sure it return hashtags only.
    return render_template('graphs.html',result=result)