import model, view

def order_loop():
    response = view.what_action()
    while response != '0':

        if response == '1': # buy
            order = model.Order(view.ticker())
            order.buy(int(view.price()), 1)
        elif response == '2':
            view.print_info(str(order))

        response = view.what_action()




order_loop()

