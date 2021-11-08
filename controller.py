import model
import view


def order_loop():
    '''Основной цикл программы.'''
    response = view.what_action()
    while response != '0':

        if response == '1':  # buy
            order = model.Order(view.in_ticker())
            order.buy(int(view.price()), 1)
        elif response == '2':
            view.print_all(model.Order.items)
        elif response == '3':
            view.print_all(model.Order.items)
            order_to_close = view.order_choise()
            print(model.select_order(order_to_close), 'to be closed!!!')

            # В этом условии надо принимать номер ордера
            # и обращаясь к модели его закрывать.
            # Надо сделать что бы в функции выбора
            # можно было и выбирать и все распечатывать.


        response = view.what_action()


order_loop()
