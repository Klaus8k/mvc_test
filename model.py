class Order:
    def __init__(self, name: str):
        self.name = name
        self.balance = 0

    def __str__(self):
        return (f'{self.name}, {self.balance}')

    def buy(self, price_in, lots):
        self.balance = self.balance - price_in * lots
        return self.balance

    def sell(self, price_in, lots):
        self.balance = self.balance + price_in * lots
        return self.balance

    def close(self, price_out):
        if self.balance < 0:
            self.sell(price_out, self.lots)
        else:
            self.buy(price_out, self.lots)