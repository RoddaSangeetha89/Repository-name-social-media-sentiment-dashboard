import matplotlib.pyplot as plt
import streamlit as st

def plot_sentiment_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    df['sentiment'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Sentiment Distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    st.pyplot(fig)

def plot_sentiment_trend(df):
    trend = df.groupby(['timestamp'])['sentiment'].value_counts().unstack().fillna(0)
    fig, ax = plt.subplots(figsize=(8, 5))
    trend.plot(kind='line', ax=ax)
    ax.set_title("Sentiment Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    st.pyplot(fig)
