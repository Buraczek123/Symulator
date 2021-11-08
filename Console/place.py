from monsters import Monsters
class Place:
    __places = dict()
    SHOP = 0
    ARENA = 1

    def init():
        Monsters.init()
        # glade
        place = Place("Glade", Place.ARENA)
        place.addMonster(Monsters.getMonster("Rabbit"))

    def getPlace(name):
        return Place.__places[name]

    def visit(place, game):
        print(f"odwiedzasz {place.getName()}")
        from os import system
        system("pause")

    def __init__(self, name, type):
        self.__name = name
        self.__type = type

        Place.__places[name] = self

    def getName(self):
        return self.__name

    def addMonster(self, monster):
        try:
            if monster not in self.__monsters:
                self.__monsters.append(monster)
        except:
            self.__monsters = list()
            self.addMonster(monster)
