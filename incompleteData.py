import pandas as pd

from dataframe import get_data, plot_data

if __name__ == '__main__':
    symbol_list = ["JAVA"]
    start_date = "2005-12-31"
    end_date = "2014-12-07"

    idx = pd.date_range(start_date, end_date)

    df_data = get_data(symbol_list, idx)
    df_data.fillna(method="ffill", inplace=True)  # First forward
    df_data.fillna(method="bfill", inplace=True)  # Then backward
    # Forward -> Backward, to avoid future peeking. Due to it is really bad
    plot_data(df_data)
