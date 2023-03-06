import pandas as pd

movies_csv = pd.read_csv('datasets/movies.csv')

# print(movies_csv.info())
# print("\n---\n")
# print(movies_csv.isna().sum())
# movies_csv = movies_csv.dropna()
# print("\n---\n")
# print(movies_csv.info())
# print(movies_csv.isna().sum())

genresVal = []
for i in range(len(movies_csv)):
    genresVal = genresVal + movies_csv.loc[i,"genres"].split('|')
    genresVal = list(set(genresVal))
print(genresVal)
"""
['Thriller', 'Western', 'Sci-Fi', '(no genres listed)', 
'Documentary', 'Animation', 'Adventure', 'Film-Noir', 
'IMAX', 'Drama', 'War', 'Mystery', 'Comedy', 'Horror', 
'Fantasy', 'Romance', 'Children', 'Crime', 'Musical', 'Action']
"""

print(len(movies_csv))
movies_csv.drop(movies_csv[(movies_csv['genres'] == '(no genres listed)')].index, inplace=True)
# print(movies_csv.head())
print(len(movies_csv))
print()