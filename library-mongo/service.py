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

    def find(self, isbn):
        book = self.__repo.find(isbn)
        if book is None:
            raise Exception("Book Not Found")
        return book

    def search(self, title):
        docs = self.__repo.search(title)
        books = []

        for doc in docs:
            books.append(Book(doc['isbn'], doc['title'], doc['price']))
        return books