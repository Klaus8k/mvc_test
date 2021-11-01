def what_action():
    res = input('What we mast to do?\n'
                    '1 - byu\n'
                    '2 - show all\n'
                    '0 - exit\n')
    return res

def ticker():
    ticker = input('What whe ticker?:\n')
    return ticker

def price():
    price = input('Price?:\n')
    return price

def print_info(info: str):
    print(info)