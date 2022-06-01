# LAB - Class 33 DRF-Auth
Project: DRF-Auth \
Author: Benjamin Carter \
Links and Resources

## Setup
```
python -m venv .venv 
python .venv\Scripts\activate
pip install django
django-admin startproject ______
python manage.py migrate
python manage.py runserver
python manage.py startapp ______
python manage.py makemigrations _______
python manage.py migrate
python manage.py createsuperuser
Username: ________
password: ________
python manage.py runserver
```

## How to User
Once the docker container is created and running, create a superuser, and access the /api/token/ endpoint \
Here you will be prompted to login, use your new superuser credentials to receive a access token. /
Now change your endpoint to /api/refresh/ and enter your refresh token. You will receive an access token.


DATABASE_URL - URL to the running Postgres instance/db \
How to initialize/run your application (where applicable) \
e.g. python main.py \

How to use your library (where applicable)
## Tests 
`python manage.py test`
How do you run tests? \
python manage.py test \
Any tests of note? \
Describe any tests that you did not complete, skipped, etc