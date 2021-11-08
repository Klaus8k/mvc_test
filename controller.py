import model
import view


def order_loop():
    response = view.what_action()
    while response != '0':

        if response == '1':  # buy
            order = model.Order(view.in_ticker())
            order.buy(int(view.in_price()), 1)
        elif response == '2':
            print_all()
        elif response == '3':
            print_all()
            close_order_num = view.order_choise()

            print(model.Order.items[close_order_num-1])
            # В этом условии надо принимать номер ордера и обращаясь к модели его закрывать.


        response = view.what_action()

def print_all():
    for item in model.Order.items:
        view.print_info(item)


order_loop()
