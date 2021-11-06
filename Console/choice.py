class Choice:
    def __init__(self, name, action):
        self.__name = name
        self.__action = action

    def getName(self):
        return self.__name

    def perform(self, game):
        self.__action(game)
