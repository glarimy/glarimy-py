from Category import Category

class City: 
    def __init__(self, name):
        self.__name = name;
        self.__categories = dict()
    def getName(self):
        return self.__name
    def addCategory(self, name):
        self.__categories[name]= Category(name)
    def getCategory(self, name):
        return self.__categories[name]
    def getCategories(self):
        return list(self.__categories.keys())
    def addEntry(category, entry):
        self.__categories[category].add(entry)