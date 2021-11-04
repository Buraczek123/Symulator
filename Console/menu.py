class Menu:
    menu = dict()
    def init():
        Menu("Main Menu")


    def __init__(self, name):
        self.name = name
        Menu.menu[name] = self
