class Location:
    __locations = dict()

    def getLocation(name):
        return Location.__locations[name]

    def init():
        pass # do zainicjowania barnek village

    def __init__(self, name):
        self.__name = name
        Location.__locations[name] = self
