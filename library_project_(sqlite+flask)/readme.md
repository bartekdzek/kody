# Book Library Management App

This project is a simple web application for managing a book library, built using the Flask framework and SQLAlchemy. The application allows users to add, edit, view, and delete books from a database. Below are the details of the application's features:

## Application Features

1. **Viewing Books**:
   - The homepage (`/`) displays a list of all books stored in the database, sorted alphabetically by title.

2. **Adding a New Book**:
   - On the `/add` page, users can add a new book to the database by providing the book's title, author, and rating.

3. **Editing a Book's Rating**:
   - On the `/edit` page, users can update the rating of a selected book. Users choose a book to edit and then modify its rating.

4. **Deleting a Book**:
   - On the `/delete` page, users can delete a selected book from the database.

## Technologies Used

- **Python**: The programming language used to develop the application.
- **Flask**: A micro web framework that handles routing, templating, and other functionalities needed for a web application.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) used to interact with the SQLite database, where book information is stored.
- **HTML/CSS**: Used to create simple templates for the web pages.

## Project Structure

- `main.py`: The main application file that contains all the server logic, data models, and route handling functions.
- `templates/`: A directory containing HTML templates used to render web pages.
- `instance/`: Database file

## Requirements

- Python 3.12
- Flask
- Flask-SQLAlchemy

## Running the Project
The application will be accessible at http://127.0.0.1:5000/ .

