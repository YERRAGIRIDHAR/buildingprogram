import pandas as pd
data = pd.read_csv("reviews.csv")
print(data.head())
print("............")
print(data.shape)
print(".........")
print(data.hist("Rating"))