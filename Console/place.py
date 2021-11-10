from monsters import Monsters
from random import randint
from battle import Battle

class Place:
    __places = dict()
    SHOP = 0
    ARENA = 1
    visit = dict()

    def init():
        Monsters.init()
        Place.visit[Place.SHOP] = Place.visit_SHOP
        Place.visit[Place.ARENA] = Place.visit_ARENA
        # glade
        place = Place("Glade")
        place.addMonster(Monsters.getMonster("Slime"))
        place.addMonster(Monsters.getMonster("GoblinYoung"))

    def getPlace(name):
        return Place.__places[name]

    def visit_SHOP(place, game):
        pass

    def visit_ARENA(place, game):
        monsters = place.getMonsters()
        monster = monsters[randint(0, len(monsters)-1)]()
        game.clear()
        Battle.battle(game.getPlayer(), monster)

    def __init__(self, name):
        self.__name = name
        self.__type = Place.SHOP

        Place.__places[name] = self

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def addMonster(self, monster):
        try:
            if monster not in self.__monsters:
                self.__monsters.append(monster)
        except:
            self.__monsters = list()
            self.__type = Place.ARENA
            self.addMonster(monster)

    def getMonsters(self):
        return self.__monsters
