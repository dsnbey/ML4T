import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame


def read_data():
    df = pd.read_csv('GOOG.csv')
    df = df.set_index('Date')
    df = df.iloc[:, :1]
    return df


def compute_daily_returns(df: pd.DataFrame):
    d_returns: DataFrame = df.pct_change()
    d_returns.hist(bins=20)
    plt.show()
    d_returns = d_returns.reset_index() # for to scatter plot work
    d_returns.plot.scatter(x='Date', y=df.columns[0])
    plt.show()
    d_returns.set_index('Date')
    d_returns.fillna(method='bfill', inplace=True)
    d_returns.rename(columns={'Open': 'Return'}, inplace=True)
    print(d_returns)
    return d_returns


def stats(df: pd.DataFrame):
    mean = df.mean()
    std = df.std()
    return mean, std


if __name__ == "__main__":
    data = read_data()
    returns = compute_daily_returns(data)

    #stats_data = stats(data)
    #stats_returns = stats(returns)
    #print(stats_returns)
    #print(stats_data)



