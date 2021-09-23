import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

# '''Average Rating By Month'''

# data['Month'] = data['Timestamp'].dt.strftime('%Y %m')
# month_average = data.groupby(['Month']).mean()
# print(month_average)

# print(plt.figure(figsize=(30,3)))
# print(plt.plot(month_average.index, month_average['Rating']))
# print(plt.show())

'''Avrag Rating By Month By Course'''

data['Month'] = data['Timestamp'].dt.strftime('%Y %m')
month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack()
print(month_average_crs[-20:])

print(plt.figure(figsize=(30,3)))
print(plt.plot(month_average_crs.index, month_average_crs['Rating']))
print(plt.show())
