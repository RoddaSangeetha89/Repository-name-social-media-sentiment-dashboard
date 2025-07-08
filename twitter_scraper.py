import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(query="#mentalhealth", limit=100):
    print(f"🔍 Scraping tweets for query: {query} (limit {limit})")
    tweets = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append([tweet.date, tweet.content])
    
    df = pd.DataFrame(tweets, columns=["timestamp", "text"])
    return df
