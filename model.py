class Order:
    '''Класс сделки. Имя бумаги, цена покупки отражается в балансе.

    При закрытии продает бумагу с ценой закрытия'''
    items = []

    def __init__(self, name: str):
        self.name = name
        self.balance = 0
        Order.items.append(self)

    def __str__(self):
        return '{0}. Ticker: {1}, Balance: {2}'.\
            format(self.items.index(self)+1,self.name,self.balance)

    def buy(self, price_in, lots):
        self.balance = self.balance - price_in * lots
        return self.balance

    # Для шортов пока не делаем
    def sell(self, price_in, lots):
        self.balance = self.balance + price_in * lots
        return self.balance

    def close(self, price_out):
        if self.balance < 0:
            self.sell(price_out, self.lots)
        else:
            self.buy(price_out, self.lots)