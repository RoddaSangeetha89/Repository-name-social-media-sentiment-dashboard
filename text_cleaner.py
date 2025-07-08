import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)  # remove URLs
    text = re.sub(r'\@\w+|\#', '', text)                 # remove @ and #
    text = re.sub(r'[^\w\s]', '', text)                  # remove punctuation
    return text
