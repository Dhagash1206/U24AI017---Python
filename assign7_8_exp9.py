"""Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]"""

import re

def tokenize(text):
    patterns = [
        r'\d{1,2}/\d{1,2}/\d{2,4}',
        r'https?://\S+|www\.\S+',
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        r'@\w+',
        r'\d{1,3}(,\d{3})*(\.\d+)?',
        r'[^\w\s]',
        r'[\u0900-\u097F]+'
    ]
    regex = '|'.join(patterns)
    return re.findall(regex, text)

text = "Sample text with date 12/12/2023, URL https://example.com, email test@example.com, number 3,22,243.15, and @username."
tokens = tokenize(text)
print(tokens)


