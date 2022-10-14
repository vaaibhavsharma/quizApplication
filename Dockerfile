# Use Python 3.10 base image
FROM python:3.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Mounts the application `app` to the image
COPY . /app/
WORKDIR /app

EXPOSE 8080

# Allows docker to cache installed dependencies between builds
RUN pip install --no-cache-dir -r requirements.txt
