from service import Library
from model import Book

java = Book(123, 'Java Book', -1)
py = Book(234, 'Python Book', 200)
jee = Book(345, 'Java Book', 230)

library = Library()
print ('Adding Books')
try:
    library.add(java)
except Exception as e:
    print (e)

try:
    library.add(py)
except Exception as e:
    print (e)

try:
    library.add(jee)
except Exception as e:
    print (e)

print()

try: 
    print ('Finding book with ISBN 123')
    book = library.find(123);
    print ("Found Book: ", book)
    print()
except Exception as e:
    print (e)

try: 
    print ('Finding book with ISBN 234')
    book = library.find(234);
    print ("Found Book: ", book)
    print()
except Exception as e:
    print (e)


print ('Find books with title Java Book')
books = library.search('Java Book')
print ("Found Books: ")
for book in books:
    print(book)
print()