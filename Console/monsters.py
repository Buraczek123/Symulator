from entity import Entity

class Monsters:
    __monsters = dict()

    def init():
        Monsters.addMonster(Slime)
        Monsters.addMonster(GoblinYoung)

    def getMonster(name):
        return Monsters.__monsters[name]

    def addMonster(monster):
        name = str(monster)
        name = name[name.find(".")+1:name.find("'>")]
        Monsters.__monsters[name] = monster

class Slime(Entity):
    def __init__(self):
        super().__init__("Slime", 5, 1, xp = 3)

class GoblinYoung(Entity):
    def __init__(self):
        super().__init__("Young Goblin", 10, 2, xp = 10)
