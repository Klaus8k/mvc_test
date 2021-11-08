def what_action():
    res = input('What we mast to do?\n'
                '1 - byu\n'
                '2 - show all\n'
                '3 - close order\n'
                '0 - exit\n')
    return res


def in_ticker():
    ticker = input('What whe ticker?:\n')
    return ticker


def price():
    price = input('Price?:\n')
    return price


def print_all(items):
    for item in items:
        print(item)

def order_choise():
    o_choise = input('Select orders number:')
    return int(o_choise)


