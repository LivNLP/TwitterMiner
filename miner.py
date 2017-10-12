#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @Date    : 2017-09-09 00:03:48
# @Author  : Danushka Bollegala (danushka@liverpool.ac.uk)
# @Link    : http://www.csc.liverpool.ac.uk/~danushka
# @Version : $Id$

from appJar import gui

app = gui("Twitter Miner", "1200x1000")
app.addLabelEntry("Query")
app.setLabelFont(16, "Arial")

import twitter
import json
from sklearn.feature_extraction.text import CountVectorizer
from pytagcloud import create_tag_image, make_tags, LAYOUT_MIX, LAYOUT_HORIZONTAL
from pytagcloud.lang.counter import get_tag_counts




class Miner:

    def __init__(self):
        with open("config.json") as config_file:
            self.config = json.load(config_file)
        self.api = twitter.Api(consumer_key=self.config["consumer_key"], consumer_secret=self.config["consumer_secret"],
                      access_token_key=self.config["access_key"], access_token_secret=self.config["access_secret"],
                      input_encoding="utf-8")
        pass


    def get_results(self, query):
        res = self.api.GetSearch(term=query, lang="en", return_json=True)
        return [txt['text'].encode('utf-8')   for txt in res['statuses']]
        
    def get_freq(self, texts):
        """
        Tokenise the texts, remove stop words and get a frequency count
        """
        vectorizer = CountVectorizer(stop_words="english")
        h = vectorizer.fit_transform([" ".join(texts)])
        vocab = vectorizer.vocabulary_
        freq = {}
        for word in vocab:
            freq[word] = h[0,vocab[word]]
        return freq


    def get_cloud(self, freq, fname):
        """
        Create a tag cloud.
        """
        txt_str = ""
        stop_words = ["https", "http"]
        for word in freq:
            if freq[word] > 0 and len(word) < 8 and word not in stop_words:
                txt_str += (" %s " % word) * freq[word]
        tags = make_tags(get_tag_counts(txt_str), minsize=1, maxsize=120)
        #print tags
        create_tag_image(tags, fname, size=(1200, 800), fontname='Inconsolata', layout=LAYOUT_MIX)
    pass


def save_cloud(query):
    TM = Miner()
    res = TM.get_results(query)
    
    lbl_txt = ""
    for (i,s) in enumerate(res):
        tweet = "%i: %s\n" % (i+1, s)
        print tweet
        lbl_txt += tweet
    app.setLabel("Results", lbl_txt)
    freq = TM.get_freq(res)
    TM.get_cloud(freq, "sample.png")
    pass


def press(button):
    if button == "Exit":
        app.stop()
    else:
        query = app.getEntry("Query")
        print query
        save_cloud(query)
        app.setImage("img", "sample.png")
    pass

app.addButtons(["Search", "Exit"], press)

app.startLabelFrame("Search Results")
app.addLabel("Results", "")
app.stopLabelFrame()

#app.startLabelFrame("Tag Cloud")
app.addImage("img", "blank.png")
#app.stopLabelFrame()
app.go()


