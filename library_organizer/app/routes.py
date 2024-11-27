from flask import Flask, jsonify, request
from .models import db, Book

def register_routes(app):
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the Library Organizer API!"}), 200

    # Get all books
    @app.route("/books", methods=["GET"])
    def get_books():
        books = Book.query.all()
        book_list = [
            {
                "id": book.id,
                "name": book.name,
                "description": book.description,
                "pages": book.pages,
                "author": book.author
            }
            for book in books
        ]
        return jsonify({"books": book_list}), 200

    # Get a single book by ID
    @app.route("/books/<int:book_id>", methods=["GET"])
    def get_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"error": "Book not found"}), 404
        return jsonify(
            {
                "id": book.id,
                "name": book.name,
                "description": book.description,
                "pages": book.pages,
                "author": book.author
            }
        ), 200

    # Add a new book
    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        name = data.get("name")
        description = data.get("description")
        pages = data.get("pages")
        author = data.get("author")

        if not all([name, description, pages, author]):
            return jsonify({"error": "All fields are required"}), 400

        new_book = Book(name=name, description=description, pages=pages, author=author)
        db.session.add(new_book)
        db.session.commit()

        return jsonify({"message": "Book added successfully!", "book": {
            "id": new_book.id,
            "name": new_book.name,
            "description": new_book.description,
            "pages": new_book.pages,
            "author": new_book.author
        }}), 201

    # Update an existing book
    @app.route("/books/<int:book_id>", methods=["PUT"])
    def update_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"error": "Book not found"}), 404

        data = request.get_json()
        book.name = data.get("name", book.name)
        book.description = data.get("description", book.description)
        book.pages = data.get("pages", book.pages)
        book.author = data.get("author", book.author)

        db.session.commit()
        return jsonify({"message": "Book updated successfully!"}), 200

    # Delete a book
    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({"error": "Book not found"}), 404

        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"}), 200
