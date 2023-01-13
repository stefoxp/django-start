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

## Playing with the API

in the Python shell

```sh
python manage.py shell
```

explore the database API:

```python
from polls.models import Choice, Question

Question.objects.all()

# Create a new Question

from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())

q.save()

q.id

# access model field values
q.question_text
q.pub_date

# change values
q.question_text = "What's up?"
q.save()

# display all the questions
Question.objects.all()
```

### Adding a __str__() method to both Question and Choice models

Save these changes and start a new Python interactive shell.

```python
from polls.models import Choice, Question

Question.objects.all()

Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith='What')

# question published this year
from django.utils import timezone

current_year = timezone.now().year

Question.objects.get(pub_date__year=current_year)

# request a question that doesn't exist will raise an exception
Question.objects.get(id=2)

# use a shortcut for primary-key exact lookups
Question.objects.get(pk=1)

# use the custom method
q = Question.objects.get(pk=1)
q.was_published_recently()

# display any choices from the related object set
q.choice_set.all()

# create three choices
q.choice_set.create(choice_text='Not much?', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# choice objects have API access to their related Question objects
c.question

# and vice versa
q.choice_set.all()
q.choice_set.count()

# The API automatically follows relationships as far as you need
# Use double underscores to separate relationships
Choice.objects.filter(question__pub_date__year=current_year)

# Let's delete one of the choices
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```

## The Django Admin

### Creating an admin user

```sh
python manage.py createsuperuser

Username: stefano
Email address: ...
Password: ************
Password (again): ***********

python manage.py runserver
```

open the browser and go to "/admin/":

http://localhost:8000/admin/

### Make the polls app modifiable in the admin

We need to tell the admin that Question objects have an admin interface on the polls/admin.py

## Views

A view is a type of Web page in your Django application that generally serves a specific function and has a specific template.

In our polls application, we will have the following four views:

- Question index page
- Question detail page
- Question results page
- Vote action

Each view is represented by a Python function (or method, in the case of class-based views).

Django will choose a view by examining the URL that's requested.
To get from a URL to a view, Django uses what are known as 'URLconfs'.

### Writing more views

on polls/views.py

Wire these new views into the polls.urls module by adding the path() calls.

Take a look in your browser, at /polls/34/. It'll run the detail() method and display whatever ID you provide in the URL.
Try /polls/34/results/ and /polls/34/vote/ too

### Writing views that actually do something

Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.

Here's one stab at a new index() view, which displays the latest 5 poll questions in the system, separated by comma, according to publication date.

#### Template

Let's use Django's template system to separate the design from Python by creating a template that the view can use.

First, create a directory called **templates** in your polls directory.

Within the templates directory, create another directory called **polls**, and within that create a file called **index.html**.

Let's update our index view in polls/views.py to use the template.

#### A shortcut: render()

Django provides a shortcut to load a template, fill a context and return an HttpResponse object with the result of the rendered template.

## Raising a 404 error

Let's tackle the question detail view.

The view raises the Http404 exception if a question with the requested ID doesn't exist.

### A shortcut: get_object_or_404()

There's also a get_list_or_404() function.

### Use the template system

Back to detail() view and her template.

### Removing hardcoded URLs in templates

The problem with this hardcoded, tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates.

Since you defined the name argument in the path() functions in the polls.urls module, you can remove a reliance on specific URL paths defined in your url configurations by using the {% url %} template tag.

In the polls/index.html:

```html
<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>
```

```python
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
```

## Namespacing URL names

Django differentiate the URL names between them with namespaces.
The namespaces should be added to your URLconf.

## Part 4

### Write a minimal form

Insert a form in polls/detail.html

Create a real version of the vote() in polls/views.py

Create the results() in polls/views.py

Create the template for results
