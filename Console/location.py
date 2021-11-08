from place import Place
class Location:
    __locations = dict()

    def getLocation(name):
        return Location.__locations[name]

    def init():
        Place.init()
        # barnek village
        location = Location("BarnekVillage")
        location.setDescription("Barnek Village.\nSmall and calm place.")
        location.addPlace(Place.getPlace("Glade"))


    def __init__(self, name):
        self.__name = name
        self.__places = list()
        Location.__locations[name] = self

    def getName(self):
        return self.__name

    def setDescription(self, description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def addPlace(self, place):
        self.__places.append(place)

    def getPlaces(self):
        return self.__places
