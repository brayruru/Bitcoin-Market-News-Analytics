import pandas as pd
import numpy as np
import nltk
import logging
import os
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

# Crear la carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Limpieza de datos
def clean_price_data(df):
    try:
        df = df.copy()
        df = df.drop_duplicates()
        df = df[df["price_usd"] > 0]
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=["timestamp"])
        return df
    except Exception as e:
        logging.error(f"Error in clean_price_data: {e}")
        raise

def clean_news_data(df: pd.DataFrame) -> pd.DataFrame:
    
    try:
        df = df.copy()
        df = df.drop_duplicates()
        df["dateTimePub"] = pd.to_datetime(df["dateTimePub"], errors="coerce")
        df = df.dropna(subset=["dateTimePub"])
        df["title"] = df["title"].fillna("").str.strip()
        df["body"] = df["body"].fillna("").str.strip()
        cleaned = df[["dateTimePub", "title", "body", "sentiment", "source", "url"]].copy()
        return cleaned
    except Exception as e:
        logging.error(f"Error in clean_news_data: {e}")
        raise
# Features
def add_indicators(df):
    try:
        df = df.copy()
        df = df.sort_values('timestamp')
        df['sma_5'] = df['price_usd'].rolling(window=5).mean()
        df['ema_5'] = df['price_usd'].ewm(span=5).mean()
        return df
    except Exception as e:
        logging.error(f"Error in add_indicators: {e}")
        raise
    

def extract_keywords(df, top_n=10):
    try:
        df = df.copy()
        stop_words = set(stopwords.words('english'))
        vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
        X = vectorizer.fit_transform(df['title'].fillna(''))
        keywords = vectorizer.get_feature_names_out()
        df['keywords'] = [', '.join([kw for kw in keywords if kw in title.lower()]) for title in df['title']]
        return df
    except Exception as e:
        logging.error(f"Error in extract_keywords: {e}")
        raise

def compute_aggregated_metrics(news_df):
    try:
        df = news_df.copy()
        df['date'] = df['dateTimePub'].dt.date

        agg_metrics = df.groupby('date').agg({
            'sentiment': 'mean',
            'title': 'count'
        }).rename(columns={
            'sentiment': 'avg_sentiment',
            'title': 'news_count'
        }).reset_index()

        logging.info("Aggregated metrics successfully calculated.")
        return agg_metrics

    except Exception as e:
        logging.error(f"Error calculating aggregated metrics:: {e}")
        raise    