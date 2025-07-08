import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.text_cleaner import clean_text
from modules.sentiment_analyzer import get_sentiment
from modules.visualizer import plot_sentiment_chart, plot_sentiment_trend

st.set_page_config(page_title="🧠 Mental Health Sentiment Dashboard", layout="wide")

st.title("🧠 Social Media Sentiment Dashboard - Mental Health")
st.markdown("Analyzing sentiment trends from real-world mental health discussions.")

# Load and preprocess data
df = load_data()
df = df.head(500)  # Limit for faster Streamlit testing
df.dropna(inplace=True)
df['cleaned_text'] = df['text'].apply(clean_text)
df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

# Show sample data
st.subheader("📄 Sample Processed Data")
st.dataframe(df[['timestamp', 'text', 'sentiment']].head())

# Save output
df.to_csv("output_results.csv", index=False)

# Plot sentiment chart
st.subheader("📊 Sentiment Distribution")
plot_sentiment_chart(df)

# Plot trend
st.subheader("📈 Sentiment Trend Over Time")
plot_sentiment_trend(df)
