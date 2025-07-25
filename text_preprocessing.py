import re

def clean_text(text):
    text = re.sub(r"http\\S+|@\\S+|#\\S+", "", text)
    text = re.sub(r"[^a-zA-Z\\s]", "", text)
    return text.lower().strip()
