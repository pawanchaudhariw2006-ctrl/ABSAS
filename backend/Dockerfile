# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Replace your old CMD line with this exact line:
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000