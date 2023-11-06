import pandas as pd

data = pd.Series(data=[0, 1, 2, 3], index=["a", "b", "c", "d"])

print(data.values)
print(data.index)
print(type(data.values))
print(data["a":"d"])

data_dict = {"0": "a", "1": "b", "2": "c", "3": "d"}
data = pd.Series(data=data_dict)

print(data.values)
print(data.index)
print(data[0:2])