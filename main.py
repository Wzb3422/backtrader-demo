import datetime
import backtrader as bt
import os.path  # To manage paths
import sys
from strategies import *

#Instantiate Cerebro engine
cerebro = bt.Cerebro()

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, './data/0700.HK.csv')

data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    fromdate=datetime.datetime(2018, 6, 7),
    todate=datetime.datetime(2019, 6, 7),
)
cerebro.adddata(data) 

#Add strategy to Cerebro
cerebro.addstrategy(MAcrossover)

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    # Run Cerebro Engine
    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run()

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')