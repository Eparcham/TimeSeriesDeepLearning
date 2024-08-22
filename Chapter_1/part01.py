import pandas as pd

data = pd.read_csv('H:/TimeSeries/book/assets/datasets/time_series_solar.csv',
                   parse_dates=['Datetime'],
                   index_col='Datetime')

series = data['Incoming Solar']
print(series)