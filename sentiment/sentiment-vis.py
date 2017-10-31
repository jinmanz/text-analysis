 # -*- coding: utf-8 -*- 
import re
import tweepy
import csv
from textblob import TextBlob
####input your credentials here

consumer_key = 'WRzrHerkO3PQFE9PsbOSVJxUO'
consumer_secret = 'l2F8owgWRm33SeK7ts5Vs6yBU3Qd2FbXzVoM2x9k0BFsXbqLfr'
access_token = '527454179-JZ7zT9M4jgffQYqn3SG7W1z3UdphCT5irgXI96Qa'
access_token_secret = 'Ljtj25dztSwJ4OGs2IfB2vkGhdghmvZl4cLMSkCssKxnJ'
 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data

csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03",
                           until ="2017-05-03"
                           ).items():
    #print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
 


fo = open("ua.txt", "wb")
for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    #store tweets in a txt file
    fo.write(tweet.text.encode('utf-8'));
   
