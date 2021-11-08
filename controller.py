import model
import view


def order_loop():
    '''Основной цикл программы.'''
    response = view.what_action()
    while response != '0':

        if response == '1':  # buy
            order = model.Order(view.in_ticker())
            order.buy(int(view.in_price()), 1)
        elif response == '2':
            print_all()
        elif response == '3':
            print_all()
            order_choice()
            # В этом условии надо принимать номер ордера и обращаясь к модели его закрывать.
            # Надо сделать что бы в функции выбора можно было и выбирать и все распечатывать.


        response = view.what_action()

def order_choice():
    choose_order = model.Order.items[view.order_choise() - 1]
    print(choose_order)

def print_all():
    for item in model.Order.items:
        view.print_info(item)


order_loop()
