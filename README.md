# Basic Project to Dockerize Django Web Application for Checking Prime Numbers

## Project Overview

This is a basic web application built using Django that checks whether a given number is prime or not. The application has been Dockerized to ensure easy deployment and development, with separate Docker containers for the frontend and backend components.

### Features:
- **Frontend:** Simple UI built with HTML, CSS (Tailwind), and JavaScript to interact with the user.
- **Backend:** A Django REST framework API endpoint that accepts a number and returns whether it is prime or not.
- **Dockerization:** The project uses Docker and Docker Compose to create isolated containers for both the frontend and backend, making the application easy to deploy and manage.

## Project Structure
- **frontend/**: Contains the HTML, CSS, and JavaScript files for the frontend.
- **backend/**: Contains the Django project and application that runs the backend API.
- **docker-compose.yml**: A file that defines the services (frontend and backend), their dependencies, and network settings.
- **Dockerfiles**: Separate Dockerfiles for the frontend and backend, defining how to build and run the respective services.

## Technologies Used:
- Django (Backend)
- Django REST Framework (For API endpoints)
- JavaScript (Frontend interactivity)
- Tailwind CSS (Frontend styling)
- Docker (For containerization)
- Docker Compose (For orchestration of multiple services)
