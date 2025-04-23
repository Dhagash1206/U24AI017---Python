import re


pattern = r"\d+"

text = input()
matches = re.findall(pattern, text)
print(matches)
