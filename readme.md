# Django project - start

- [Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

## Environment setup

```sh
python3 -m venv env

python3 -m pip install --upgrade pip

python3 -m pip install Django

python3 -m django --version

# 3.2.16 at office

pip freeze > requirements.txt

pip install -r requirements.txt
```

## Start a Django project

```sh
django-admin startproject mysite

# test the django project
cd mysite
python manage.py runserver

```
