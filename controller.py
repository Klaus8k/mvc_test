import model, view

def loop_start():
    start = view.ui_start()
    while start != 0:
        name = view.your_name()
        view.res(name, model.len_name(name))
        start = view.ui_start()

loop_start()

