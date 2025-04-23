"""Write a Pandas program to convert all the string values to upper, lower cases in a given
pandas series. Also find the length of the string values.
s = pd.Series"""

import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()
lower_case = s.str.lower()
string_length = s.str.len()

print("Original Series:\n", s)
print("\nUppercase:\n", upper_case)
print("\nLowercase:\n", lower_case)
print("\nLength of strings:\n", string_length)
