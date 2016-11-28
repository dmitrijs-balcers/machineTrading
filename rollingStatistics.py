import matplotlib.pyplot as plt
import pandas as pd

from consts import SPY, XOM
from dataframe import get_data, plot_data


def test_run():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    df = get_data([SPY], dates)

    ax = df[SPY].plot(title="SPY rolling mean", label=SPY)
    # Plot SPY data, retain matplotlib axis object
    rm_SPY = pd.rolling_mean(df[SPY], window=20)
    rm_SPY.plot(label="Rolling mean", ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Date")
    ax.legend(loc="upper left")
    plt.show()


def compute_bollinger_bands():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    df = get_data([SPY], dates)
    rm_spy = get_rolling_mean(df[SPY])
    rstd_spy = get_rolling_std(df[SPY])
    upper_band, lower_band = get_bollinger_bands(rm_spy, rstd_spy)

    ax = df[SPY].plot(title="SPY rolling mean", label=SPY)
    rm_spy.plot(label="Rolling mean", ax=ax)
    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Date")
    ax.legend(loc="upper left")
    plt.show()


def get_rolling_mean(df, window=20):
    return pd.Series(df).rolling(window).mean()


def get_rolling_std(df, window=20):
    return pd.Series(df).rolling(window).std()


def get_bollinger_bands(rm_SPY, rstd_SPY):
    return rm_SPY + 2 * rstd_SPY, rm_SPY - 2 * rstd_SPY


def daily_returns():
    dates = pd.date_range('2012-07-01', '2012-07-31')
    df = get_data([SPY, XOM], dates)
    # plot_data(df)
    # print df
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns")


def compute_daily_returns(df):
    # dr = df.copy()
    # # compute daily returns for row 1 onwards
    # # [:-1] 0 -> df.length - 1
    # # we use .values to access NumPy array
    # dr[1:] = (df[1:] / df[:-1].values) - 1  # we are trying to get %
    # # ix[0, :] for 0 row in all columns
    # dr.ix[0, :] = 0  # set daily returns for row 0 to 0
    # return dr

    dr = (df / df.shift(1)) - 1
    dr.ix[0, :] = 0  # set daily returns for row 0 to 0
    return dr


def comulative_returns():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    df = get_data([SPY, XOM], dates)
    # plot_data(df)
    # print df
    cr = compute_comulative_returns(df)
    plot_data(cr, title="Comulative returns")


def compute_comulative_returns(df):
    dr = (df / df.ix[0, :]) - 1
    return dr


if __name__ == "__main__":
    comulative_returns()
