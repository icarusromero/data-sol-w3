import pandas as pd
data = pd.read_csv('artwork_sample.csv')
# data = pd.read_csv('artwork_sample.csv', usecols=['artist', 'title'])

# print(data.head())
# print(data.columns.str.lower())
# data.columns = [x.lower() for x in data.columns]
# import re
# data.colums = [re.sub(r'([A-Z])', r'_\1', x).lower() for x in data.columns]
data.rename(columns={'thumbnailUrl': 'thumbnail'}, inplace=True)
data.rename(columns=lambda x: x.lower(), inplace=True)
print(data.columns)