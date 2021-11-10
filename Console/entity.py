class Entity:
    def __init__(self, name, hp = 0, attack = 0, xp = 0):
        self.__name = name
        self.__maxHp = hp
        self.__hp = hp
        self.__attack = attack
        self.__xp = xp
        self.__nextXp = 0
        self.__level = 0

    def getName(self):
        return self.__name

    def isAlive(self):
        alive = self.__hp > 0
        if not alive:
            print(f"{self.__name} is dead.\n")
        return alive

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

    def getXp(self):
        return self.__xp

    def giveXp(self, xp):
        print(f"Received {xp} xp.")
        self.__xp += xp
        if self.__xp >= self.__nextXp:
            self.lvlUp()

    def lvlUp(self):
        print("Level UP!\n")
        self.__xp -= self.__nextXp
        self.__level += 1
        self.__nextXp = int(10*(self.__level)**1.7)
