# TwitterMiner
A simple GUI tool for mining information from twitter

![Sample output](/output.png?raw=true "Sample output")

## Creating a Twitter Account

The first thing you must do is to create an account in Twitter. If you do have a Twitter account, you can skip this step.
Even if you do have a twitter account but want to create a new one for the purpose of evaluating this tool then in that case also
please create a new twitter account. You can create a twitter account by visiting [here](https://twitter.com/signup)

## Creating a Twitter App

Once you have created a twitter account, next, you need to create a Twitter App. To do this visit [Twitter Apps](https://apps.twitter.com/)
and follow the instructions for Creating New App. You will be able to get the following four pieces of information:
* consumer_key
* consumer_secret
* access_key
* access_secret

Copy these information to the relevant fields in the config.json file.

## Installation

This tool is written in Python and requires Python 2.7 or 3. Moreover, it requires the following Python packages that you can install via pip.
To install via pip do: 
```
pip install package_name
```

* [appJar](http://appjar.info/)
* [python-twitter](https://github.com/bear/python-twitter)
* [scikit-learn](http://scikit-learn.org/stable/)
* [pytagcloud](https://pypi.python.org/pypi/pytagcloud)

## Running

To run this tool simply specify the json file that you created above at the command line as follows:
```
python miner.py config.json
```

This will open a GUI that you can enter a query. When you hit the SEARCH button, the tool will search in twitter, find the top search
results (as ranked by twitter) for the given query. It will show these tweets in the screen. Moreover, the tool will count the frequency of the words that
appear in those top tweets (we exclude some noncontent stop words) and display a tag cloud. The size of a word in the tag cloud corresponds to the frequency of that word in the top-ranked tweets.

Sometimes the tag cloud might be too large to properly display within the GUI. In that case you can open "sample.png" file created by the tool in the same directory as miner.py using any image viewer.


