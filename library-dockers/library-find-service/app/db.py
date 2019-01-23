import pymongo
from model import Book

class MongoRepository:
    def __init__(self):
        self.__mongo = pymongo.MongoClient("mongodb://mongo:27017/")
        self.__db = self.__mongo['glarimy-library']

    def find(self, isbn):
        books = self.__db['books'];
        docs = books.find({'isbn': isbn})
        if docs.count() == 0:
            return None
        doc = docs[0]
        return Book(doc['isbn'], doc['title'], doc['price'])