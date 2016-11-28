import pandas as pd

import consts
import dataframe


def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = [consts.SPY, consts.XOM, consts.GOOG, consts.GLD]
    df = dataframe.get_data(symbols, dates)
    dataframe.plot_data(df)

    # Mean is the average of set of values
    # Median value in the middle when they are all sorted
    # Standard deviation (std) square root of variants
    # It is a measure of deviation of central value which is mean.
    # Higher number means that stock has varied over
    # time more then other stocks.

    # Global Statistics: mean, median, std, sum, prod, mode, etc....

    print df.mean()


if __name__ == "__main__":
    test_run()
