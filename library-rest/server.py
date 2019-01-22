from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from service import Library
from model import Book

app = Flask(__name__)
api = Api(app)
library = Library()

@app.route("/library/book", methods=['POST'])
def add():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('isbn')
        parser.add_argument('title')
        parser.add_argument('price')
        book = parser.parse_args()
        library.add(Book(int(book.isbn), book.title, int(book.price)))
        response = make_response(jsonify({
            "isbn": int(book.isbn),
            "title": book.title,
            "price": int(book.price)
        }))
        response.headers['Location'] = "/library/book/" + book.isbn
        return response
    except Exception as e:
        return str(e), 400

@app.route("/library/book/<int:isbn>", methods=['GET'])
def find(isbn):
    try:
        book = library.find(isbn)
        response = make_response(jsonify({
            "isbn": book.isbn,
            "title": book.title,
            "price": book.price
        }))
        return response
    except Exception as e:
        return str(e), 404

@app.route("/library/book", methods=['GET'])
def search():
        args = request.args
        title = args['title']
        books = library.search(title)
        array = []
        for book in books:
            array.append({
                "isbn": book.isbn,
                "title": book.title,
                "price": book.price
            })
        response = make_response(jsonify(array))
        return response

app.run(debug=True)
