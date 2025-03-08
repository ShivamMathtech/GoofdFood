# GoodFood - Hotel Website

## Overview
GoodFood is a hotel website built using Django, leveraging the advanced template concept. The project follows a modular structure with reusable components, template inheritance, and dynamic content rendering to provide a seamless user experience.

## Features
- **Dynamic Menu System** - Display various food categories and items dynamically.
- **Template Inheritance** - Efficient template structure using base templates.
- **Authentication System** - User login, registration, and profile management.
- **Booking System** - Users can book tables online.
- **Order Management** - Place and manage food orders.
- **Admin Dashboard** - Manage menu, orders, and user data.
- **Reviews & Testimonials** - Users can leave reviews about the food and services.
- **Responsive Design** - Mobile-friendly layout with Bootstrap.

## Technologies Used
- **Backend**: Django, Django ORM, SQLite/PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Template Engine**: Django Templates with inheritance
- **Authentication**: Django Authentication System
- **Database**: SQLite (default), can be switched to PostgreSQL or MySQL

## Installation

### 1. Clone the Repository
```sh
$ git clone https://github.com/your-username/goodfood.git
$ cd goodfood
```

### 2. Create a Virtual Environment
```sh
$ python -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
$ python manage.py migrate
```

### 5. Create a Superuser
```sh
$ python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 6. Run the Development Server
```sh
$ python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

## Template Structure
- **base.html** - Main template containing navbar, footer, and common elements.
- **home.html** - Homepage extending `base.html`.
- **menu.html** - Displays menu items dynamically.
- **booking.html** - Table reservation page.
- **order.html** - User orders and cart management.
- **dashboard.html** - Admin panel for management.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

## License
This project is open-source and available under the MIT License.

---
Happy coding! 🍽️

