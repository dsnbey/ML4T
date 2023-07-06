import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv('GOOG.csv')
    df = pd.concat([df.iloc[0:6, 1:2], df.iloc[21:29, 1:2], df.iloc[44:50, 1:2], df.iloc[148:155, 1:2]])
    return df.reset_index(drop=True)


def calculate_bollinger_bands(df, window_size=3, num_std=2):
    rolling_mean = df['Open'].rolling(window=window_size).mean()
    rolling_mean.columns = ['Rolling Mean']
    rolling_std = df['Open'].rolling(window=window_size).std()
    rolling_std.columns = ['Rolling ']
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    return upper_band, lower_band, rolling_mean


def plot_bollinger_bands(df, upper_band, lower_band, rolling_mean):
    ax = df.plot(title='GOOG Price with Bollinger Bands', legend=True)
    upper_band.plot(label='Upper Band', ax=ax)
    lower_band.plot(label='Lower Band', ax=ax)
    rolling_mean.plot(label='Rolling Mean', ax=ax)  # Plot the rolling mean
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = load_data()
    upper_band, lower_band, rolling_mean = calculate_bollinger_bands(data)
    plot_bollinger_bands(data, upper_band, lower_band, rolling_mean)
