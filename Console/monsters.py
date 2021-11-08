from entity import Entity

class Monsters:
    __monsters = dict()

    def init():
        Monsters.addMonster(Rabbit)

    def getMonster(name):
        return Monsters.__monsters[name]

    def addMonster(monster):
        name = str(monster)
        name = name[name.find(".")+1:name.find("'>")]
        Monsters.__monsters[name] = monster


class Rabbit(Entity):
    def __init__(self):
        super().__init__("Rabbit", 6, 1)
