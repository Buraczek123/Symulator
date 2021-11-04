from menu import Menu
from os import system

class Main:
    def __init__(self):
        Menu.init()
        self.__activeMenu = Menu.getMenu("Main Menu")
        self.gameLoop()

    def gameLoop(self):
        while 1:
            system("cls")
            self.__activeMenu.display()
            self.getChoice()

    def getChoice(self):
        choice = int(input("\n"))
        self.__activeMenu.getChoice(choice-1).perform()

if __name__ == "__main__":
    Main()
