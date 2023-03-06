tags_csv = pd.read_csv('datasets/tags.csv')

print(tags_csv.info())
print("\n---\n")
print(tags_csv.isna().sum())
tags_csv = tags_csv.dropna()
print("\n---\n")
print(tags_csv.info())
