import pandas as pd
"""
only drop the na value
"""
def get_links_csv():
    links_csv = pd.read_csv('datasets/links.csv')
    # print(links_csv.info())
    # print("\n---\n")
    # print(links_csv.isna().sum())
    links_csv = links_csv.dropna()
    # print("\n---\n")
    # print(links_csv.info())
    return links_csv

