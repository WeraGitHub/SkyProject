# Use an official Python runtime as a parent image
FROM python:3

# Introduce maintainer of this document
MAINTAINER Weronika "weronikalimberger@gmail.com"

# Set the working directory to /app
WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]