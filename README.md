# Python Django

## Getting Started

### Step 1: Create a virtual environment and activate it.

> To create a virtual environment and activate it run the following command

```shell
$ pip3 install virtualenvwrapper-win

$ mkvirtualenv <name_of_the_virtual_enviroment>
```

> Note that as soon as you close the command prompt the virtual environment will be deactivated. So to activate it when you want to run the following command:

```shell
$ workon <virtual-environment-name>
```

#### Available command and their use in `virtualenvwrapper`

> Listing the virtual environments available

```shell
$ lsvirtualenv
```

> Remove the virtual environment that exists

```shell
$ rmvirtualenv <name>
```

> Activate the virtual environment

```shell
$ workon [<name>]
```

> Deactivate the virtual environment

```shell
$ deactivate
```

> To Read more about the virtualenvwrapper visit [here](https://pypi.org/project/virtualenvwrapper-win/)

### Step 2: Install Django:

> To install django run the following command.

```shell
$pip3 install django
```

### Step 3: To initiate a project in Django:

> To create a new Django project run the following command:

```shell
$ django-admin startproject <project-name>
# Example
$ django-admin startproject templates
```

### Step 4: Navigate to the project directory

> To navigate to the project directory run the following command:

```shell
$ cd <project-name>
# Example
cd templates
```

### Step 5: Running the Django server

> To run the server, you need to go to the directory containing manage.py and from there enter the command:

```shell
$python manage.py runserver
```

### Step 6: Creating a Django Application

> To create a basic app in your Django project you need to go to the directory containing manage.py and from there enter the command:

```
$ python manage.py startapp <app-name>

# Example
$ python manage.py startapp basic

```

### Step 8: Create the url for the app

In the basics folder created create the file called `basic/urls.py` and populate with the following code...

###### `urls.py`

```
from django.urls import path

from . import views

urlpatterns =[
    path('', views.main, name='main')
]

```

> Now go to the `templates/urls.py` and populate with the following code

###### `templates/urls.py`

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('basic/', include('basic.urls')),
    path('admin/', admin.site.urls),
]
```

> In the file `basic/views.py` populate with the following code:

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(req):
    return HttpResponse("<h1>Hello World</h1>")
```

#### Then:

> Start the server:

```shell
$python manage.py runserver
```

> Visit [here](http://127.0.0.1:8000/basic/) for our hello world application.

## Done with the setup.

- [Django Documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
