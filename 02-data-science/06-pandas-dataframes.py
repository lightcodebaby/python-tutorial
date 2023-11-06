import pandas as pd

grades_dict = {"A": 4, "A-": 3.5, "B": 3, "B-": 2.5, "C": 2}
marks_dict = {"A": 85, "A-": 80, "B": 75, "B-": 65, "C": 60}
data = pd.DataFrame(data={"grades": grades_dict, "marks": marks_dict})

print(data)
print(data.T)
print(data.values)
print(data.columns)

data["scaled_marks"] = 100*(data["marks"]/90)
print(data)

del data["scaled_marks"]
print(data)

approved = data[data["marks"] >= 75]
print(approved)