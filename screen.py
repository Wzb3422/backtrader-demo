import datetime
import backtrader as bt
from strategies import *

#Instantiate Cerebro engine
cerebro = bt.Cerebro()

#Add data to Cerebro
instruments = ['0005', '0700', '3690', '9988']
for ticker in instruments:
    data = bt.feeds.YahooFinanceCSVData(
        dataname='./data/{}.HK_5Y.csv'.format(ticker),
        fromdate=datetime.datetime(2019, 1, 1),
        todate=datetime.datetime(2020, 10, 30))
    cerebro.adddata(data) 

#Add analyzer for screener
cerebro.addanalyzer(Screener_SMA)

if __name__ == '__main__':
    #Run Cerebro Engine
    cerebro.run(runonce=False, stdstats=False, writer=True)