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
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = make_response(str(e), 400)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

app.run(host='0.0.0.0', port=8000, debug=True)
