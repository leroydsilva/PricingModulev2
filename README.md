# Pricing Module
## Description
The Pricing Module is a Django-based web application designed to manage pricing configurations for ride-sharing services. It allows users to define various pricing parameters such as distance base price, distance additional price, time multiplier factor, and waiting charges. The module provides an API endpoint to calculate the price based on the input parameters.

# Features
Add, modify, and remove pricing configurations
Calculate price using a RESTful API
Store pricing configurations in a PostgreSQL database
Log changes made to pricing configurations along with timestamps
Enable/disable specific pricing configurations and make sure only one configuration is enalbed at a time
Validate input parameters to prevent negative values and ensure data consistency

## Installation
To run the Pricing Module locally, follow these steps:

Clone the repository:

Copy code
```bash
git clone https://github.com/leroydsilva/PricingModulev2.git
```
Create a virtual environment for the project:

```bash
  python3 -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```bash
  source venv/bin/activate 
```
On Windows:
```bash
venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Configure the Database database:
I have used PostgresSQL, you can change you DB or use the default sqlite. please change the database in settings.py

Migrate database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```
Run the development server:

```bash
python manage.py runserver
```
Access the application at http://localhost:8000.

Usage
Django Admin
Access the Django admin interface at http://localhost:8000/admin.
Log in with your superuser credentials.
Navigate to the Pricing Configuration section to add, modify, or remove pricing configurations.
API Endpoint
Use the /calculate-price API endpoint to calculate the price.

Send a POST request with JSON payload containing distance and time parameters.

Example payload:

json
```bash
{
    "distance": 10,
    "time": 2
}
```
Contributors
Leroy Dsilva
