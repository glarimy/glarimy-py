#py -m pip install pymongo
import pymongo

class MongoRepository:
    def __init__(self):
        self.__mongo = pymongo.MongoClient("mongodb://localhost:27017/")
        self.__db = self.__mongo['glarimy-python-ms-db']

    def getCities(self):
        return self.__db.collection_names()

    def getCategories(self, cityname):
        city = self.__db[cityname];
        return city.find().distinct('category')

    def getSections(self, cityname, categoryname):
        city = self.__db[cityname];
        return city.find({'category':categoryname}).distinct('section')    

    def getEntries(self, cityname, categoryname, sectionname):
        city = self.__db[cityname];
        return city.find({'category': categoryname, 'section':sectionname});

    def addEntry(self, cityname, entry):
        if cityname is None or len(cityname.strip()) == 0:
            raise Exception('Invalid city name')
        if entry is None or entry['category'] is None or entry['section'] is None or entry['name'] is None or entry['address'] is None:
            raise Exception('Invalid entry')
        city = self.__db[cityname];
        city.insert_one(entry)