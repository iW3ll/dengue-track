import pandas as pd

url = 'https://info.dengue.mat.br/api/alertcity?geocode=2905701&disease=dengue'
search_filter = (
    'geocode=2905701&disease=dengue&format=csv&' +
    'ew_start=1&ew_end=50&ey_start=2023&ey_end=2024'
)
df = pd.read_csv('%s?%s' % (url, search_filter))
print(df)
df.head()
