import pandas as pd
data = pd.read_csv('artwork_sample.csv')
# data = pd.read_csv('artwork_sample.csv', usecols=['artist', 'title'])


# print(data.head())
# print(data.columns.str.lower())
# data.columns = [x.lower() for x in data.columns]
# import re
# data.colums = [re.sub(r'([A-Z])', r'_\1', x).lower() for x in data.columns]
# data.rename(columns={'thumbnailUrl': 'thumbnail'}, inplace=True)
# data.rename(columns=lambda x: x.lower(), inplace=True)
# print(data.columns)


# print(data[0:2])
# print(data.loc[0:2, :])
# print(data.loc[[1, 5], ['artist', 'title']])
# print(data.loc[[1, 5], 'id':'artistId'])
# print(data.loc[data.artist == 'Blake, Robert', :])
# print(data.iloc[0:3, :])
# print(data.loc[data.medium.str.contains('Graphite', case=False), ['artist', 'medium']])
# print(data.loc[data.medium.str.contains('graphite|line', case=False, regex=True), ['artist', 'medium']])
# print(data.loc[data.dimensions.str.contains('support', na=False)])


# print(data.loc[data.title.str.contains('\s$', regex=True)])
# print(data.title.str.strip())
# print(pd.isna(data.loc[:, 'dateText']))
from numpy import nan
# print(data.replace({'dateText': {'date not known': nan}} inplace=True))
# data.loc[data.dateText == 'date not known', ['dateText']] = nan
# data.fillna(value={'depth': 0}, inplace=True)
# print(data.depth)
# data.dropna()
# print(data.shape)
data.drop_duplicates(subset=['artist'], keep='first', inplace=True)
print(data)