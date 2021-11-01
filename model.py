class Order:
    items = []

    def __init__(self, name: str):
        self.name = name
        self.balance = 0
        Order.items.append(self)

    def __str__(self):
        return f'{self.items.index(self)+1}. Ticker: {self.name}, Balance: {self.balance}'

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