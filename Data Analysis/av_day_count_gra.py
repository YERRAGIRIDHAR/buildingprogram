import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])


data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).count()
print(day_average.head())

print(plt.figure(figsize=(25,3)))
print(plt.plot(day_average.index, day_average['Rating']))
print(plt.show())


