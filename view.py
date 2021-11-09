def what_action():
    res = input('What we mast to do?\n'
                '1 - new order\n'
                '2 - show all\n'
                '3 - close order\n'
                '0 - exit\n')
    return res

def buy_or_sell():
    answer = input('1 - Buy\n2 - Sell')
    if answer == '1':
        return '1'
    else: return '0'

def ticker():
    ticker = input('Ticker?:\n')
    return ticker


def price_lots():
    price = int(input('Price?:\n'))
    lots = int(input('Lots?:'))
    return [price, lots]


def print_all(items):
    for item in items:
        print(item)

def order_choise():
    o_choise = input('Select orders number:')
    return int(o_choise)


