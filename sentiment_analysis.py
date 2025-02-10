import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Twitter API credentials (We will set these up later)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def fetch_tweets(keyword, count=10):
    tweets = api.search_tweets(q=keyword, count=count, lang="en", tweet_mode="extended")
    for tweet in tweets:
        sentiment = analyzer.polarity_scores(tweet.full_text)
        sentiment_label = "Positive" if sentiment['compound'] > 0.05 else "Negative" if sentiment['compound'] < -0.05 else "Neutral"
        print(f"Tweet: {tweet.full_text}\nSentiment: {sentiment_label}\n")

fetch_tweets("Bitcoin", 5)
