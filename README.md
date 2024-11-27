# APIs-Guide


```markdown
# Library Organizer API

The Library Organizer is a simple Flask-based REST API for managing a collection of books. This project demonstrates how to create an API with Flask, SQLAlchemy, and SQLite, and how to interact with it using tools like Postman. It also serves as a resource for beginners to understand the basics of RESTful APIs.

# Features

- Add new books to the database.
- Retrieve all books in the database.
- Basic routing with Flask.
- Database handling with SQLAlchemy.
- Learn how APIs work through a real-world example.

---

# What is an API?

An API (Application Programming Interface) is a set of rules that allows applications to communicate with each other. For example, when you use a weather app to check the forecast, the app uses an API to fetch the data from a server. APIs enable data exchange between different systems, allowing them to interact in a structured and secure way.

# Example: A Simple API Request
Let's say you want to check the weather for your location. You might send a request to an API that looks like this:

```

```

This request would return data like this:

```json
{
  "location": "London",
  "temperature": "18°C",
  "condition": "Cloudy"
}
```

This is a simplified example, but the idea is that the client (in this case, the weather app) makes a request to the server (the weather API) to get information.

---

## Notes on APIs

### What is REST?
REST (Representational State Transfer) is an architectural style used for designing networked applications. It relies on a stateless, client-server communication model, where the server provides resources and the client can interact with these resources using standard HTTP methods.

# Common HTTP Methods in REST APIs:
1. GET: Retrieves data from the server (e.g., retrieving a list of books).
2. POST: Sends data to the server (e.g., creating a new book entry).
3. PUT: Updates an existing resource on the server (e.g., modifying a book’s details).
4. DELETE: Deletes a resource from the server (e.g., removing a book).

# HTTP Status Codes
- 200 OK: The request was successful.
- 201 Created: A resource was successfully created (e.g., a new book).
- 400 Bad Request: The request was malformed or missing necessary data.
- 404 Not Found: The requested resource does not exist.
- 500 Internal Server Error: The server encountered an unexpected error.

# JSON (JavaScript Object Notation)
JSON is a lightweight data interchange format used in APIs. It's easy for humans to read and write, and easy for machines to parse and generate. In this project, the API uses JSON format to send and receive data about books.

# Example JSON format for a book:
```json
{
    "name": "Kafka on the Shore",
    "description": "Kafka on the Shore, a tour de force of metaphysical reality, is powered by two remarkable characters: a teenage boy, Kafka Tamura, who runs away from home either to escape a gruesome oedipal prophecy or to search for his long-missing mother and sister; and an aging simpleton called Nakata, who never recovered from a wartime affliction and now is drawn toward Kafka for reasons that, like the most basic activities of daily life",
    "pages": 600,
    "author": "Haruki Murakami"
}
```

---

# Resources for learning APIs
- REST API Crash Course (Video)](https://www.youtube.com/watch?v=qbLc5a9jdXo)
- 7 Tips for API Design (Video)](https://www.youtube.com/watch?v=_gQaygjm_hg)
- [RESTful API Design Guide](https://www.restapitutorial.com/)
- [JSON Format Documentation](https://www.json.org/json-en.html)

---

# Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/library_organizer.git
   cd library_organizer
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python run.py
   ```

---

# API Endpoints

1. Get all books 
   - URL: `/books`  
   - Method: `GET`  
   - Response:  
     ```json
     [
       {
         "id": 1,
         "name": "Book Title",
         "description": "A brief description of the book.",
         "pages": 300,
         "author": "Author Name"
       }
     ]
     ```

### 2. Add a new book 
   - URL: `/books`  
   - Method: `POST`  
   - Request body:  
     ```json
     {
       "name": "Book Title",
       "description": "A brief description of the book.",
       "pages": 300,
       "author": "Author Name"
     }
     ```
   - Response:  
     ```json
     {
       "message": "Book added successfully!"
     }
     ```

---

# Testing with Postman

1. Install Postman:
   Download and install [Postman](https://www.postman.com/).

2. Start the Flask server:
   ```bash
   python run.py
   ```

3. Set up requests in Postman:
   - Create a new `GET` request for `http://127.0.0.1:5000/books` to fetch all books.
   - Create a new `POST` request for `http://127.0.0.1:5000/books` to add a book. Include the JSON payload in the body.

---

# Improvements Made During Development

1. Migrated from using Blueprints to a single-file `routes.py` for simplicity.
2. Removed JWT for better beginner accessibility.
3. Fixed database connection issues and ensured proper table creation.
4. Enhanced error handling for common API issues.
5. Improved documentation and project structure.

---

# Learn More

Explore the concepts behind this project and get more resources:
- Flask Documentation: [Flask](https://flask.palletsprojects.com/)
- SQLAlchemy Documentation: [SQLAlchemy](https://docs.sqlalchemy.org/)
- Postman API Tool: [Postman](https://www.postman.com/)

---

# Contributing

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.  

---
```
