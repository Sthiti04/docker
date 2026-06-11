from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Sense and Sensibility",     "author": "Jane Austen"},
    {"id": 2, "title": "War and Peace",     "author": "Leo Tolstoy"},
    {"id": 3, "title": "Crime and Punishment",         "author": "Fyodor Dostoevsky"},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Books API"})

# return the list of books in JSON format
@app.route("/books")
def get_books():
    return jsonify(books)

# return the book based on the book id. Reture 404 if the book is not found
@app.route("/books/<int:book_id>")
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# 0.0.0.0 so that the flask app can listen from anywhere, not just the localhost.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)