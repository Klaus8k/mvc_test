import model
import view


class Order():
    """Класс сделки. Со словарем атрибутов"""
    id = 0

    def __init__(self, ticker):
        self.ticker = ticker
        Order.id += 1
        self.id = Order.id
        self.param = {'ticker': self.ticker,
                      'mid': 0,
                      'lots_in': [],
                      'p_in': [],
                      'long': True}

    def __str__(self):
        return f'{self.id} --- {str(self.param)}'

    def buy(self):
        p_l = view.price_lots()
        self.param['p_in'].append(p_l[0])
        self.param['lots_in'].append(p_l[1])
        # mid = model.medium(order.param['p_in'], order.param['lots_in'])

    def sell(self):
        p_l = view.price_lots()
        self.param['p_in'].append(-p_l[0])
        self.param['lots_in'].append(-p_l[1])

    def close(
            self):  # Разобраться с закрытием, возможно метод для цены и лотов, или через модель. так как там расчеты
        # нужны.
        if self.param['long']:
            self.sell()


if __name__ == '__main__':
    responce = view.main_action()
    a = Order('GZP')
    b = Order('APL')
    c = Order('YAN')
    all_orders = [a, b, c]
    while responce != '0':
        if responce == '1':
            order = Order(view.ticker())
            all_orders.append(order)
            if view.buy_or_sell() == '1':
                order.buy()
            else:
                order.sell()
                order.param['long'] = False
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
                all_orders[order_number].close()




        elif responce == '3':
            view.show_all(all_orders)

        responce = view.main_action()
