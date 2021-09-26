import backtrader.analyzers as btay

class TestStrategy(bt,Strategy):
    def __init__(self):
        self.dataclose=self.datas[0].close
        self.order=None
        self.buyprice=None
        self.buycomm=None
    def next(self):
        if self.order:
            return
        if not self.position:
            if self.sma

cerebro=bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
startcash=10000
cerebro.broker.setcash(startcash)
cerebro.broker.setcommission(commission=0.0005)

d1=start.strftime('%Y%m%d')
d2=end.strftime(%Y%m%d)


cerebro.addanalyzer(btay.SharpeRatio,_name='sharpe')
resutlts=cerebro.run()
portvalue=cerebro.broker.getvalue()
pn1=portvalue-startcash

print(resutls[0].analyzers.sharpe.get_analysis())