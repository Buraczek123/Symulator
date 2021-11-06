from menu import Menu
from os import system
from player import Player

class Main:
    def __init__(self):
        Menu.init()
        self.setMenu("MainMenu")
        self.gameLoop()

    def setMenu(self, name):
        self.__activeMenu = Menu.getMenu(name)

    def gameLoop(self):
        self.__running = True
        while self.__running:
            self.clear()
            self.__activeMenu.display()
            self.getChoice()

    def quit(self):
        self.__running = False

    def getChoice(self):
        choice = int(input("\n"))
        self.__activeMenu.getChoice(choice-1).perform(self)

    def pause(self):
        system("pause")

    def clear(self):
        system("cls")

    def createPlayer(self):
        self.clear()
        name = input("Jak chcesz sie nazywac?\n")
        self.player = Player(name)

if __name__ == "__main__":
    Main()
