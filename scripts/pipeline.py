import pandas as pd

#file dir
file_dir = "/workspaces/COMP603_assignment2/data/movies.csv"
file_dir2 = "/workspaces/COMP603_assignment2/data/tags.csv"
file_dir3 = "/workspaces/COMP603_assignment2/data/ratings.csv"

#open
with open(file_dir, mode='r') as file:
    df_data = pd.read_csv(file_dir)
with open(file_dir2, mode='r') as file2:
    df_data2 = pd.read_csv(file_dir2)
with open(file_dir3, mode='r') as file3:
    df_data3 = pd.read_csv(file_dir3)

#print
print(df_data.head(5))
print(df_data2.head(5))
print(df_data3.head(5))

#delete timestamp
dropped_columns2 = df_data2.drop(columns="timestamp")
dropped_columns3 = df_data3.drop(columns="timestamp")
print(f"verified drop columns: {dropped_columns2}")
print(f"verified drop columns: {dropped_columns3}")

#access data
row_0 = df_data2.iloc[0]
print(row_0)
print(type(row_0))
row_0.index
print(row_0['userId'])
print('ratings' in row_0)
print(row_0.name)

#descriptive stats
print(df_data3.describe())

print(df_data3.mode())

numeric_columns = ['userId', 'movieId', 'rating']
numeric_columns_data = df_data3[numeric_columns]
print(numeric_columns_data.corr())