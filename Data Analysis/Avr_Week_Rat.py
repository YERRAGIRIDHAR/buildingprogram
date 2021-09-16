import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

'''Average Rating By Weeek'''

data['Week'] = data['Timestamp'].dt.strftime('%Y %U')
week_average = data.groupby(['Week']).mean()
print(week_average)
print(".......................")
print(week_average['Rating'])

# data['Week'] = data['Timestamp'].dt.strftime('%Y %U')
# week_average = data.groupby(['Week']).count()
# print(week_average)

print(plt.figure(figsize=(30,3)))
print(plt.plot(week_average.index, week_average['Rating']))
print(plt.show())