class Entity:
    def __init__(self, name, hp = 0, attack = 0):
        self.__name = name
        self.__maxHp = hp
        self.__hp = hp
        self.__attack = attack

    def getName(self):
        return self.__name

    def isAlive(self):
        return self.__hp > 0

    def attack(self, defender):
        damage = self.__attack
        defender.receiveDamage(damage)
        if defender.getHp() < 0:
            damage -= defender.getHp()
            defender.heal(-defender.getHp())
        print(f"{self.getName()} dealt {damage} damage to {defender.getName()} ({defender.getHp()}/{defender.getMaxHp()})")

    def receiveDamage(self, damage):
        self.__hp -= damage

    def heal(self, healing):
        self.__hp += healing
        if self.__hp > self.__maxHp:
            self.__hp == self.__maxHp

    def getHp(self):
        return self.__hp

    def getMaxHp(self):
        return self.__maxHp
