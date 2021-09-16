import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

'''Average Rating Of Day By Day'''

data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()
print(day_average)
print(type(day_average))
print(".......................")
print(day_average.columns)
print(type(day_average.columns))
print(".................")
print(day_average.index)
print(type(day_average.index))
print("..................................")
print(list(day_average.index))
print("..............")
print(day_average['Rating'])
print(type(day_average['Rating']))
print("...................")
print(day_average['Rating'].mean())
print(type(day_average['Rating'].mean()))
print("...................................")

print(plt.figure(figsize=(25,3)))
print(plt.plot(day_average.index, day_average['Rating']))
print(plt.show())