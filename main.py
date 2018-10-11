from nltk.corpus import twitter_samples
print (twitter_samples.fileids())
pos_tweets = twitter_samples.strings('positive_tweets.json')
print (len(pos_tweets)) # Output: 5000
 
neg_tweets = twitter_samples.strings('negative_tweets.json')
print (len(neg_tweets)) # Output: 5000
 
#all_tweets = twitter_samples.strings('tweets.20150430-223406.json')
#print (len(all_tweets)) # Output: 20000
 
# positive tweets words list
pos_tweets_set = []
for tweet in pos_tweets:
    pos_tweets_set.append((tweet, 'pos'))
 
# negative tweets words list
neg_tweets_set = []
for tweet in neg_tweets:
    neg_tweets_set.append((tweet, 'neg'))
 
print (len(pos_tweets_set), len(neg_tweets_set)) # Output: (5000, 5000)
 
# radomize pos_reviews_set and neg_reviews_set
# doing so will output different accuracy result everytime we run the program
from random import shuffle 
shuffle(pos_tweets_set)
shuffle(neg_tweets_set)
