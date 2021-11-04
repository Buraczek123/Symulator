from choice import Choice

class Menu:
    __menu = dict()
    def init():
        # main menu
        menu = Menu("Main Menu")
        menu.addChoice(Choice("Wyjdz", exit))

    def addMenu(menu):
        Menu.__menu[menu.getName()] = menu

    def getMenu(name):
        return Menu.__menu[name]

    def getMenus():
        return Menu.__menu

    def __init__(self, name):
        self.__name = name
        self.__choices = dict()
        Menu.addMenu(self)

    def addChoice(self, choice):
        self.__choices[len(self.__choices)] = choice

    def getChoice(self, name):
        return self.__choices[name]

    def getName(self):
        return self.__name

    def display(self):
        menus = Menu.getMenus()
        for i, choice in self.__choices.items():
            print(f"{i+1}. {self.__choices[i].getName()}")
