# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8001

# Run Django migrations (if any)
RUN python manage.py migrate

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
