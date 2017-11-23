# django-1.9
Django 1.9 Bootstrap Project. It helps to quickly setup the project.

Features
* Contains all the Bootstrap and Jquery Css and Js File
* All the Media and Static Settings are add in the settings.py file
* Logging Enabled
* Default Bootstrap Index Page
* Environment Configuration With .env file
* Default Local, Staging, Production Settings File


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Python2.7
Virtualenv
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

Clone the Project Repo

```
git clone 
```

Create Virtualenv

```
virtualenv --no-site-packages venv
source venv/bin/activate
cd django-1.9
```

### Rename the Project

Find all the TODO comment in code repo

Rename ./django_bootstrap_1_9 Folder with your project name

Replace it with you project name and change environment name in (.env file)

### Setup the Project

Run Migration

```
python manage.py migrate
```

Run Server

```
python manage.py runserver
```





