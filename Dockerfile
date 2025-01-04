# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=main.py

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
