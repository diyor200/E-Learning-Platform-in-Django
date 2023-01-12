# Pull official base Python Docker image
FROM python:3.10.6

# Set environment variables
ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy Django project
Copy . /code/
