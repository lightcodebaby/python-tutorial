import pandas as pd

my_dataframe = pd.read_csv("./my_csv_file.csv")
my_dataframe.head(n=10)
my_dataframe.drop(["SNo", "Last Update"], axis=1, inplace=True)
my_dataframe.rename(
    columns={
        "ObservationDate": "Date",
        "Province/State": "Province",
        "Country/Region": "Country",
    },
    inplace=True,
)
my_dataframe["Date"] = pd.to_datetime(my_dataframe["Date"])

print(my_dataframe.describe())
print(my_dataframe.info())

grouped_df = (
    my_dataframe.groupby(["Country", "Date"])[
        ["Country", "Date", "Data Column 1", "Data Column 2", "Data Column 3"]
    ]
    .sum()
    .reset_index()
)

filtered_df = my_dataframe[my_dataframe["Data Column 2"] > 100]
