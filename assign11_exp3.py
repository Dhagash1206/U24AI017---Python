"""After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
were on vacation, youre now in the market for a new vehicle. Your insurance didnt cover
the loss, so you want to make sure you get a good deal on your new car."""

import pandas as pd

asking_prices = pd.Series([24000, 18000, 22000, 27000, 16000])
fair_prices = pd.Series([25000, 20000, 21000, 26500, 17000])

good_deal_indices = asking_prices[asking_prices < fair_prices].index.tolist()

print("Good deal indices:", good_deal_indices)
