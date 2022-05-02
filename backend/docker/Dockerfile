#syntax=docker/dockerfile:1
FROM python:3.10-bullseye

WORKDIR /app

# Install requirements
COPY requirements.txt requirements.txt
run pip3 install -r requirements.txt

# Copy app
COPY . .

# Build native code
WORKDIR /app/native
run make

# Run app
WORKDIR /app
EXPOSE 8080
CMD [ "waitress-serve", "--port=8080", "--call", "main:get_app"]
