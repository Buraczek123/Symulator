from entity import Entity
from os import system

class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 25, 3)
        self.lvlUp()
        self.__moves = dict()
        self.__moves[0] = self.attack

    def chooseMove(self):
        choice = int(input("Choose move:\n1. Attack\n")) - 1
        system("cls")
        return self.__moves[choice]

    def getLevel(self):
        return self.__level
