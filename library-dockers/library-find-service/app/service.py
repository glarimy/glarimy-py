from model import Book
from db import MongoRepository

class Library:
    def __init__(self):
        self.__repo = MongoRepository()

    def find(self, isbn):
        book = self.__repo.find(isbn)
        if book is None:
            raise Exception("Book Not Found")
        return book