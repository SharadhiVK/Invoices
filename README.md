# Invoicing System

This is a Django-based web application for managing invoices and invoice details.

## Features

- Allows users to create, view, update, and delete invoices.
- Supports adding invoice details to each invoice.
- Provides endpoints for interacting with the application via RESTful APIs.
- Includes authentication and authorization for user management.

## Setup

1. Clone the repository:
git clone <repository-url>

2. Install dependencies:
pip install -r requirements.txt


3. Run migrations:
python manage.py migrate


4. Create a superuser (admin):
python manage.py createsuperuser


5. Start the development server:
python manage.py runserver


The application will be accessible at http://localhost:8000/.

## Usage

- Navigate to http://localhost:8000/admin/ to access the admin panel and manage users, invoices, and invoice details.
- Use the provided API endpoints to interact with the application programmatically.

## API Endpoints

- `GET /invoices/`: Retrieve a list of all invoices or create a new invoice.
- `GET /invoices/<pk>/`: Retrieve, update, or delete a specific invoice.
- `GET /invoices/details/`: Retrieve a list of all invoice details or create a new invoice detail.
- `GET /invoices/<invoice_id>/details/<pk>/`: Retrieve, update, or delete a specific invoice detail associated with an invoice.

## Authentication

- Authentication is required to access certain endpoints.
- Use the admin panel to create and manage users.
- Include the authentication token in the request headers for authenticated requests.











