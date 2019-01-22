from Entry import Entry

class Category: 
    def __init__(self, name):
        self.__name = name
        self.__entries = dict()
    def getName(self): 
        return self.__name
    def addEntry(self, entry):
        self.__entries[entry.name] = entry
    def getEntries(self):
        return self.__entries