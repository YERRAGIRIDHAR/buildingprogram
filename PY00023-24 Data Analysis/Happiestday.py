import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['Daynumber'] = data['Timestamp'].dt.strftime('%w')

weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')
print(weekday_average)
print("..........................")
print(weekday_average.index.get_level_values(0))
#print(plt.figure(figsize=(25,3)))
print(plt.plot(weekday_average.index.get_level_values(0), weekday_average['Rating']))
#print(plt.show())


'''Number of Rating by course'''
share = data.groupby(['Course Name'])['Rating'].count()
print(share)
plt.pie(share, labels=share.index)
print(plt.show())