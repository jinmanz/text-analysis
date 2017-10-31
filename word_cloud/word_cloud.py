 # -*- coding: utf-8 -*- 
import os
import re
import tweepy
import csv
import collections
from os import path
from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize

import matplotlib.pyplot as plt
from wordcloud import WordCloud
####input your credentials here
def clean_punctuation(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'

    for marker in punctuation:
        text = text.replace(marker, "")
    return text
def clean_http(text):
    return re.sub(r"http\S+", "", text)

def clean_text(text):
    return re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",text)


infile = open('ua.txt')
text = infile.read().lower()
infile.close()
text = clean_punctuation(text)
#remove hash tag, user name, http
text = clean_http(text)
text = clean_text(text)


match_pattern = nltk.word_tokenize(text)

# remove stop words
filtered_words = [word for word in match_pattern if word not in stopwords.words('english')]
word_freq = collections.Counter(filtered_words)

#record the term frequency in tf.csv
csvFile = open('tf.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
for word, freq in word_freq.most_common():
    csvWriter.writerow([word, freq])
    


wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(filtered_words))

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
