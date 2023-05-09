from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    sentiment = SentimentIntensityAnalyzer()
    sent = sentiment.polarity_scores(text)
    return sent
