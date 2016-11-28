''' Build a dataframe in pandas '''
import os

import matplotlib.pyplot as plt
import pandas as pd


def test_run():
    df = get_data(
        ['SPY', 'GOOG', 'IBM', 'GLD'],
        pd.date_range('2010-01-01', '2010-12-31')
    )

    plot_data(normilise_data(df))

    print df.ix['2010-03-15': '2010-03-10', ['SPY', 'IBM']].iloc[::-1]


def get_data(symbols, dates):
    # Create an empty dataframe
    data_frame = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = read_symbol(symbol).rename(columns={'Adj Close': symbol})
        # Using inner we can drop holidays (NaN)
        data_frame = data_frame.join(df_temp, how='inner')

    return data_frame.iloc[::-1]


def read_symbol(symbol):
    return pd.read_csv(
        symbol_to_path(symbol),
        index_col="Date",  # Otherwise index 0,1,2 will be used
        parse_dates=True,
        usecols=['Date', 'Adj Close'],
        na_values=['nan']  # convert string to NaN, to be used in dropna
    )


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def plot_data(df, title="Stock prises"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def normilise_data(df):
    """Normalize stock prices using the first row of the dataframe"""
    # In such way all prices will start with one dollar 30 / 30 = 0
    return df / df.ix[0, :]


if __name__ == "__main__":
    test_run()
