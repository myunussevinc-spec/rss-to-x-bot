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
    "https://www.ntv.com.tr/son-dakika.rss",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://tr.defensehere.com/rss/son-dakika",
    "https://tr.defensehere.com/rss/yapay-zeka",
    "https://tr.defensehere.com/rss/tsk",
    "https://tr.defensehere.com/rss/teknoloji",
    "https://tr.defensehere.com/rss/savunma-sanayii",
    "https://tr.defensehere.com/rss/nukleer",
    "https://tr.defensehere.com/rss/ukrayna",
    "https://tr.defensehere.com/rss/tatbikatlar",
    "https://www.tasnimnews.com/tr/rss/feed/1440/0/7/0/MostPupolar",
    "https://www.tasnimnews.com/tr/rss/feeds/1320/0/0/0",
    "https://news.un.org/feed/subscribe/en/news/region/africa/feed/rss.xml",
    "https://www.haberturk.com/rss/kategori/teknoloji.xml",
    "https://www.yeniakit.com.tr/rss/video/dunya",
    "https://www.aa.com.tr/tr/teyithatti/rss/news?cat=gazze",
    "https://www.aa.com.tr/tr/teyithatti/rss/news?cat=ekonomi",
    "https://www.mfa.gov.tr/tr.rss.mfa?259fca5b-ebee-47d1-b850-ec53936ab32e",
    "https://www.voaturkce.com/api/ztbvrl-vomx-tpekvkq",
    "https://globalnews.ca/feed/",
    "https://siyahordu.net/rss/israil",
    "https://globalnews.ca/world/feed/",
    "https://www.saba.ye/en/rsscatfeed18.htm",
    "https://www.saba.ye/en/rsscatfeed60.htm",
    "https://www.crisisgroup.org/rss/2",
    "https://www.crisisgroup.org/rss/4708",
]
