from http import client
from user import app
import pymongo
import urllib
# from flask import ServerApi

#DataBase
# client = pymongo.MongoClient('localhost',27017)
# db = client.user_login_system
# db2 = client.


client = pymongo.MongoClient("mongodb+srv://hadimn123:"+ urllib.parse.quote_plus("@Q1w2e3r4t5y6")+"@cluster0.8kblayh.mongodb.net/?retryWrites=true&w=majority")
db = client.user_login_system


if __name__ == '__main__':
    app.run(debug=True)