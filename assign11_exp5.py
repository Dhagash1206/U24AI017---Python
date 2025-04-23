'''Given a dataset of concerts, count the number of concerts per (artist, venue), per year
month. Make the resulting table be a wide table - one row per year month with a column
for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
to determine which (artist, venue) pairs to include in the result.'''

import pandas as pd

data = {
    'artist': ['Artist A', 'Artist B', 'Artist A', 'Artist A', 'Artist B', 'Artist C', 'Artist A'],
    'venue': ['Venue X', 'Venue Y', 'Venue X', 'Venue Z', 'Venue Y', 'Venue X', 'Venue Z'],
    'date': ['2023-01-15', '2023-01-20', '2023-02-10', '2023-02-12', '2023-03-05', '2023-03-10', '2023-03-15']
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

concert_count = df.groupby(['artist', 'venue', 'year_month']).size().reset_index(name='concert_count')

artists = df['artist'].unique()
venues = df['venue'].unique()
year_months = df['year_month'].unique()

cross_product = pd.MultiIndex.from_product([artists, venues, year_months], names=['artist', 'venue', 'year_month'])

concert_count = concert_count.set_index(['artist', 'venue', 'year_month']).reindex(cross_product, fill_value=0).reset_index()

result = concert_count.pivot_table(index='year_month', columns=['artist', 'venue'], values='concert_count', fill_value=0)

print(result)
