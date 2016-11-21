import pandas as pd
import matplotlib.pyplot as plt

def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()


def get_mean_volume(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()

def showPlot():
    df = pd.read_csv("data/AAPL.csv")
    print df['Adj Close']
    df[['Close', 'Adj Close']].plot()
    plt.show()

def test_run():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Max close"
        print symbol, get_max_close(symbol)

    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)

    showPlot()


if __name__ == "__main__":  # If run standalone
    test_run()
