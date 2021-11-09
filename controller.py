import model
import view

class Order():
    """Класс сделки. Со словарем атрибутов"""
    def __init__(self, ticker):
        self.ticker = ticker
        self.param = {'ticker':self.ticker,'mid':0,'lots_in':[], 'p_in':[]}


    def __str__(self):
        return self.param







if __name__ == '__main__':
    responce = view.what_action()
    Orders = []
    while responce != 0:
        if responce == '1':
            new_order = Order(view.ticker())
            if view.buy_or_sell() == '1':
                p_l = view.price_lots()
                new_order.param['p_in'].append(p_l[0])
                new_order.param['lots_in'].append(p_l[1])
                mid = model.medium(new_order.param['p_in'], new_order.param['lots_in'])
                print(mid)

                print(new_order.param)



        responce = view.what_action()
