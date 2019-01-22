from model import Book

class Library:
    def __init__(self):
        self.__stock = dict()
    
    def add(self, book):
        if book.isbn is None or book.title is None or book.price is None or book.isbn < 0 or book.price < 0:
            raise Exception("Invalid Book")

        if book.isbn in self.__stock:
            raise Exception("Duplciate Book")

        self.__stock[book.isbn] = book

    def find(self, isbn):
        if isbn not in self.__stock:
            raise Exception("Book Not Found")
        return self.__stock[isbn]

    def search(self, title):
        books = []
        for isbn in self.__stock.keys():
            if(self.__stock[isbn].title == title):
                books.append(self.__stock[isbn])
        return books