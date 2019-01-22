from City import City

class Directory :
    def __init__(self):
        self.__cities = dict()
    def addCity(self, name):
        self.__cities[name] = City(name)
    def addCategory(self, city, name):
        self.__cities[city].addCategory(name)
    def addEntry(self, city, category, entry):
        self.__cities[city].getCategory(category).addEntry(entry)
    def getCities(self):
        return list(self.__cities.keys())
    def getCity(self, name):
        return self.__cities[name]