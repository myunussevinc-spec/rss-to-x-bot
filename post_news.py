import feedparser
import tweepy
import os
# X API bilgileri (GitHub Secrets üzerinden gelecek)
X_API_KEY = os.environ["X_API_KEY"]
X_API_SECRET = os.environ["X_API_SECRET"]
X_ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
X_ACCESS_TOKEN_SECRET = os.environ["X_ACCESS_TOKEN_SECRET"]

# RSS kaynakları
RSS_FEEDS = [
    "https://www.euronews.com/rss",
       ]
