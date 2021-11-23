def main_action():
    responce = input('What we mast to do?\n'
                     '1 - new.\n'
                     '2 - select order\n'
                     '3 - show all\n'
                     '0 - exit\n')
    return responce


def choose_order():
    o_choise = input('2 - select order number:\n')

    return int(o_choise) - 1


def buy_or_sell():
    responce = input('1 - Buy\n'
                     '2 - Sell\n'
                     '0 - Close order!\n')
    return responce


def ticker():
    ticker = input('Ticker?:\n')
    return ticker


def price_lots():
    price = int(input('Price?:\n'))
    lots = int(input('Lots?:\n'))
    return [price, lots]


def show_all(items: list):
    for i in items:
        print(i)


def show_current(item):
    print(item)
