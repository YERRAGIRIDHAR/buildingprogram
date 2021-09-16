import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, tzinfo
from pytz import utc

'''overview of dataframe'''

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
print(data)

print("......")

print(data.head())

print("............")

print(data.shape)

print(".........")

print(data.columns)

print(".................")

print(data['Course Name'].unique())


'''seleing data from the dataframe'''
'''select a column'''

print(data['Rating'])

'''select multiple cloumns'''

print(data[['Timestamp','Rating']])

'''select a row'''

print(data.iloc[3])

'''select multiple row'''

print(data.iloc[1:3])

'''selecting a section'''

print(data[['Timestamp','Rating']].iloc[2:5])

'''selecting a cell'''

print(data['Rating'].iloc[3])
print("...........")
print(data.at[3, 'Rating'])

'''Filtring data based on conditions'''
'''one condition'''

print(data[data['Rating'] > 4])

'''multiple cionditions'''

print(data[data['Rating'] > 4].mean()) #we count the data['Rating] > 4 & len too
print("...............")
print(data[(data['Rating'] > 4) & (data['Course Name'] =='The Complete Python Course: Build 10 Professional OOP Apps')])
print("...............................................................")
print(data[(data['Rating'] > 4) & (data['Course Name'] =='The Complete Python Course: Build 10 Professional OOP Apps')]
      ['Rating'].mean())
print("..........................................................................")
# first we have to import datetime from datetime
#print(data[(data['Timestamp'] >= datetime(2020, 7, 1) ) & (data['Timestamp'] <= datetime(2020, 12, 31))])
# Beforr run this, We have read the file by including 'parse_datetime=' in data
# import utc from pytz
print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc) ) & 
     (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))])

'''From Data into Information'''
'''Average rating''' '''for a particular course'''

print(data['Rating'].mean())

'''Average rating for a particular course'''

print(data[data['Course Name'] == 'The Complete Python Course: Build 10 Professional OOP Apps']['Rating'].mean())

'''Average rating for a period'''

print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc) ) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))]['Rating'].mean())

'''Average rating for particular period and for a particular course'''

print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc)) & 
           (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc)) & 
           (data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications')]['Rating'].mean())

'''Average of un commented ratings'''

print(data[data['Comment'].isnull()]['Rating'].mean())

'''Average of commented ratings'''

print(data[data['Comment'].notnull()]['Rating'].mean())

'''Number of un commented ratings'''

print(data[data['Comment'].isnull()]['Rating'].count())

'''Number of commnted ratings'''

print(data[data['Comment'].notnull()]['Rating'].count())

'''number of comments containing a certain word'''

print(data[data['Comment'].str.contains('good', na=False)].count())

'''Averag of commented ratings with 'accent' in comments'''

print(data[data['Comment'].str.contains('good', na=False)]['Rating'].mean())
print("................................")
print(data.hist('Rating'))
plt.show()
