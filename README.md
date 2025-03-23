# Library Management System

This project is a Library Management System built with Django, Django REST Framework, and MySQL. It provides two ways to interact with the system:

1. **REST API Endpoints:**  
   For admin operations (signup, login, and CRUD on books) and student operations (listing all books) via external API calls.

2. **Direct Web Interface (Admin Panel & Student View):**  
   A web-based interface for admins to log in and perform CRUD operations using Django forms and templates, and a simple student view to display all book records.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Direct Web Interface](#direct-web-interface)
  - [Admin Panel](#admin-panel)
  - [Student View](#student-view)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

---

## Features

- **Admin Operations:**
  - **Signup:** Create a new admin account (unique by email).
  - **Login:** Authenticate an admin via email and password.
- **Book Management (CRUD):**
  - **Create Book:** Add new book entries.
  - **Retrieve Books:** Get a list of all books.
  - **Update Book:** Edit book details.
  - **Delete Book:** Remove a book record.
- **Student View:**
  - Display all book records.
- **Authentication:**
  - REST API uses token-based authentication.
  - Direct web interface uses session-based authentication (Django login/logout).

---

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Frontend:** HTML, Bootstrap, Django Templates
- **Authentication:** Token Authentication (for API), Session Authentication (for web)

---

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SohamSawalakhe/library_management.git
   cd library_management
Create and Activate a Virtual Environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies:

If you have a requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
If not, ensure you install:

Django

djangorestframework

mysqlclient (or PyMySQL)

djangorestframework-authtoken

Configure MySQL Database:

Create a database in MySQL (e.g., library_db). Then update the library_management/settings.py file with your database credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',  # Your database name
        'USER': 'root',
        'PASSWORD': '0264',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Set Custom User Model:

In library_management/settings.py, add:

python
Copy
Edit
AUTH_USER_MODEL = 'library_app.AdminUser'
Apply Migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create a Superuser (Optional):

bash
Copy
Edit
python manage.py createsuperuser
Collect Static Files (For Production, if needed):

bash
Copy
Edit
python manage.py collectstatic
Running the Project
Start the Django development server with:

bash
Copy
Edit
python manage.py runserver
You can now access the application at: http://localhost:8000.

API Endpoints
These endpoints use token-based authentication (except for signup and listing books).

Admin API Endpoints
Signup:

URL: /api/admin/signup/

Method: POST

Payload:

json
Copy
Edit
{
  "email": "admin@example.com",
  "name": "Admin Name",
  "password": "your_password"
}
Login:

URL: /api/admin/login/

Method: POST

Payload:

json
Copy
Edit
{
  "email": "admin@example.com",
  "password": "your_password"
}
Response: Returns a token (e.g., { "token": "your_token_here" }).

Book API Endpoints
List Books:

URL: /api/books/

Method: GET

Authentication: Not required

Create Book:

URL: /api/books/create/

Method: POST

Headers:

makefile
Copy
Edit
Authorization: Token your_token_here
Payload:

json
Copy
Edit
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_date": "1925-04-10",
  "isbn": "9780743273565",
  "summary": "A classic novel set in the Jazz Age."
}
Retrieve/Update/Delete Book:

URL: /api/books/<book_id>/

Methods: GET, PUT, DELETE

Headers:

makefile
Copy
Edit
Authorization: Token your_token_here
Direct Web Interface
Admin Panel
Use the admin panel (which uses session-based authentication) to perform CRUD operations.

Admin Login:

URL: /admin-panel/login/

Description: Login using admin credentials.

Dashboard:

URL: /admin-panel/dashboard/

Description: View a list of all books with options to add, update, or delete.

Create Book:

URL: /admin-panel/books/create/

Description: Form to create a new book entry.

Update Book:

URL: /admin-panel/books/<book_id>/update/

Description: Form to update an existing book.

Delete Book:

URL: /admin-panel/books/<book_id>/delete/

Description: Confirmation page to delete a book.

Admin Logout:

URL: /admin-panel/logout/

Student View
Student Book List:

URL: /student/books/

Description: Public view to list all available books.

Testing
Using Postman
Test the API endpoints by sending requests to the URLs listed above. For protected endpoints, include the header:

makefile
Copy
Edit
Authorization: Token your_token_here
Using Django Test Suite
Run tests (if written) with:

bash
Copy
Edit
python manage.py test
Project Structure
bash
Copy
Edit
library_management/
├── library_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── library_app/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views_api.py         # REST API endpoints
│   ├── views_panel.py       # Direct web interface views
│   └── urls.py
├── templates/
│   └── library_app/
│       ├── admin/
│       │   ├── login.html
│       │   ├── dashboard.html
│       │   ├── create_book.html
│       │   ├── update_book.html
│       │   └── delete_book.html
│       └── student/
│           └── book_list.html
└── manage.py
