# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Install CUPS development files and other required packages
RUN apt-get update && apt-get install -y libcups2-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV FLASK_APP=your_app_filename.py

# Run the Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
