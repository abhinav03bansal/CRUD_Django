# Django CRUD API with JWT Authentication

This project implements a RESTful API for managing books and publishers with JWT authentication using Django REST Framework.

## Features

- User registration and authentication with JWT tokens
- CRUD operations for books and publishers
- Relationship between books and publishers (Many-to-One)
- Secured endpoints with JWT authentication
- Complete test coverage

## Technology Stack

- Python 3.x
- Django 4.2.7
- Django REST Framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- SQLite (default database)

## Project Structure

```
README.MD
Requirements.txt

django_crud_api/
├── manage.py
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── django_crud_api/
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-crud-api.git
   cd django-crud-api
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py makemigrations api
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the API at `http://127.0.0.1:8000/api/`

## API Endpoints

### Authentication
- `POST /api/register/`: Register a new user
- `POST /api/login/`: Login and get JWT tokens
- `POST /api/token/refresh/`: Refresh JWT token

### Books
- `GET /api/books/`: List all books
- `POST /api/books/`: Create a new book
- `GET /api/books/<id>/`: Retrieve a specific book
- `PUT /api/books/<id>/`: Update a book
- `DELETE /api/books/<id>/`: Delete a book

### Publishers
- `GET /api/publishers/`: List all publishers
- `POST /api/publishers/`: Create a new publisher
- `GET /api/publishers/<id>/`: Retrieve a specific publisher
- `PUT /api/publishers/<id>/`: Update a publisher
- `DELETE /api/publishers/<id>/`: Delete a publisher

## Authentication

The API uses JWT authentication. To access protected endpoints:

1. Register a user or login to get JWT tokens
2. Include the access token in the Authorization header:
   ```
   Authorization: Bearer <your_access_token>
   ```

## Example Usage

### Register a user
```
POST /api/register/
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword123"
}
```

### Login
```
POST /api/login/
{
  "username": "testuser",
  "password": "securepassword123"
}
```

### Create a publisher
```
POST /api/publishers/
{
  "name": "Example Publishing",
  "address": "123 Book Street, Library City"
}
```

### Create a book
```
POST /api/books/
{
  "title": "Django for Beginners",
  "author": "Jane Doe",
  "isbn": "9781234567890",
  "publication_date": "2023-01-15",
  "publisher": 1
}
```

## Testing

Run tests with:
```
python manage.py test
```

The project includes comprehensive tests for all API endpoints and authentication mechanisms.
