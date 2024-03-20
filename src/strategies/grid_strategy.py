import backtrader as bt


class EMAMACDScalpingStrategy(bt.Strategy):
    params = (
        ('short_ema_period', 12),
        ('medium_ema_period', 26),
        ('long_ema_period', 50),
        ('macd1', 12),
        ('macd2', 26),
        ('macdsignal', 9),
    )

    def __init__(self):
        # Initialize EMAs
        self.ema_short = bt.indicators.EMA(
            self.data.close, period=self.params.short_ema_period)
        self.ema_medium = bt.indicators.EMA(
            self.data.close, period=self.params.medium_ema_period)
        self.ema_long = bt.indicators.EMA(
            self.data.close, period=self.params.long_ema_period)

        # Initialize MACD
        self.macd = bt.indicators.MACD(self.data.close,
                                       period_me1=self.params.macd1,
                                       period_me2=self.params.macd2,
                                       period_signal=self.params.macdsignal)

        # To keep track of pending orders
        self.order = None

    def next(self):
        if self.order:
            return  # If an order is pending, do not send another one

        # Check for buy signals
        if self.ema_short > self.ema_medium > self.ema_long and self.macd.lines.macd > self.macd.lines.signal:
            self.order = self.buy()

        # Check for sell signals
        elif self.ema_short < self.ema_medium < self.ema_long or self.macd.lines.macd < self.macd.lines.signal:
            self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Order submitted/accepted - nothing to do
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, {order.executed.price}')
            elif order.issell():
                self.log(f'SELL EXECUTED, {order.executed.price}')
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Reset orders
        self.order = None

    def log(self, txt, dt=None):
        '''Logging function'''
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')
