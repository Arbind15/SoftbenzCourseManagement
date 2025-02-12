# Course Management Setup Guide

## Prerequisites
Ensure you have the following installed on your system:
- Python
- Git
- Virtualenv

## Cloning the Repository
```sh
git clone https://github.com/Arbind15/SoftbenzCourseManagement.git
cd CourseManagement
```

## Setting Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

## Installing Dependencies
```sh
pip install -r requirements.txt
```

## Setting Up Environment Variables
1. Create a `.env` file in the project root.
2. Add the following environment variables (modify as needed):
```
SECRET_KEY=your_secret_key
EMAIL_USER=your-email
EMAIL_PASSWORD=your-password
```

## Applying Migrations
```sh
python manage.py migrate
```

## Creating a Superuser
```sh
python manage.py createsuperuser
```

## Running the Development Server
```sh
python manage.py runserver
```

## Go to Dashboard
```sh
http://127.0.0.1:8000/
```
