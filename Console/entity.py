class Entity:
    def __init__(self, name, hp = 0, attack = 0):
        self.__name = name
        self.__hp = hp
        self.__attack = attack

    def getName(self):
        return self.__name
