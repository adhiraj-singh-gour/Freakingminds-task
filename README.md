# Restaurant Review Platform

This is a Django-based application for reviewing restaurants. Users can sign up, log in, add restaurants, and leave reviews for restaurants. The application also provides APIs for restaurant and review data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/restaurant-review-platform.git
    ```

2. Change into the project directory:
    ```bash
    cd Freakingmind Task\project>   
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run database migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Sign up for a new account or log in if you already have one.
3. Add a new restaurant or view existing ones.
4. Leave a review for a restaurant.

## Features

- User authentication (signup, login, logout)
- Add new restaurants
- View restaurant details and reviews
- Leave reviews for restaurants
- API endpoints for restaurant and review data

## API Endpoints

- **List/Create Restaurants**: `/api/restaurants/`
    - GET: List all restaurants
    - POST: Create a new restaurant
- **List/Create Reviews**: `/api/reviews/`
    - GET: List all reviews
    - POST: Create a new review



