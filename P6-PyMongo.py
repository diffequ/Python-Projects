######################################################################################
# Burak Koryan | http://koryan.ca | burak@koryan.ca | April 22 2018
# Description : Simple mongodB connection in python and inserting one document into dB
######################################################################################

#- importing libraries -#
import pymongo
import datetime
import pprint
from pymongo import MongoClient

client = MongoClient ('localhost',27017)                     # connect to localhost

db = client['test-database']                                 # name the db

collection = db.test_collection                              # define the mongodb collection

post = {"Place": "Canada","date":datetime.datetime.utcnow()} # create the document
posts = db.posts
post_id = posts.insert_one(post).inserted_id                 # Insert Post into db
pprint.pprint(posts.find_one())                              # print db on console
