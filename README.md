Pricing Module
Description
The Pricing Module is a Django-based web application designed to manage pricing configurations for ride-sharing services. It allows users to define various pricing parameters such as distance base price, distance additional price, time multiplier factor, and waiting charges. The module provides an API endpoint to calculate the price based on the input parameters.

Features
Add, modify, and remove pricing configurations
Calculate price using a RESTful API
Store pricing configurations in a PostgreSQL database
Log changes made to pricing configurations along with timestamps
Enable/disable specific pricing configurations
Validate input parameters to prevent negative values and ensure data consistency
Installation
To run the Pricing Module locally, follow these steps:

Clone the repository:

bash
Copy code
git clone <repository-url>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the PostgreSQL database:

Set up a PostgreSQL database and update the DATABASES settings in settings.py with your database credentials.
Migrate database schema:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
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
Copy code
{
    "distance": 10,
    "time": 2
}
Contributors
Your Name
