import model
import view


class Order():
    """Класс сделки. Со словарем атрибутов"""
    id = 0

    def __init__(self, ticker):
        self.ticker = ticker
        Order.id += 1
        self.id = Order.id
        self.price = []
        self.lots = []
        self.sum_order = [self.price, self.lots]
        self.long = True


    def __str__(self):
        return f'{self.id}. {self.ticker}. lots: {sum(self.lots)} \
        for {self.price}\nmid = {self.sum_order}'

    def buy(self):
        p_l = view.price_lots()
        self.price.append(p_l[0])
        self.lots.append(p_l[1])
        # Посчитать на основе списка списков sum_order

    def sell(self):
        p_l = view.price_lots()
        self.price.append(-p_l[0])
        self.lots.append(-p_l[1])

    def mid(self):
        pass


if __name__ == '__main__':
    responce = view.main_action()
    a = Order('GZP')
    a.price.append(10)
    a.lots.append(1)
    all_orders = [a]
    while responce != '0':
        if responce == '1':
            order = Order(view.ticker())
            all_orders.append(order)
            if view.buy_or_sell() == '1':
                order.buy()
            else:
                order.sell()
                order.long = False
        elif responce == '2':
            view.show_all(all_orders)
            order_number = view.choose_order()
            view.show_current(all_orders[order_number])
            responce = view.buy_or_sell()
            if responce == '1':
                all_orders[order_number].buy()
            elif responce == '2':
                all_orders[order_number].sell()
            elif responce == '0':
                all_orders[order_number].close()# Пока не реализовано


        elif responce == '3':
            view.show_all(all_orders)

        responce = view.main_action()
