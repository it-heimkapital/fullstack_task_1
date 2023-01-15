# Heimkapital task(Django + React)

## Getting Started with Create Django Project

### Installing Django and its dependencies
```bash
# Create virtual env
python3 -m venv employee_env

# Switch to virtual employee_env
source employee_env/bin/activate

# Install Django and its dependencies
pip3 install django djangorestframework django-cors-headers

# Create Django Project
django-admin startproject backend_django

# Switch to backend_django Directory
cd backend_django

# Run following command to create a app in backend_django project
python3 manage.py startapp employee

# Create Sql scripts for models
python3 manage.py makemigrations

# Create table structures on database
python3 manage.py migrate

# Create a Admin User to handle registered apps into admin
python3 manage.py createsuperuser

# To start django project ,In the project directory, you can run:
python3 manage.py runserver

Open http://localhost:8000 to view it in the browser.
```

## Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Installing React and its dependencies
```bash

npx create-react-app frontend
cd frontend

# Install HTTP client for the browser and node.js
npm i axios

# Install bootstrap and reactstrap dependencies
npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps

# Install datepicker dependency
npm install react-datepicker --save
```

In the project directory, you can run:

### Before starting frontend server make sure backend server is running

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

