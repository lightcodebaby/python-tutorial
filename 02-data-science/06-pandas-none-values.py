import pandas as pd

my_dataframe = pd.DataFrame([{"a": 0, "b": 1}, {"b": -1, "c": -2}])
print(my_dataframe)

my_dataframe = my_dataframe.fillna(0)
print(my_dataframe)