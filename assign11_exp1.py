"""Write a Pandas program to create
a) Date time object for Jan 15 2012.
b) Specific date and time of 9:20 pm.
c) Local date and time.
d) A date without time.
e) Current date.
t) Time from a date time.
g) Current local time."""

import pandas as pd
from datetime import datetime, time

date_a = pd.Timestamp('2012-01-15')
print("a) Date time object for Jan 15, 2012:", date_a)

date_b = pd.Timestamp('2023-01-01 21:20')
print("b) Specific date and time of 9:20 pm:", date_b)

date_c = pd.Timestamp.now()
print("c) Local date and time:", date_c)

date_d = pd.to_datetime('2023-04-24').date()
print("d) A date without time:", date_d)

date_e = pd.Timestamp.today().date()
print("e) Current date:", date_e)

datetime_f = pd.Timestamp('2023-04-24 15:45:30')
time_f = datetime_f.time()
print("f) Time from a date time:", time_f)

current_time_g = datetime.now().time()
print("g) Current local time:", current_time_g)
