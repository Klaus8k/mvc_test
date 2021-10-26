def ui_start():
    start = input(f'Вперед?')
    if start == 'y':
        return 1
    else: return 0

def your_name():
    name = input('Как тебя зовут?')
    return name

def res(name, count_name):
    print('Тебя зовут: ', name, ', в твоем имени: ', count_name, ' букв')

