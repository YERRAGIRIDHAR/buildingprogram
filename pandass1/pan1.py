import pandas as pd
x = pd.DataFrame([[1,2,3],[6,7,52]])
print(x)    
print(".............")
x2 = pd.DataFrame([[1,2,3],[12,22,23]], columns =   ["price","age","name"], index=["val1","val2"])
print(x2)
print("...........")
x3=x2.mean()
print(x3)
print("...........")
x3=x2.mean().mean()
print(x3)
print('.............')
y1=pd.read_csv("F:\PYTHON BASICS\pandass1\supermarkets\supermarkets.csv")
print(y1)
print(".....................................")
y2=pd.read_json("F:\PYTHON BASICS\pandass1\supermarkets\supermarkets.json")
print(y2.set_index("ID"))
print("......................................")
y3=pd.read_excel("F:\PYTHON BASICS\pandass1\supermarkets\supermarkets.xlsx")
print(y3)
print(".............................................")
y4=pd.read_csv("F:\PYTHON BASICS\pandass1\supermarkets\supermarkets-semi-colons.txt",)
print(y4)
print(".........................")
