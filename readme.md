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

# create the polls app (in the same directory of manage.py)
python manage.py startapp polls
```

## Start app

Web path: http://localhost:8000/polls/

## settings.py - Database setup

migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables

```sh
python manage.py migrate
```

## models for the polls app

models: your database layout with additional metadata

### Question and Choice

A Question has a question and a publication date.

A Choice has two fields: the text of the choice and a vote tally.

Each Choice is associated with a Question.

### Activating models

First we need to tell our project that the polls app is installed:

- add the path of app in mysite/settings.py
- makemigrations

```sh
python manage.py makemigrations polls
```

> migrations are how Django stores changes to your models, they are files on disk

There's a command that will run the migrations for you and manage your database schema automatically: **migrate**.

First, let's see what SQL that migration would run. The **sqlmigrate** command takes migration names and returns their SQL:

```sh
python manage.py sqlmigrate polls 0001
```

> you can also run
 python manage.py check
 for to check for any problems in your project without making migrations or touching the database

Now, run migrate to create those model tables in your database:

```sh
python manage.py migrate
```

Remember the three-step guide to making model changes:

1. Change your models (in **models.py**).
2. Run **python manage.py makemigrations** to create migrations for those changes
3. Run **python manage.py migrate** to apply those changes to the database.