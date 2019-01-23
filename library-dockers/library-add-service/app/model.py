class Book: 
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price
    
    def __str__(self):
        return ("ISBN: " + str(self.isbn) + ", Title: " + self.title + ", Price: " + str(self.price))