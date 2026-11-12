import pandas as pd
import matplotlib.pylab as plt
import re

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
df_data2 = df_data2.drop(columns="timestamp")
df_data3 = df_data3.drop(columns="timestamp")
print(f"verified drop columns: {df_data2}")
print(f"verified drop columns: {df_data3}")

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

#filter
positive_ratings_filter = df_data3[df_data3['rating']>0]

#group
grouped = positive_ratings_filter.groupby(df_data3['movieId'])
grouped_and_averaged = grouped.mean()
print(grouped_and_averaged)

#handling missing data
columns_to_handle = ['userId', 'rating']
df_data3 = df_data3[columns_to_handle].apply(pd.to_numeric, errors="coerce")

print(df_data.shape)
print(df_data.isnull().sum())

print(df_data2.shape)
print(df_data2.isnull().sum())

print(df_data.shape)
print(df_data.isnull().sum())

#16 null cells in tags['tag']
df_data2 = df_data2.dropna()
print(df_data2.isnull().sum())
print(df_data2.shape)

#plot histogram
df_data3.hist(column="rating", figsize=(15, 10), bins=10)
plt.savefig('../img/show_histogram')

#get information from columns
print(df_data2.head())
print(df_data[['title', 'genres']])
print(df_data3.iloc[-10])
print(df_data3[-10:])
print(df_data3.tail())
print(df_data3.tail(10))
df_data2_count = df_data2['tag'].value_counts()
print(df_data2_count.head())
plt.clf()
df_data2_count.head().plot(kind="bar", figsize=(12, 8))
plt.savefig('../img/show_barchart.png')
plt.clf()
df_data2_count.head(60).plot(kind="bar", figsize=(12, 8))
plt.savefig('../img/show_barchart(60).png')
plt.clf()
df_data2_count[60:100].plot(kind="bar", figsize=(12,8))
plt.savefig('../img/show_barchart(60colon100).png')
is_highly_rated = df_data3['rating']>4
print(df_data3[is_highly_rated].head())
is_animation = df_data['genres'].str.contains("Animation")
print(df_data[is_animation].head())
ratings_count = df_data3.groupby("rating").count()
print(ratings_count)
print(f"Average of ratings of all movies: {grouped_and_averaged['rating'].mean(axis=0)}")
average_ratings_bymovies = positive_ratings_filter[['rating', 'movieId']].groupby('movieId').mean()
print(average_ratings_bymovies.head())
average_ratings_bymoviestopdown = average_ratings_bymovies.sort_values('rating', ascending=False)
print(average_ratings_bymoviestopdown.head())
# changing order of placing the 2 tables to be merged in the parameters brackets of pd.merge() according to the question (Merge the average ratings with movie titles) is a good practice of protecting fact table data (or "main concerned" in this case)
df_data3 = pd.merge(average_ratings_bymoviestopdown, df_data, how="inner", on="movieId")
df_data3.drop(columns="genres")
print(df_data3.head())
is_comedy = df_data3['genres'].str.contains("Comedy")
is_comedy = df_data3[is_comedy]
print(is_comedy.head())
is_highly_rated2 = is_comedy[is_comedy['rating']>=4.0]
print(is_highly_rated2.head())
#use df_data3 instead of df_data to do the following q's
def find_release_year(list_of_titles):
    match = re.search(r'\((\d{4})\)', str(list_of_titles))
    if match:
        return match.group(1)
    else:
        return None

df_data3['release_year'] = df_data3['title'].apply(find_release_year)
print(df_data3['release_year'].head()) 
average_rating_peryear = df_data3[['release_year', 'rating']].groupby('release_year').mean()
print(average_rating_peryear.head())
plt.clf()
average_rating_peryear.plot(kind="line", figsize=(12, 8))
plt.savefig("../img/show_line.png")