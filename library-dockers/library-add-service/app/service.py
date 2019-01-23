from model import Book
from db import MongoRepository

class Library:
    def __init__(self):
        self.__repo = MongoRepository()
    
    def add(self, book):
        if book.isbn is None or book.title is None or book.price is None or book.isbn < 0 or book.price < 0:
            raise Exception("Invalid Book")

        self.__repo.add({
            "isbn": book.isbn,
            "title": book.title,
            "price": book.price 
        })