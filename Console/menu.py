from choice import Choice
from location import Location
from functools import partial
from place import Place


class Menu:
    __menu = dict()
    MENU = 0
    LOCATION = 1

    def __quit(game):
        game.quit()

    def __play(game):
        game.createPlayer()
        game.setMenu("Adventure")

    def init():
        Location.init()
        # const choices
        Menu.__QUIT = Choice("Exit", Menu.__quit)

        # main menu
        menu = Menu("MainMenu")
        menu.setDescription("Main Menu")
        menu.addChoice(Choice("Play", Menu.__play))
        menu.addChoice(Menu.__QUIT)

        # Adventure
        menu = Menu("Adventure")
        menu.linkLocation("BarnekVillage")

    def addMenu(menu):
        Menu.__menu[menu.getName()] = menu

    def getMenu(name):
        return Menu.__menu[name]

    def getMenus():
        return Menu.__menu

    def __init__(self, name):
        self.__name = name
        self.reset()
        self.__type = Menu.MENU
        Menu.addMenu(self)

    def setDescription(self, description):
        self.__description = description

    def addChoice(self, choice):
        self.__choices[len(self.__choices)] = choice

    def getChoice(self, name):
        return self.__choices[name]

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def display(self):
        print(self.__description, "\n")
        for i, choice in self.__choices.items():
            print(f"{i+1}. {self.__choices[i].getName()}")

    def reset(self):
        self.__choices = dict()
        self.__description = str()
        self.__type = Menu.MENU

    def linkLocation(self, location):
        self.reset()
        self.__type = Menu.LOCATION
        self.__location = Location.getLocation(location)
        self.setDescription("You are currently in:\n" + self.getLocation().getDescription())
        places = self.getLocation().getPlaces()
        for place in places:
            self.addChoice(Choice(place.getName(), partial(Place.visit[place.getType()], place)))


    def getLocation(self):
        return self.__location
