import matplotlib.pyplot as plt
import pandas as pd

from consts import SPY, XOM
from dataframe import get_data
from rollingStatistics import compute_daily_returns


def test_run():
    dates = pd.date_range("2009-01-01", "2012-12-31")
    df = get_data([SPY, XOM], dates)

    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns")

    daily_returns[SPY].hist(bins=20, label=SPY)
    daily_returns[XOM].hist(bins=20, label=XOM)
    plt.legend(loc="upper right")

    mean = daily_returns[SPY].mean()
    print "mean= ", mean

    std = daily_returns[SPY].std()
    print "std= ", std

    # plt.axvline(mean, color="w", linestyle="dashed", linewidth=2)
    # plt.axvline(std, color="r", linestyle="dashed", linewidth=2)
    # plt.axvline(-std, color="r", linestyle="dashed", linewidth=2)
    plt.show()

    print daily_returns.kurtosis()


if __name__ == "__main__":
    test_run()
