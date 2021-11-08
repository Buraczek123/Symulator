class Choice:
    def __init__(self, name, action, active = True):
        self.__name = name
        self.__action = action
        self.__active = active

    def getName(self):
        return self.__name

    def isActive(self):
        return self.__active

    def setActive(self, state):
        self.__active = state

    def perform(self, game):
        self.__action(game)
