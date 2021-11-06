from choice import Choice
from location import Location


class Menu:
    __menu = dict()
    def __quit(game):
        game.quit()

    def __play(game):
        game.createPlayer()
        game.setMenu("BarnekVillage")

    def init():
        # const choices
        quit = Choice("Exit", Menu.__quit)

        # main menu
        menu = Menu("MainMenu")
        menu.setDescription("Główne Menu Gry")
        menu.addChoice(Choice("Play", Menu.__play))
        menu.addChoice(quit)

        # Barnek Village
        menu = Menu("BarnekVillage")
        menu.setDescription("Wioska Barnek.\nMała i niczym nie wyróżniająca się.")
        menu.linkLocation("BarnekVillage")
        menu.addChoice(quit)

    def addMenu(menu):
        Menu.__menu[menu.getName()] = menu

    def getMenu(name):
        return Menu.__menu[name]

    def getMenus():
        return Menu.__menu

    def __init__(self, name):
        self.__name = name
        self.__choices = dict()
        self.__description = str()
        Menu.addMenu(self)

    def setDescription(self, description):
        self.__description = description

    def addChoice(self, choice):
        self.__choices[len(self.__choices)] = choice

    def getChoice(self, name):
        return self.__choices[name]

    def getName(self):
        return self.__name

    def display(self):
        menus = Menu.getMenus()
        print(self.__description, "\n")
        for i, choice in self.__choices.items():
            print(f"{i+1}. {self.__choices[i].getName()}")
