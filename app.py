from modules.data_loader import load_data
from modules.text_cleaner import clean_text
from modules.sentiment_analyzer import get_sentiment
from modules.visualizer import plot_sentiment_chart, plot_sentiment_trend
import pandas as pd

def main():
    print("🚀 Healthcare Sentiment Analysis Tool")

    df = load_data()

    # ⏱️ Use only first 10 rows for now to test speed
    df = df.head(10)

    df.dropna(inplace=True)
    df['cleaned_text'] = df['text'].apply(clean_text)
    df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

    print(df[['timestamp', 'text', 'sentiment']].head())

    df.to_csv("output_results.csv", index=False)

    plot_sentiment_chart(df)
    plot_sentiment_trend(df)


if __name__ == "__main__":
    main()
