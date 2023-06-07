import datetime
import backtrader as bt
import os.path  # To manage paths
import sys
from strategies import *

#Instantiate Cerebro engine
cerebro = bt.Cerebro(optreturn=False,stdstats=True)

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, './data/0700.HK_5Y.csv')

data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    fromdate=datetime.datetime(2019, 6, 7),
    todate=datetime.datetime(2020, 6, 7),
)
cerebro.adddata(data) 

cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_ratio')
cerebro.optstrategy(MAcrossover, pfast=range(5, 20), pslow=range(50, 100))  

# Default position size
cerebro.addsizer(bt.sizers.SizerFix, stake=3)

if __name__ == '__main__':
    optimized_runs = cerebro.run()

    final_results_list = []
    for run in optimized_runs:
        for strategy in run:
            PnL = round(strategy.broker.get_value() - 10000, 2)
            sharpe = strategy.analyzers.sharpe_ratio.get_analysis()
            final_results_list.append([strategy.params.pfast, 
                strategy.params.pslow, PnL, sharpe['sharperatio']])

    sort_by_sharpe = sorted(final_results_list, key=lambda x: x[3], 
                             reverse=True)
    for line in sort_by_sharpe[:10]:
        print(line)

    cerebro.plot()