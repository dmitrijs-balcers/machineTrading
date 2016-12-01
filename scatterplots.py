import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from consts import SPY, XOM, GLD
from dataframe import get_data
from rollingStatistics import compute_daily_returns


def test_run():
    dates = pd.date_range("2009-01-01", "2012-12-31")
    df = get_data([SPY, XOM, GLD], dates)

    daily_returns = compute_daily_returns(df)
    spy_daily_returns = daily_returns[SPY]
    xom_daily_returns = daily_returns[XOM]
    daily_returns.plot(kind="scatter", x=SPY, y=XOM)
    beta_XOM, alpha_XOM = np.polyfit(spy_daily_returns, xom_daily_returns, 1)
    plt.plot(spy_daily_returns, beta_XOM * spy_daily_returns + alpha_XOM, "-", color="r")
    plt.show()

    gld_daily_returns = daily_returns[GLD]
    daily_returns.plot(kind="scatter", x=SPY, y=GLD)
    beta_GLD, alpha_GLD = np.polyfit(spy_daily_returns, gld_daily_returns, 1)
    plt.plot(spy_daily_returns, beta_GLD * spy_daily_returns + alpha_GLD, "-", color="r")
    plt.show()

    print daily_returns.corr(method="pearson")


if __name__ == "__main__":
    test_run()
