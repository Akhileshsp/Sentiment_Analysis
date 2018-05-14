from textblob import TextBlob
text = "Python is a great tool"
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print(sentiment)
