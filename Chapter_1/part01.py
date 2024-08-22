import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dir = "H:/TimeSeries/book/TimeSeriesDeepLearning/assets"

data = pd.read_csv(f'{dir}/datasets/time_series_solar.csv',
                   parse_dates=['Datetime'],
                   index_col='Datetime')

series = data['Incoming Solar']
print(series)

def plot_result(series_df, name_file = 'time_series_plot'):
    series.plot(figsize=(12, 6), title='Solar radiation time series')

    plt.rcParams['figure.figsize'] = [12, 6]
    sns.set_theme(style='darkgrid')

    sns.lineplot(x='Datetime',
                 y='Incoming Solar',
                 data=series_df)

    plt.ylabel('Solar Radiation')
    plt.xlabel('')
    plt.title('Solar radiation time series')

    name_ =f'{dir}/{name_file}.png'
    plt.savefig(name_)
    plt.show()
##

series_df = series.reset_index()
plot_result(series_df)


series_daily = series.resample('D').sum()
series_df = series_daily.reset_index()

plot_result(series_df, name_file = 'daily')