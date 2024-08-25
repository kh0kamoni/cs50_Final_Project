# Dining Management System

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Architecture](#architecture)
5. [Setup and Installation](#setup-and-installation)
6. [Usage Guide](#usage-guide)
    - [User Registration and Login](#user-registration-and-login)
    - [Dashboard](#dashboard)
    - [Admin Panel](#admin-panel)
    - [Dining Manager Role](#dining-manager-role)
7. [Project Demonstration](#project-demonstration)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

## Overview
The **Dining Management System** is a comprehensive web application designed to streamline the management of prepaid meals for students living in a university residence hall. The system provides a centralized platform where users can monitor their meal usage, manage their account balances, and for designated administrators and dining managers, to manage and recharge user accounts.

## Features
- **User Registration and Authentication**: Secure user registration with unique phone numbers, password protection, and authentication.
- **Personal Dashboard**: Users can view their meal status, balance, daily meal usage, and have the ability to activate or deactivate their meal status.
- **Automated Balance Deduction**: The system automatically deducts a fixed meal charge from the user's balance daily if the meal status is active.
- **Admin and Dining Manager Roles**: Specific users are granted admin or dining manager roles, providing them with additional functionalities such as recharging balances and selecting a dining manager.
- **Search and Filter Capabilities**: Admins and dining managers can search and filter users based on room number and floor, simplifying user management.
- **Responsive and Professional UI**: The system features a professional design using Bootstrap, ensuring a user-friendly interface that is responsive across devices.

## Technologies Used
- **Backend**: 
  - Flask (Python-based web framework)
  - SQLite (Lightweight relational database)
  - Flask-Login (User session management)
  - Werkzeug (Password hashing and security)
- **Frontend**: 
  - HTML5, CSS3
  - Bootstrap (Responsive design framework)
  - JavaScript (Interactive elements)
  - Jinja2 (Template engine for dynamic content rendering)
- **Deployment**: Flask development server for local testing.

## Architecture
The Dining Management System follows a Model-View-Controller (MVC) architecture:
- **Model**: Represents the database structure and business logic, managed by SQLAlchemy ORM.
- **View**: The user interface, constructed with HTML templates, CSS, and JavaScript.
- **Controller**: The Flask routes handling requests, processing data, and rendering appropriate views.

### Database Structure
The SQLite database includes the following tables:
- **Users**: Stores user information including name, phone number, room number, floor number, balance, total meals, meal status, and roles (admin, dining manager).
- **Sessions**: Tracks user login sessions.

## Setup and Installation
To set up the Dining Management System locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd dining-management-system
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the database**:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the Flask application**:
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Usage Guide

### User Registration and Login
- **Registration**: New users can sign up by providing their name, phone number, room and floor number, and password at `/register`.
- **Login**: Existing users can log in using their phone number and password at `/login`.

### Dashboard
- **User Dashboard**: Upon logging in, users are redirected to their personal dashboard where they can view and manage their meal status, balance, and meal history.

### Admin Panel
- **Recharge Users**: Admins can recharge user balances at `/admin/recharge`, with options to search users by room and floor number.
- **Select Dining Manager**: The admin can select a dining manager for the month at `/admin/select_dining_manager`.

### Dining Manager Role
- **Recharging Balances**: The selected dining manager has access to the recharge route, allowing them to manage other users' balances.

## Project Demonstration
A video walkthrough demonstrating the features of the Dining Management System is available at [this URL](https://your-video-url.com).

## Future Enhancements
Planned improvements for the Dining Management System include:
- **Email Notifications**: Notify users when their balance is low or when a meal is deducted.
- **Analytics Dashboard**: Provide admins with visual data insights on meal usage and balance trends.
- **Mobile App Integration**: Develop a mobile app version for easier access.

## Contributing
We welcome contributions from the community! If you’d like to contribute, please fork the repository, create a feature branch, and submit a pull request. Ensure your code follows the project’s coding standards and is well-documented.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any inquiries or support, please reach out to [Your Name](mailto:your-email@example.com).

