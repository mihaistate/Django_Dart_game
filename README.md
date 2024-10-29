# Pokémon Help Request System

This project is a Pokémon-themed help request system built using Django for the backend and Flutter for the mobile app. The system allows users to log in and submit help requests, which are then assigned to Pokémon staff members in a round-robin manner. The Django admin site is customized to enable searching users’ requests by staff ID, Pokémon name, or user’s email.

## Features

- **Catch Pokémon**: Fetch Pokémon data from the PokeAPI and store their moves, abilities, and types.
- **Unique Staff ID**: Assign a unique modular staff ID to each Pokémon.
- **Help Requests**: Users can log in and submit help requests.
- **Round-Robin Assignment**: Help requests are allocated to Pokémon staff members in a round-robin manner.
- **Admin Search**: Search users’ requests by staff ID, Pokémon name, or user’s email in the Django admin site.


# Build the project
docker-compose up --d

# Run the backend in a separate command prompt

docker-compose up backend

# Run the frontend

cd frontend/

flutter run

# Login

admin@example.com
adminadmin

# Help request example

I need assistance with understanding the different types of Pokémon and their abilities.

I'm having trouble catching a specific Pokémon. Can you help me with strategies or tips?

It would be great to have a feature that shows the most powerful moves of each Pokémon. Can this be added?

# Apply Migrations
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

# Create a Superuser
docker-compose exec backend python manage.py createsuperuser

# Project Structure
backend: Contains the Django backend code.
myapp: Django app with models, views, serializers, and settings.
Dockerfile.backend: Dockerfile for the backend service.
requirements.txt: Python dependencies.
frontend: Contains the Flutter mobile app code.
lib: Flutter app source code.
Dockerfile.frontend: Dockerfile for the frontend service.