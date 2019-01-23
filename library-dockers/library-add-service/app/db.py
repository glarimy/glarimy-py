import pymongo
from model import Book

class MongoRepository:
    def __init__(self):
        self.__mongo = pymongo.MongoClient("mongodb://mongo:27017/")
        self.__db = self.__mongo['glarimy-library']

    def add(self, book):
        books = self.__db['books'];
        books.insert_one(book)