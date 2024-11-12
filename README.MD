# Task Manager API

## Project Overview

The **Task Manager API** is a RESTful web service built with Flask, designed to help users manage their tasks. It supports full CRUD (Create, Read, Update, Delete) functionality, user authentication using JWT (JSON Web Tokens), and uses SQLAlchemy for database interaction. This project is ideal for those looking to integrate authentication, database management, and API creation with Flask.

## Features

- **User Authentication**: Secure JWT-based authentication to allow user-specific data access.
- **Task Management**: Add, update, delete, and list tasks.
- **User-Friendly Endpoints**: Simple, intuitive API endpoints for interacting with tasks.

## Technologies Used

- **Python 3.x**
- **Flask**: Lightweight Python web framework for building the API.
- **Flask-SQLAlchemy**: ORM for database interaction.
- **Flask-JWT-Extended**: For handling JSON Web Token authentication.
- **SQLite** (or another SQL database): For persistent data storage.

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```

### Set up a Virtual Environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

Install all necessary packages from the requirements.txt file.
```
pip install -r requirements.txt
```
### Set Up the Database

The app uses SQLite by default. If you want to use a different database (e.g., PostgreSQL), modify the configuration file accordingly.

Initialize the database with the following commands:
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
### Configure Environment Variables

Create a .env file to store your secret keys and database URI. Example:
```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DATABASE_URL=sqlite:///site.db  # Or your preferred SQL database URL
```
### Run the Application

Finally, you can start the Flask development server:
```
python run.py
```
### The app will run on http://127.0.0.1:5000/
API Endpoints

    POST /register: Register a new user.
        Request body: { "username": "testuser", "email": "test@example.com", "password": "password123" }
    POST /login: Login and get a JWT token.
        Request body: { "username": "testuser", "password": "password123" }
    GET /tasks: Retrieve all tasks (JWT token required).
        Headers: Authorization: Bearer <your_jwt_token>
    POST /tasks: Create a new task (JWT token required).
        Request body: { "title": "New Task", "description": "Task details", "priority": "High", "due_date": "YYYY-MM-DD" }
    PUT /tasks/<task_id>: Update an existing task (JWT token required).
        Request body: { "title": "Updated Task", "completed": true }
    DELETE /tasks/<task_id>: Delete a task (JWT token required).

### License
This project is licensed under the MIT License - see the LICENSE file for details.
Contribution

Feel free to fork this project and create a pull request. Contributions are welcome!