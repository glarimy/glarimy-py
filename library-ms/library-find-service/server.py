from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource, reqparse
from service import Library
from model import Book

app = Flask(__name__)
api = Api(app)
library = Library()

@app.route("/library/book/<int:isbn>", methods=['GET'])
def find(isbn):
    try:
        book = library.find(isbn)
        response = make_response(jsonify({
            "isbn": book.isbn,
            "title": book.title,
            "price": book.price
        }))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = make_response(str(e), 404)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

app.run(debug=True)
