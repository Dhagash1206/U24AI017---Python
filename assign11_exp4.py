"""Whenever your friends John and Judy visit you together, yall have a party. Given a
DataFrame with 10 rows representing the next 10 days of your schedule and whether John
and Judy are scheduled to make an appearance, insert a new column
called days_til_party that indicates how many days until the next party.
days_til_party should be 0 on days when a party occurs, 1 on days when a party doesnt
occur but will occur the next day, etc."""


import pandas as pd

data = {
    'day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
    'party': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

df['days_til_party'] = None

for i in range(len(df)-1, -1, -1):
    if df.loc[i, 'party'] == 1:
        df.loc[i, 'days_til_party'] = 0
    elif i < len(df) - 1:
        df.loc[i, 'days_til_party'] = df.loc[i + 1, 'days_til_party'] + 1

print(df)
