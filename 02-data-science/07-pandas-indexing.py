import pandas as pd

my_dataframe = pd.Series(["a", "b", "c"], index=[1, 3, 5])
print(my_dataframe[1])
print(my_dataframe[1:3])
print(my_dataframe.loc[1:3]) # Explicit index
print(my_dataframe.iloc[1:3]) # Implicit index

grades_dict = {"A": 4, "A-": 3.5, "B": 3, "B-": 2.5, "C": 2}
marks_dict = {"A": 85, "A-": 80, "B": 75, "B-": 65, "C": 60}
data = pd.DataFrame(data={"grades": grades_dict, "marks": marks_dict})
print(data)
print(data.iloc[2:]) # All rows starting from 2
print(data.iloc[2,:]) # Row number 2
print(data.iloc[::-1,:]) # All rows reversed