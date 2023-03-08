<h1>Django</h1>

<p align="center">
<img width="500" src="https://user-images.githubusercontent.com/31994778/128596682-6a292026-0904-4a72-aa73-2f3d425500b4.png">
 </p>
 
 <b><i>"Django makes it easier to build better web apps more quickly and with less code."</i></b>
 
 ---
 
<b>Table Of Contents</b> |
------------ | 
[Introduction to Django](#intro)
[Dev Env](#dev-env)
[Explaining Django Apps](#django-apps)
[Django Project Structure](#django-project-structure)
[Django App Structure](#django-app-structure)
[Writing Views](#writing-views)
[Debugging Django Applications in VsCode](#debug-in-vscode)
[Project Settings](#project-settings)
[Building A Data Model](#data-model)
[Django ORM](#orm)
[OR Queries](#or)
[AND Queries](#and)
[NOT Queries](#not)
[Django Rest Framework](#drf)
[Serializer](#serializer)
[Using Class Based Views](#class-based-view)
[Using Mixins](#mixins)
[Validators](#validators)
[Model Serializer](#model-serializer)
[Serializer Method Fields](#custom-fields)
[Relationships](#relationships)
[Select & Prefetch Related](#select-prefetch-related)
[Writing Views for StudentsDetail](#students-detail-views)
[User Model](#user-model)
[Permissions](#permissions)
[Custom Calculations](#custom-calculations)
[Authentication](#authentication)
[Unit Tests](#unit-tests)
[Running Our Tests Through VSCode](#vs-code-integration)
[Throttling](#throttling)
[Swagger](#swagger)

---

<div id="intro">
  <h2>Introduction to Django</h2>
  </div>
  
Django is a Python framework to build web apps.

<p align="center">
<img width="500" alt="Screen Shot 2021-08-07 at 1 19 06 PM" src="https://user-images.githubusercontent.com/31994778/128597061-c526344c-b8e5-4903-8d86-81f9fe23b165.png">
 </p>
 
 As you can see, it's the most popular web development framework for Python. Why? 
 
 Because Django adopts two main principles:
 
 1- <b>Less Time</b>
 
 2- <b>Less Code</b>
 
 These two are because Django already comes with lots of built in features, therefore helping developers do more with less code in less time. Due to having lots of built-in features, Django is called what's known as a "Batteries Included" framework.
 
 <h4>Companies Using Django</h4>
 
 
<p align="left">
<img width="500" alt="Screen Shot 2021-08-07 at 1 19 27 PM" src="https://user-images.githubusercontent.com/31994778/128597054-5fecc4ba-5f9e-4152-a100-a4b03225d48b.png">
 </p>
 
 <h4>Django Features</h4>
  
<p align="left">
<img width="500" alt="Screen Shot 2021-08-07 at 1 25 19 PM" src="https://user-images.githubusercontent.com/31994778/128597112-9e8d3b89-cf4f-4118-8b80-4320738269cc.png">
 </p>

<h4>Django Alternatives</h4>

<p align="left">
<img width="500" alt="Screen Shot 2021-08-07 at 1 32 26 PM" src="https://user-images.githubusercontent.com/31994778/128597288-7eb47c5e-d9ea-442e-8e3f-f50e3a5281b5.png">
 </p>
 
---

<div id="dev-env">
<h2>Setting Up the Development Environment</h2>
</div>

On my desktop

```
burakhanaksoy@Burakhans-MacBook-Pro ~/Desktop
$ mkdir Django_Project
burakhanaksoy@Burakhans-MacBook-Pro ~/Desktop/Django_Project
$ python3 -m venv django_env
burakhanaksoy@Burakhans-MacBook-Pro ~/Desktop/Django_Project
$ source django_env/bin/activate
(django_env) burakhanaksoy@Burakhans-MacBook-Pro ~/Desktop/Django_Project
$ pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/d5/9b/3514fae1e9d0c71044739dca5ed55f50443bd1309548b63603712365e6e9/Django-3.2.6-py3-none-any.whl (7.9MB)
     |████████████████████████████████| 7.9MB 528kB/s 
Collecting asgiref<4,>=3.3.2 (from django)
  Downloading https://files.pythonhosted.org/packages/fe/66/577f32b54c50dcd8dec38447258e82ed327ecb86820d67ae7b3dea784f13/asgiref-3.4.1-py3-none-any.whl
Collecting pytz (from django)
```

Now, I have my virtual env ready and django installed.

<p align="left">
<img width="500" alt="Screen Shot 2021-08-07 at 1 55 18 PM" src="https://user-images.githubusercontent.com/31994778/128597868-272805d9-5a55-45cc-b3ca-6ff674f1b6bf.png">

 </p>

To start the first Django project, we need to run `django-admin startproject <Project Name>`

Having done so, we get

<p align="left">
<img width="500" alt="Screen Shot 2021-08-07 at 1 58 27 PM" src="https://user-images.githubusercontent.com/31994778/128597943-e7e79f07-9293-4ec5-8484-e12e27dca771.png">
 </p>
 
 <h3>Getting Rid of Redundant Folders</h3>
 
 <p align="center">
<img width="368" alt="Screen Shot 2021-08-07 at 2 01 31 PM" src="https://user-images.githubusercontent.com/31994778/128598039-82e51b0a-d0ad-45e7-9924-3307b1270afb.png">
 </p>
 
 here, we have two `my_first_django_project` folder. Having two is redundant. So, let's reduce it to one by
 
 `django-admin startproject my_first_django_project .`
 
 the dot at the end tells django to use current directory.
 
 Having done that, we now have only one folder..
 
  <p align="center">
<img width="365" alt="Screen Shot 2021-08-07 at 2 04 03 PM" src="https://user-images.githubusercontent.com/31994778/128598058-18449368-e5e1-461b-adf9-43c2268a6f20.png">
 </p>
 
 ---
 
 <div id="django-apps">
 <h2>Explaining Django Apps</h2>
 </div>
 
   <p align="center">
<img width="367" alt="Screen Shot 2021-08-07 at 2 17 45 PM" src="https://user-images.githubusercontent.com/31994778/128598574-3e51f38f-10c5-46ab-8c4b-86db0caa9798.png">

 </p>
 
 By default, Django has 6 built-in apps.
 
 ```
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

<b>django.contrib.admin</b>: This app is used for providing the user with an admin interface for managing the web app.

<b>django.contrib.auth</b>: This app is used for authenticating users.

<b>django.contrib.contenttypes</b>: This app is used for tracking models in the project, providing the user with an interface to work with the models.

<b>django.contrib.sessions</b>: This app is not used anymore. It's legacy. We can delete it.

<b>django.contrib.messages</b>: This app is used for displaying one-time notifications to the user.

<b>django.contrib.staticfiles</b>: This app is used for serving static files, like images, css files and so on.
 
 ---
 
 <div id="django-project-structure">
 <h2>Django Project Structure</h2>
 </div>
 
 ```
$ tree /Users/burakhanaksoy/Desktop/Django_Project/my_first_django_project/
/Users/burakhanaksoy/Desktop/Django_Project/my_first_django_project/
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   ├── settings.cpython-38.pyc
│   ├── urls.cpython-38.pyc
│   └── wsgi.cpython-38.pyc
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

 <h3>manage.py</h3>
 
This file is used as a wrapper for django-admin command. 

When we run `python manage.py` on our terminal, we can see the available options.

```
$ python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```
 
 As we can see, the options available for django-admin is also available for manage.py, such as `startapp` and `startproject`.
 
 This command is used for starting, debugging, deploying, making migrations and more.
 
 -> <b>runserver</b>: This command is used to run the server for our web application.
 
 -> <b>migrate</b>: This is used for applying the changes done to our models into the database. That is if we make any changes to our database then we use migrate command. This is used the first time we create a database.
 
 -> <b>makemigrations</b>: this is done to apply new migrations that have been carried out due to the changes in the database.
 
 ---
 
  <h3>__init__.py</h3>
  
  This is to tell Python that this folder is a Python package.
  
  <h3>settings.py</h3>
  
  This file contains our Installed Apps, Middleware Apps, settings about our project and so on. A very important file, indeed. The one we'll be changing later on.
  
  <h3>urls.py</h3>
  
  This file handles all the URLs of our web application. This file has the lists of all the endpoints that we will have for our website.
  
   <p align="center">
<img width="500" alt="Screen Shot 2021-08-07 at 2 46 32 PM" src="https://user-images.githubusercontent.com/31994778/128599057-012f9264-82ef-4c95-be7d-cbcc68676607.png">
</p>

The more urls we need, the more urls we add to urls.py.

---

<h3>wsgi.py</h3>

This file mainly concerns with the WSGI server and is used for deploying our applications on to servers like Apache etc.

WSGI, short for Web Server Gateway Interface can be thought of as a specification that describes how the servers interact with web applications.

Again we won’t be doing any changes to this file.

<h3>asgi.py</h3>

In the newer versions of Django, you will also find a file named as asgi.py apart from wsgi.py. ASGI can be considered as a succeeder interface to the WSGI.

ASGI, short for Asynchronous Server Gateway interface also has the work similar to WSGI but this is better than the previous one as it gives better freedom in Django development. That’s why WSGI is now being increasingly replaced by ASGI.

Again we won’t be doing any changes to this file.

---

<div id="django-app-structure">
<h2>Django App Structure</h2>
  </div>
  
As we have illustrated above, Django is comprised of many apps. Each built-in apps provide a certain functionality. We can also create our own apps.

So let's take a look at the file structure when we create our own app..

```
(django_env) burakhanaksoy@Burakhans-MacBook-Pro ~/Desktop/Django_Project
$ python manage.py startapp my_demo_app
```

```
my_demo_app
|
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

<h3>__init__.py:</h3> As we have said before, this is for Python to recognize this directory as a Python package.

<h3>admin.py:</h3> As the name suggests, this file is used for registering the models into the Django administration.

The models that are present have a superuser/admin who can control the information that is being stored.

   <p align="center">
<img width="500" alt="Screen Shot 2021-08-07 at 3 20 34 PM" src="https://user-images.githubusercontent.com/31994778/128599937-36c91238-d3d7-403c-9b20-1aff42545020.png">
</p>

<h3>apps.py:</h3> This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases and hence we won’t be doing anything here in the beginning.

   <p align="center">
<img width="552" alt="Screen Shot 2021-08-07 at 3 24 00 PM" src="https://user-images.githubusercontent.com/31994778/128600012-7d9199c1-2add-4eaf-9ed6-63bcf3231cec.png">
</p>

<h3>models.py:</h3> This file contains the models of our web applications (usually as classes).

Models are basically the blueprints of the database we are using and hence contain the information regarding attributes and the fields etc of the database.

<h3>views.py:</h3> This file is a crucial one, it contains all the Views(usually as classes). Views.py can be considered as a file that interacts with the client. Views in Django can be named as "request handler" since the request is routed to this module after being handled in the urls.py.

Everytime you create an app, you have to write append it on `INSTALLED_APPS` in settings.py such as

```
INSTALLED_APPS = [
   ...,
   ...,
   ...,
   ...,
   ...,
   ...,
    'my_demo_app'
]
```

<h3>urls.py:</h3> Just like the project urls.py file, this file handles all the URLs of our web application. This file is just to link the Views in the app with the host web URL. The settings urls.py has the endpoints corresponding to the Views.

<h3>tests.py:</h3> This file contains the code that contains different test cases for the application. It is used to test the working of the application.

---

<div id="writing-views">
 <h2>Writing Views</h2>
 </div>
 
 As we said before, Django views are `Request Handlers`. This is to say that they receive HTTP Requests and they can do such things as follows:
 
 1- Relaying the request to another service
 
 2- Making some logical operation on the request and send as response back to the sender
 
 3- Taking the response from another service and relaying it to the sender
 
 It is important to see that Views receive <b>HTTP requests</b> and respond with <b>HTTP Responses</b>.
 
 This can be visualized as follows:
 
 <p align="center">
 <img width="500" alt="Screen Shot 2021-08-07 at 5 37 03 PM" src="https://user-images.githubusercontent.com/31994778/128603754-6ed7be0b-fab0-4096-97a0-229d81e82ffb.png">
 </p>
 
 Now, I am in views.py.
 
 ```py
from django.http import HttpResponse
from django.http import JsonResponse


def demo_api(request):
    data = JsonResponse({
        'status': 200,
        'msg': 'django is awesome!'
    })

    return HttpResponse(data, status=200)
```

Now I'm in urls.py (From app)

```py
from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo_api)
]
```

Now I'm in urls.py (From project)

```py

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_demo_app.urls'))
]
```

Now I'm in views.py (From app)

```py
from django.http import HttpResponse
from django.http import JsonResponse


def demo_api(request):
    data = JsonResponse({
        'status': 200,
        'msg': 'django is awesome!'
    })

    return HttpResponse(data, status=200)
```

I added `demo/` endpoint <b>This is very important since we did a request mapping to an endpoint here</b>, and defined `demo_api(request)` method.

<p align="center">
<img width="500" alt="Screen Shot 2021-08-07 at 6 14 54 PM" src="https://user-images.githubusercontent.com/31994778/128604980-73114b4e-4487-454b-bc94-d968af3c6aef.png">
 </p>
 
 <b>Note that each views method should take `request` as positional argument.</b>
 
 ---
 
 <div id="debug-in-vscode">
 <h2>Debugging Django Applications in VsCode</h2>
 </div>
 
 <h3>Creating launch.json For Debugging</h3>
 
 We need a launch.json so that VSCode can use it to run django server.
 
 ```
 {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "8081"
            ],
            "django": true
        }
    ]
}
```

I want to put a breakpoint on my view so that whenever I send a request to that endpoint, it stops at the view and I can analyze it line by line.

<p align="center">
 <img width="500" alt="Screen Shot 2021-08-07 at 6 48 54 PM" src="https://user-images.githubusercontent.com/31994778/128605948-310f1eab-ded5-4997-b680-ab7903e3d4c4.png">
 </p>
 
 Then, click start button
 
 <p align="center">
 <img width="418" alt="Screen Shot 2021-08-07 at 6 50 06 PM" src="https://user-images.githubusercontent.com/31994778/128605975-b0c8e87a-c1a6-4084-bede-e9620c3f8d70.png">
 </p>
 
 Then, send a request, and boom!
 
 We hit the endpoint!

<p align="center">
 <img width="600" alt="Screen Shot 2021-08-07 at 6 51 47 PM" src="https://user-images.githubusercontent.com/31994778/128606002-527e7f61-ff35-4c08-908f-30626785cf3e.png">
</p>

---

<div id="data-model">
 <h2>Building A Data Model</h2>
 </div>
 
 <h3>Introduction to Data Modeling</h3>
 
 Django applications contain a models.py file where data models are defined. 
 
 Each data model is mapped to a database table. To complete the project setup, you need to create the tables associated with the models of the applications listed in INSTALLED_APPS. Django includes a migration system that manages this.
 
 
---

<div id="project-settings">
<h2>Project Settings</h2>
 </div>
 
 Under settings.py, there are some very important things that worth explaining.
 
 <h3>DEBUG</h3>
 
 Debug mode is a boolean that turns on and off. By default, it is True. In development, it can stay this way but in production it must be false since it would disclose sensitive information, such as passwords.
 
 When Debug mode is True, Django will display uncaught exceptions that are thrown by the application.
 
 <h3>ALLOWED_HOSTS</h3>
 
 This setting is not important when run in Debug mode is True or doing tests. It becomes important when on production. 
 
 Once you move your site to production and set DEBUG to False, you will have to add your domain/host to this setting in order to allow it to serve your Django site.
 
 <h3>ROOT_URLCONF</h3>
 
 Indicates the Python module where the Root URL Configurations are defined for your project.
 
 <h3>INSTALLED_APPS</h3>
 
 Let's just put it with an image
 
 <p align="center">
 <img width="500" alt="Screen Shot 2021-08-07 at 10 03 17 PM" src="https://user-images.githubusercontent.com/31994778/128611251-e43bf4a2-d4b7-49e0-a54c-6b8fe250de7e.png">
 </p>
 
 <h3>DATABASES</h3>
 
 A dictionary that contains the setting for all databases that are going to be used in the project.
 
 There must be a default database.
 
 The default configuration uses SQLite3 database.
 
 <h3>LANGUAGE_CODE</h3>
 
 defines the default language code for this Django site.
 
 <h3>USE_TZ</h3>
 
Tells Django to activate/deactivate timezone support. Django comes with support for timezone-aware datetime. This setting is set to True when you create a new project using the startproject management command.

---

<div id="orm">
 <h2>Django ORM</h2>
 </div>
 
 <b><i>"ORM stands for Object Relational Mapping, which is used to map database queries written in a native programming language to SQL."</i></b>
 
 Providing an ORM, Django keeps it's promise... <b><i>"Less code, less time.</i></b>
 
 Let's illustrate what would happen if we didn't use ORM.
 
 <p align="center">
<img height="350" src="https://user-images.githubusercontent.com/31994778/128629773-e5c9c67b-2234-40d2-8664-8b6457b3c687.png">
 </p>
 
 As you can see, that would be more time consuming and more complex.
 
 <h3>Why ORM?</h3>
 
 - Writing in a native programming language
 
 - Easily switching between SQL Databases. (MySQL, PostgreSQL, Oracle)

 - Ease of use

 - Less time consuming

SQLAlchemy is also an ORM.

 <p align="center">
<img width="500" alt="Screen Shot 2021-08-08 at 3 03 09 PM" src="https://user-images.githubusercontent.com/31994778/128631321-af18422d-9f6d-4761-ba79-30ec33d8178c.png">
 </p>
 
 To be more accurate, we need a driver for relaying ORM request to DB. For example, psycopg2 is a driver for PostgreSQL DB.
 
 <p align="center">
 <img width="412" alt="Screen Shot 2021-08-08 at 3 14 18 PM" src="https://user-images.githubusercontent.com/31994778/128631714-5ea931bf-afb8-4318-b4d3-be523e27398d.png">
 </p>
 
---

<h3>A Simple Demo</h3>

I'm inside models.py from the application my_demo_app.

```py
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
```

added `'my_demo_app.apps.MyDemoAppConfig',` to `INSTALLED_APPS` under settings.py

```
$ python manage.py makemigrations my_demo_app
Migrations for 'my_demo_app':
  my_demo_app/migrations/0001_initial.py
    - Create model Student
    - Create model Teacher
```

Django created `0001_initial.py` file under migrations/ directory.

```
$ python manage.py sqlmigrate my_demo_app 0001
BEGIN;
--
-- Create model Student
--
CREATE TABLE "my_demo_app_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(100) NOT NULL, "last_name" varchar(100) NOT NULL, "age" integer NOT NULL, "teacher" varchar(100) NOT NULL);
--
-- Create model Teacher
--
CREATE TABLE "my_demo_app_teacher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(100) NOT NULL, "last_name" varchar(100) NOT NULL);
COMMIT;
```

Let's sync your database with the new model. Run the following command to apply existing migrations:

```py
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, my_demo_app, sessions
Running migrations:
  Applying my_demo_app.0001_initial... OK
  ```
  
  Let's add your models to the administration site. Edit the admin.py file of the my_demo_app application and make it look like this:
  
  ```
from django.contrib import admin
from.models import Student, Teacher
admin.site.register(Student)
admin.site.register(Teacher)
```

<p align="center">
 <img width="500" alt="Screen Shot 2021-08-08 at 3 59 54 PM" src="https://user-images.githubusercontent.com/31994778/128632761-042c3bf3-b1db-43d4-a4d4-5ccdfc830486.png">
 </p>
 
 Here, you can see that our app and it's models are successfully displayed on the admin site.
 
 Then, inside views.py
 
 ```py
 from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student


def get_students(request):
    data = {}

    students = Student.objects.all()
    if students:
        for no, student in enumerate(students):
            data[f'student{no + 1}'] = {'name': student.first_name,
                                        'last_name': student.last_name,
                                        'age': student.age
                                        }

    data = JsonResponse(data)

    return HttpResponse(data, status=200)
```

and

<p align="center">
 <img width="500" alt="Screen Shot 2021-08-08 at 4 53 56 PM" src="https://user-images.githubusercontent.com/31994778/128634498-cd9cec72-c23f-40ed-8b6d-281add6df6e7.png">
 </p>

To find out what the related SQL query for this operation is, we can run `print(students.query)`

```
SELECT "my_demo_app_student"."id", "my_demo_app_student"."first_name", "my_demo_app_student"."last_name", "my_demo_app_student"."age", "my_demo_app_student"."teacher" FROM "my_demo_app_student"
```

---

<div id="or">
<h3>OR Queries</h3>
 </div>
 
 Let's find students whose teacher is A or B.
 
 Run `python manage.py shell`
 
 ```py
>>> from django.db.models import Q
>>> from my_demo_app.models import Student
>>> 
>>> students = Student.objects.filter(Q(teacher="Ahmet") | Q(age= 21))
>>> students
<QuerySet [<Student: Burakhan>, <Student: Nigar>]>
>>> 
```

As you can see, we filtered students whose teacher is "Ahmet" <b>OR</b> whose age is 21.

---

<div id="and">
<h3>AND Queries</h3>
 </div>

Returns queries where each condition is met.

Example

```py
def get_students(request):
    data = {}

    students = Student.objects.filter(Q(teacher="Ahmet") & Q(age= 26))
    if students:
        for no, student in enumerate(students):
            data[f'student{no + 1}'] = {'name': student.first_name,
                                        'last_name': student.last_name,
                                        'age': student.age,
                                        'teacher': student.teacher
                                        }

    data = JsonResponse(data)

    return HttpResponse(data, status=200)
```
    
This is the corresponding SQL query
    
```SQL
SELECT "my_demo_app_student"."id", "my_demo_app_student"."first_name", "my_demo_app_student"."last_name", "my_demo_app_student"."age", "my_demo_app_student"."teacher" FROM "my_demo_app_student" WHERE ("my_demo_app_student"."teacher" = Ahmet AND "my_demo_app_student"."age" = 26)
```

<p align="center">
 <img width="500" alt="Screen Shot 2021-08-12 at 10 08 37 AM" src="https://user-images.githubusercontent.com/31994778/129153189-9f1556a9-b902-491a-b212-848adfb7df7c.png">
 </p>
 
 ---
 
 <div id="not">
 <h2>NOT Queries</h2>
 </div>
 
 `~` character is used to denote NOT.
 
 ```py
>>> from django.db.models import Q
>>> from my_demo_app.models import Student
>>> 
>>> 
>>> students = Student.objects.filter(~Q(age=26) & ~Q(age=21)).values_list()
>>> 
>>> students
<QuerySet []>
```

```py
>>> from django.db.models import Q
>>> from my_demo_app.models import Student
>>> 
>>> 
>>> students = Student.objects.filter(~Q(age=26)).values_list() >>> students
<QuerySet [(2, 'Nigar', 'Yerebakan', 21, 'Mehmet')]>
```

```py
>>> print(students.query)
SELECT "my_demo_app_student"."id", "my_demo_app_student"."first_name", "my_demo_app_student"."last_name", "my_demo_app_student"."age", "my_demo_app_student"."teacher" FROM "my_demo_app_student" WHERE NOT ("my_demo_app_student"."age" = 26)
```

---

<div id="drf">
 <h2>Django Rest Framework</h2>
 </div>
 
 <p align="center">
<img width="500" src="https://user-images.githubusercontent.com/31994778/129248854-38612797-1087-41e6-afb1-b2bd30f7af30.png">
 </p>

<h3>Why DRF?</h3>

We choose DRF for many reasons:

- <b>Serialization</b>: DRF supports serialization and deserialization. Remember we had to convert our student objects to Python dictionaries every time we queried them. With DRF, we won't have to.

<p align="center">
 <img width="550" alt="Screen Shot 2021-08-12 at 9 35 46 PM" src="https://user-images.githubusercontent.com/31994778/129250430-d90ced47-7bbe-4b14-be73-a71a25180d68.png">
 </p>
 
 We will also use DRF serializers for data validation. This is a very important usage of serializers.
 
 - Web Browsable API interface.

<p align="center">
 <img width="550" alt="Screen Shot 2021-08-12 at 9 39 37 PM" src="https://user-images.githubusercontent.com/31994778/129250922-c9822c22-204b-4810-8dd6-dd6057160cfa.png">
 </p>
 
 This is good for both testing and documentation.
 
 - Authentication with OAuth1 and OAuth2 support.

---

<div id="serializer">
<h2>Serializer</h2>
 </div>
 
 We use serializers to make data validation and serializing - deserializing objects.
 
 For example, remember we had a code where we get students from db
 
 ```py
 # if students:
    #     for no, student in enumerate(students):
    #         data[f'student{no + 1}'] = {'name': student.first_name,
    #                                     'last_name': student.last_name,
    #                                     'age': student.age,
    #                                     'teacher': student.teacher
    #                                     }
```

This was the part where we manually serialize each student object.

Let's declare a StudentSerializer

```py
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    teacher = serializers.CharField(max_length=100)
```

Go back to views and

```py
from .serializer_file import StudentSerializer

def get_students(request):
    data = {}
    data_list = []
    students = Student.objects.all()
    
    for student in students.values():
        data = StudentSerializer(student).data
        data_list.append(data)

    result = dict()
    result['result'] = data_list

    return JsonResponse(result, status=200)
```

As you can see, we use StudentSerializer to serialize each student object coming from the db. This is a major advantageous compared to manual serializing in

- Almost eliminating wrong serialization deserialization.

- Data validation

- Better looking, clearer code

```py
>>> from my_demo_app.serializer_file import StudentSerializer
>>> from my_demo_app.models import Student
>>> 
>>> students = Student.objects.all()
>>> data_list = list()
>>> for student in students.values():
...         data = StudentSerializer(student).data
...         data_list.append(data)
... 
>>> data_list
[{'first_name': 'Burakhan', 'last_name': 'Aksoy', 'age': 26, 'teacher': 'Ahmet'}, {'first_name': 'Nigar', 'last_name': 'Yerebakan', 'age': 21, 'teacher': 'Mehmet'}]
```

This is what a serialized object looks like...

```py
>>> print(type(data))
<class 'rest_framework.utils.serializer_helpers.ReturnDict'>
```

---

<h3>Many=True</h3>

In fact, for queries like `SomeModel.objects.all()`, we don't have to iterate through every data for serialization.

```py
>>> students = Student.objects.all()
>>> 
>>> for student in students.values():
...         data = StudentSerializer(student).data
...         data_list.append(data)
```

This is not a good practice.

Instead,

```py
>>> students = Student.objects.all()
>>> data = StudentSerializer(students, many=True).data
>>> 
>>> data
[OrderedDict([('first_name', 'Burakhan'), ('last_name', 'Aksoy'), ('age', 26), ('teacher', 'Ahmet')]), OrderedDict([('first_name', 'Nigar'), ('last_name', 'Yerebakan'), ('age', 21), ('teacher', 'Mehmet')])]
```

<b>For short, queries returning multiple objects should contain many=True in the serializer.</b>

---

<h3>Creating Serializer Class</h3>

Let's talk about how to create a serializer class along with `create()` and `update()` methods.

Up to now, we only GET data from our db, so using only fields in our serializer class was enough.

But now, time has come to introduce `create()` and `update()` methods being used for `POST` and `PUT` verbs.

```py
def create(self, validated_data):
        """
        Create and return a new `Teacher` instance, given the validated data.
        """
        return Teacher.objects.create(**validated_data)
```

This is used as we use `POST` request and send data to be persisted.

```py
def update(self, instance, validated_data):
        """
        Update and return an existing `Teacher` instance, given the validated data.
        """
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
```

This is used as we use `PUT` request and send data to be either persisted or updated.

---

<h3>Handling POST Method</h3>

```py
@api_view(['GET', 'POST'])
def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
        result = dict()
        result['result'] = data
        return Response(result, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_201_CREATED)
```

Here, we have handled both `GET` and `POST` methods.

Note that when .save() of serializer is called, it calls .create() method.

---

<h3>Serializer Errors</h3>

If serializer is not valid, we can Log an error message, or print it out.

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
ERROR: Returned 500
{'age': [ErrorDetail(string='This field is required.', code='required')]}
```

To do this, we need to use `serializer.errors`

```py
@api_view(['GET', 'POST'])
def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
        result = dict()
        result['result'] = data

        return Response(result, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.error(f"ERROR: Returned 201")
            logging.error(f'{request.data} created')
            return Response(None, status=status.HTTP_201_CREATED)
        else:

            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)
```

<h3>Field-level Validation</h3>

Although we say that student model has first_name, last_name as charField, we didn't make a validation.

For example, a student name and last_name cannot have `!@#$%^&*()_+=` special characters, we should validate this.

To do this, we use field validation.

```py
class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    teacher = serializers.CharField(max_length=100, required=False)

    def validate(self, attrs):
        special_chars = r"\/.,';:!@#$%^&*()_+=-÷≥≤æ…ßå∂≈ç∫´∑åƒ®´˙~`*•"
        for value in [str(i) for i in attrs.values()]:
            if any(char in special_chars for char in value):
                raise ValidationError('Special character found in a field.')
        return attrs
```

```
ERROR: Returned 500
{'non_field_errors': [ErrorDetail(string='Special character found in a field.', code='invalid')]}
```

We can also add another validation here, for example age should be 0< age <100.

```py
def validate(self, attrs):
        special_chars = r"\/.,';:!@#$%^&*()_+=-÷≥≤æ…ßå∂≈ç∫´∑åƒ®´˙~`*•"
        for value in [str(i) for i in attrs.values()]:
            if any(char in special_chars for char in value):
                raise ValidationError('Special character found in a field.')

        age = attrs.get('age')

        if not (age < 100 and age > 18):
            raise ValidationError('Age should be between 0-100.')
        return attrs
```

```
ERROR: Returned 500
{'non_field_errors': [ErrorDetail(string='Age should be between 0-100.', code='invalid')]}
```

Let me show you the directory map...

```
/Users/burakhanaksoy/Desktop/Django_Project/api
├── __pycache__
│   ├── serializer_functions.cpython-38.pyc
│   ├── serializers.cpython-38.pyc
│   ├── urls.cpython-38.pyc
│   └── views.cpython-38.pyc
├── serializer_functions.py
├── serializers.py
├── urls.py
└── views.py
```

```
/Users/burakhanaksoy/Desktop/Django_Project/classroom_app
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   ├── admin.cpython-38.pyc
│   ├── apps.cpython-38.pyc
│   ├── models.cpython-38.pyc
│   ├── serializer_file.cpython-38.pyc
│   ├── serializers.cpython-38.pyc
│   ├── urls.cpython-38.pyc
│   └── views.cpython-38.pyc
├── admin.py
├── apps.py
├── migrations
│   ├── 0001_initial.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-38.pyc
│       ├── 0002_remove_teacher_email.cpython-38.pyc
│       ├── 0003_teacher_email.cpython-38.pyc
│       └── __init__.cpython-38.pyc
├── models.py
└── tests.py
```

---

<h3>PUT & PATCH</h3>

```py
@api_view(['GET', 'PUT', 'PATCH'])
def get_student(request, pk=None):
    if request.method == 'GET':
        data = {}
        data_list = []
        if not pk:
            student = Student.objects.all()
        else:
            student = Student.objects.filter(Q(pk=pk))

        if student:
            data = StudentSerializer(student.values()[0]).data
        else:
            data = {}
        data_list.append(data)

        result = dict()
        result['result'] = data_list

        return Response(result, status=200)

    if request.method == 'PUT':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)

    if request.method == 'PATCH':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH'])
def get_teacher(request, pk=None):

    if request.method == 'GET':
        data = {}
        data_list = []
        if not pk:
            teacher = Teacher.objects.all()
        else:
            teacher = Teacher.objects.filter(Q(pk=pk))

        if teacher:
            data = TeacherSerializer(teacher.values()[0]).data
        else:
            data = {}
        data_list.append(data)

        result = dict()
        result['result'] = data_list

        return Response(result, status=200)

    if request.method == 'PUT':
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)

    if request.method == 'PATCH':
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)
```

```
INFO: Patched successfully
INFO: <QueryDict: {'first_name': ['Nigarrr'], 'last_name': ['NoLastName'], 'age': ['22'], 'teacher': ['Abuzer']}> updated
```

---

<h3>DELETE</h3>

```
INFO: Deleted successfully
INFO: Burakhan deleted
```

```py
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_student(request, pk=None):
    if request.method == 'GET':
        data = {}
        data_list = []
        if not pk:
            student = Student.objects.all()
        else:
            student = Student.objects.filter(Q(pk=pk))

        if student:
            data = StudentSerializer(student.values()[0]).data
        else:
            data = {}
        data_list.append(data)

        result = dict()
        result['result'] = data_list

        return Response(result, status=200)

    if request.method == 'PUT':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)

    if request.method == 'PATCH':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)

    if request.method == 'DELETE':
        student = Student.objects.get(pk=pk)
        student.delete()
        logging.info(f"INFO: Deleted successfully")
        logging.info(f'INFO: {student} deleted')
        return Response(None, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_teacher(request, pk=None):

    if request.method == 'GET':
        data = {}
        data_list = []
        if not pk:
            teacher = Teacher.objects.all()
        else:
            teacher = Teacher.objects.filter(Q(pk=pk))

        if teacher:
            data = TeacherSerializer(teacher.values()[0]).data
        else:
            data = {}
        data_list.append(data)

        result = dict()
        result['result'] = data_list

        return Response(result, status=200)

    if request.method == 'PUT':
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)

    if request.method == 'PATCH':
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Patched successfully")
            logging.info(f'INFO: {request.data} updated')
            return Response(None, status=status.HTTP_200_OK)
        else:
            logging.error(f"ERROR: Returned 500")
            logging.error(serializer.errors)
    
    if request.method =='DELETE':
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
```

---

<div id="class-based-view">
 <h2>Using Class Based Views</h2>
 </div>
 
Class based views are more useful then function based views when all of the crud operations will be handled at the same time. In this case, using CBV helps us exercise DRY principle.

<b>This is so because we don't have to use @api_view() decorator again and again.</b>

So, let's refactor our code.

```
classroom_app/
├── __init__.py
├── admin.py
├── apps.py
├── errors.py
├── models.py
├── tests.py
└── views
    │   
    ├── students.py
    └── teachers.py

```

We opened `views` folder and opened `students.py` and `teachers.py`.

students.py

```py
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from classroom_app.models import Student
from api.serializers import StudentSerializer
from classroom_app.errors import return_400_with_error_log, return_404_with_error_log
import logging


class StudentList(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
        result = dict()
        result['result'] = data

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Returned 201")
            logging.info(f'INFO: {request.data} created')
            return Response(None, status=status.HTTP_201_CREATED)
        else:
            return return_400_with_error_log(serializer.errors)
```

teachers.py

```py
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from classroom_app.models import Teacher
from api.serializers import TeacherSerializer
from classroom_app.errors import return_400_with_error_log, return_404_with_error_log
import logging


class TeacherList(APIView):
    """
    List all teachers, or create a new teacher.
    """

    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        data = TeacherSerializer(teachers, many=True).data
        result = dict()

        result['result'] = data
        if result['result']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logging.info(f"INFO: Returned 201")
            logging.info(f'INFO: {request.data} created')
            return Response(None, status=status.HTTP_201_CREATED)
        return return_400_with_error_log(serializer.errors)
```

Going to urls.py under api folder.

```
api
│   
├── serializer_functions.py
├── serializers.py
└── urls.py
```

```py
from django.urls import path
from classroom_app.views.teachers import TeacherList, TeacherDetails
from classroom_app.views.students import StudentList, StudentDetails

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetails.as_view()),
    path('teachers/', TeacherList.as_view()),
    path('teachers/<int:pk>/', TeacherDetails.as_view())
]
```

We changed it like this. Note that `as_view()` is used for class based views.

---

<div id="mixins">
 <h2>Using Mixins</h2>
 </div>
 
 DRF also provides us with mixins that will reduce boilerplate code.
 
 ```py
from rest_framework import mixins
from rest_framework import generics


class TeacherList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all teachers, or create a new teacher.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```
   
For example, here we have get and post methods taken care for us by `mixins.ListModelMixin` and `mixins.CreateModelMixin`.

`generics.GenericAPIView` is responsible for creating the core view.

I'm kind of leaning towards using the old CBV since we can't use logging functionality here, also we can't send a customized response such as `result = [{...}]`

And the following picture is for handling other CRUD operations.

<p align="center">
 <img width="650" alt="Screen Shot 2021-08-19 at 6 44 30 PM" src="https://user-images.githubusercontent.com/31994778/130099781-94601265-e469-4948-aa4b-2bdf1974898c.png">
 </p>
 
 Also, Generic CBV can be used to reduce code even more
 
 <p align="center">
 <img width="650" alt="Screen Shot 2021-08-19 at 6 47 13 PM" src="https://user-images.githubusercontent.com/31994778/130100380-f760e588-47dd-4382-b918-11dffa81e9c6.png">
 </p>
 
 ---
 
 <div id="validators">
 <h2>Validators</h2>
 </div>
 
 We can define validators and use them in validation of serializer fields.
 
 ```py
 class SomeModelSerializer(serializer.Serializer):
      some_field = (validators[<our validator>])
```

Let's define validate_age() function

```py
def validate_age(data):

    if not(data > 18 and data < 100):
        raise ValidationError('Age should be between 18-100.')
```

Use it in Student serializer

```py
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(validators=[validate_age])
    teacher = serializers.CharField(max_length=100, required=False)
```

This is one way of validating age. Another way is to use validate_age() function in `validate(self, attrs)`.

```py
def validate(self, attrs):

        apply_validator(validate_special_char, attrs)
        validate_age(attrs.get('age'))
        return attrs
```

---

<div id="model-serializer">
 <h2>Model Serializer</h2>
 </div>
 
 Model serializers are just like serializers, in that they help with validation of data, and serialization-deserialization of objects. However, they are created based on the model.
 
 I personally find not very productive, in that it just reduces boiler-plate code such as `create()`, `update()` methods.
 
 ```py
 class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, attrs):
        apply_validator(validate_special_char, attrs)
        validate_age(attrs.get('age'))
        return attrs
```

This is the same as StudentSerializer we used before. It's good to reduce boiler-plate code.

To hide 'teacher' from the response,

```py
class Meta:
        model = Student
        read_only_fields = ['id']
        exclude = ['teacher']
```


<div align="center">
<img width="290" alt="Screen Shot 2021-08-20 at 12 06 58 AM" src="https://user-images.githubusercontent.com/31994778/130144162-cbc0a47a-77bc-4b0f-969e-30d53a24bdb1.png">

<img width="276" alt="Screen Shot 2021-08-20 at 12 07 03 AM" src="https://user-images.githubusercontent.com/31994778/130144183-30869ba3-2161-4c57-ac89-4a74346e49d9.png">
</div>

<br>

We can also set default values like this.

```py
class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, default='test@test.com')

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if k != "email"}
        apply_validator(validate_special_char, temp_dict)
        validate_email(attrs.get("email"))
        return attrs
```

<b> Note that `fields` and `exclude` can't be used together. Either one should be used.</b>

---

<div id="custom-fields">
 <h2>Serializer Method Fields</h2>
 </div>
 
 This is a read-only field. It gets its value by calling a method on the serializer class it is attached to. It can be used to add any sort of data to the serialized representation of your object. 
 
 This is like `$addFields` in mongo.
 
 Image that we are school IT, and have to defined an email for each student enrolled.
 
 ```py
 defined_email = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']

    def get_defined_email(self, object):
        return f'{object.first_name.lower()}@school.com'
```

<p align="center">
<img width="581" alt="Screen Shot 2021-08-20 at 8 17 14 AM" src="https://user-images.githubusercontent.com/31994778/130183603-b0079dab-8176-4257-b812-8a47406c5e45.png">
 </p>

---

<div id="relationships">
 <h2>Relationships</h2>
 </div>
 
 <h3>Foreign Key vs Primary Key</h3>
 
 In relational databases, the two important terms are `Foreign Key` and `Primary Key`.
 
 Since relational databases consists of tables that have one of the relationships, i.e., one-to-one, one-to-many, many-to-many, usage of these keys are essential.
 
 <b>Primary Key:</b> A primary key is a unique identifier for a database table's rows.
 
 - It cannot be null.
 - It should be unique for each row.
 - Every row must have a primary key value.

A customer id in a banking database can be an example of a primary key.

<b>Foreign Key:</b> A FOREIGN KEY is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table.

The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.

<b>Example</b>([Ref](https://www.geeksforgeeks.org/difference-between-primary-key-and-foreign-key/))

<p align="center">
 <img width="600" alt="Screen Shot 2021-08-20 at 10 59 02 PM" src="https://user-images.githubusercontent.com/31994778/130287305-1771e2f8-7b08-407c-924c-16d8fb482ef9.png">
 </p>
 
 <p align="center">
<img width="499" alt="Screen Shot 2021-08-20 at 10 59 05 PM" src="https://user-images.githubusercontent.com/31994778/130287337-44f2dde6-15ce-40d5-a1a5-1799f3bc90be.png">
 </p>

```
Notice that the "PersonID" column in the "Orders" table points to the "PersonID" column in the "Persons" table.

The "PersonID" column in the "Persons" table is the PRIMARY KEY in the "Persons" table.

The "PersonID" column in the "Orders" table is a FOREIGN KEY in the "Orders" table.
```

<h3>Comparison</h3>

<p align="center">
 <img width="651" alt="Screen Shot 2021-08-20 at 11 03 13 PM" src="https://user-images.githubusercontent.com/31994778/130287707-46a44280-e985-41ee-a122-09ac0d910308.png">
 </p>
 
 ---
 
 <h3>Relationships</h3>
 
 There are three kinds of relationship in relational databases. These are, `one-to-one`, `many-to-one`, and `many-to-many`.
 
 <h4>one-to-one</h4>
 
 In one-to-one relationship, one record in a table is associated with one and only one record in another table. For example, in a school database, each student has only one student ID, and each student ID is assigned to only one student. [Ref](https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-one-relationships.html)
 
 <div>
<img width="450" src="https://user-images.githubusercontent.com/31994778/130310478-93c3a40e-423a-4149-b583-7708d34b39cb.png">
<img width="450" height="164.86" src="https://user-images.githubusercontent.com/31994778/130310480-95e9f4bb-f085-4c4e-b567-a5ccf88a5119.png">
 </div>
 
 In this example, the key field in each table, Student ID, is designed to contain unique values. In the Students table, the Student ID field is the primary key; in the Contact Info table, the Student ID field is a foreign key.

This relationship returns related records when the value in the Student ID field in the Contact Info table is the same as the Student ID field in the Students table.

Now, let's rewrite our models so that `Student` and `StudentDetail` are two models and they are connected with `one-to-one` relationship.

```py
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Student ID: {self.id}'

class StudentDetail(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='student'
    )
    city = models.CharField(max_length=100, default=None, blank=True)
    email = models.EmailField(max_length=100, default=None, blank=True)
    phone = models.CharField(max_length=12,
                             blank=True, unique=True, default=None)

    def __str__(self):
        return self.student_id
```

`StudentDetail` model is connected to `Student` with `student` field.

<div>
 <img width="350" alt="Screen Shot 2021-08-21 at 12 35 40 PM" src="https://user-images.githubusercontent.com/31994778/130317681-a9cab28a-0859-45e4-9fa1-74da5ece2470.png">
<img width="600" alt="Screen Shot 2021-08-21 at 12 35 50 PM" src="https://user-images.githubusercontent.com/31994778/130317689-990bb703-a3a2-4da3-a440-38f64497b3b3.png">
 </div>
 
 Now, admin panel looks good, but we have to rewrite our serializers to be able to use see serialized responses
 
 ```py
 class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        read_only_fields = ['student_id']
        exclude = ['age']

    def validate(self, attrs):
        apply_validator(validate_special_char, attrs)
        validate_age(attrs.get('age'))
        return attrs

class StudentDetailSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = StudentDetail
        fields = '__all__'

    def get_age(self, object):
        return object.student.age
```

This is what's called a `Nested Serializer` [Ref](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships).

After making some changes in the view, the response would look like follows:

<div>
 <img width="450" height="527.52" alt="Screen Shot 2021-08-21 at 12 43 28 PM" src="https://user-images.githubusercontent.com/31994778/130317906-aee5e108-b21d-40b2-8264-48f2706b43e2.png">
<img width="450" height="527.52" alt="Screen Shot 2021-08-21 at 12 43 39 PM" src="https://user-images.githubusercontent.com/31994778/130317921-2f87720a-3e97-42f3-897c-6da3a7d87c46.png">
</div>
 
---

 <h4>many-to-one</h4>
 
 In a one-to-many relationship, one record in a table can be associated with one or more records in another table. For example, each customer can have many sales orders.

A one-to-many relationship looks like this in the relationships graph:

<p align="center">
<img src="https://user-images.githubusercontent.com/31994778/130318088-e919f2ba-6bd3-4b76-976c-e6089e876a05.png">
</p>
                 
In this example the primary key field in the Customers table, Customer ID, is designed to contain unique values. The foreign key field in the Orders table, Customer ID, is designed to allow multiple instances of the same value.

This relationship returns related records when the value in the Customer ID field in the Orders table is the same as the value in the Customer ID field in the Customers table.
                                                                                                                
<p align="center">
<img width="650" src="https://user-images.githubusercontent.com/31994778/130318104-e47f9a96-7bcb-4c04-b793-ccbfc0f209d8.png">
</p>
    
We can use this technique to create a `one-to-many` relationship between students and teachers.
                                                                                                                            
Here, we will set a rule that a student can only have one teacher, but one teacher can have multiple students.
                                                                                                                            
Add this to student model

```
teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="student")
```

And, change TeacherSerializer as 

```py

`class TeacherSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)
    email = serializers.EmailField(required=False, default='test@test.com')

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, attrs):
        temp_dict = {k: v for k, v in attrs.items() if k != "email"}
        apply_validator(validate_special_char, temp_dict)
        validate_email(attrs.get("email"))
        return attrs
```
        
Make small changes in views.py and send GET request to `localhost:8081/api/teachers/`

```
{
    "result": [
        {
            "id": 1,
            "student": [
                {
                    "id": 1,
                    "first_name": "Burakhan",
                    "last_name": "Aksoy",
                    "teacher": 1
                },
                {
                    "id": 3,
                    "first_name": "Bugra",
                    "last_name": "Senyurt",
                    "teacher": 1
                }
            ],
            "email": "ahmet.yadigar@test.com",
            "first_name": "Ahmet",
            "last_name": "Yadigar"
        },
        {
            "id": 2,
            "student": [
                {
                    "id": 2,
                    "first_name": "Cevdet",
                    "last_name": "Sarac",
                    "teacher": 2
                }
            ],
            "email": "test@test.com",
            "first_name": "Mehmet",
            "last_name": "Bolukbas"
        }
    ]
}
```

Now, send a GET request to `localhost:8081/api/teachers/1/`

```
{
    "result": [
        {
            "id": 1,
            "student": [
                {
                    "id": 1,
                    "first_name": "Burakhan",
                    "last_name": "Aksoy",
                    "teacher": 1
                },
                {
                    "id": 3,
                    "first_name": "Bugra",
                    "last_name": "Senyurt",
                    "teacher": 1
                }
            ],
            "email": "ahmet.yadigar@test.com",
            "first_name": "Ahmet",
            "last_name": "Yadigar"
        }
    ]
}
```

As we can see, Teachers have many students and each student has only one teacher.

---

<h4>many-to-many</h4>

In fact, why wouldn't a student have multiple teachers, in the same way that a teacher has multiple students? Let's examine this.

A many-to-many relationship occurs when multiple records in a table are associated with multiple records in another table. For example, many-to-many relationship exists between customers and products. Customers can purchase various products and products can be purchased by many customers.

We are inside models.py

<p align="center">
 <img width="500" alt="Screen Shot 2021-08-21 at 6 10 49 PM" src="https://user-images.githubusercontent.com/31994778/130326312-6d2a1de0-dd96-4266-a914-fb1509f1fb22.png">
 </p>
 
 Now, we are inside serializers.py
 
 <p align="center">
<img width="560" alt="Screen Shot 2021-08-21 at 6 17 38 PM" src="https://user-images.githubusercontent.com/31994778/130326978-99359012-6d32-48e3-8c48-3a910e4e152d.png">
 </p>
 
 And the resulting GET requests
 
 <p align="center">
 <img width="800" alt="Screen Shot 2021-08-21 at 6 20 21 PM" src="https://user-images.githubusercontent.com/31994778/130326517-662d475b-7f14-49c7-bb98-e0c13df48489.png">
 </p>
 
  <p align="center">
 <img width="800" alt="Screen Shot 2021-08-21 at 6 24 30 PM" src="https://user-images.githubusercontent.com/31994778/130326662-e37c2174-152b-4010-9992-c6700a470849.png">
 </p>
 
<b>Here, it's very important to see that we can define as many serializer class as we want. As long as the ones we define for POST, PUT, PATCH methods are static, i.e., not changing, we can defined many serializer classes for displaying GET request results differently.</b>
 
 In this way, serializers of Django are very much like aggregation in MongoDB.
 
 ---
 
 <div id="select-prefetch-related">
 <h2>Select & Prefetch Related</h2>
 </div>
 
  <h3> Select Related </h3>
  
 We use `select_related` on forward relationships such as Foreign Key and OneToOne fields.
 
 We have a model such as follows:
 
 ```py
 class Installment(models.Model):
    schedule = models.ForeignKey("api.InstallmentSchedule", related_name="installments", on_delete=models.PROTECT)
    invoice = models.OneToOneField("api.Invoice", related_name="installment", on_delete=models.PROTECT, null=True)
    ...
    
 ```
 
 Here `Intallment` model has a Foreign Key relationship with schedule and OneToOne relationship with Invoice.
 
 Defining our `traverse` function and `time_` decorator.
 
 ```py
 
    def time_(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            print(f"Time elapsed : {round((t2-t1), 3)}")
        return wrapped
        
    @time_
    def traverse(installments):
        for ins in installments[:20]:
            _, _ = ins.invoice.date_created, ins.schedule.date_created

 ```
 
 Then, our query with select_related:
 
 ```py
 installments = (
       Installment.objects.filter(invoice__isnull=False)
      .select_related("invoice", "schedule")
  )
  
  
  traverse(installments)
  Time elapsed : 0.066s

 ```
 
 Using without select_related
 
 ```py
 installments = (
       Installment.objects.filter(invoice__isnull=False)
  )
    
 traverse(installments)
 Time elapsed : 1.61s
 ```
 
 Summary: <b>Use select_related if you traverse, and hit fields of the objects you fetch from database! </b>
 
  <h3> Prefetch Related </h3>
 
 ---
 
 <div id="students-detail-views">
 <h2>Writing Views for StudentsDetail</h2>
 </div>
 
 
So far, we wrote views for every model, except for StudentDetail. It's important to write views for every model available.

We are here

```
classroom_app/views
│   
├── student_details.py
├── students.py
└── teachers.py
```

Since our endpoint will be as follows,

For GET, POST -> `students/details/`

For Retrieve, PUT, PATCH -> `students/<int:pk>/details`

Inside student_details.py, we use mixins.

<p align="center">
 <img width="607" alt="Screen Shot 2021-08-23 at 3 44 23 PM" src="https://user-images.githubusercontent.com/31994778/130449345-aeaa2932-f1ee-4565-a83b-9a85de6a5fea.png">
 </p>

Then, add to urls.py

```
    path('students/details/', StudentDetailList.as_view()),
    path('students/<int:pk>/details/', StudentDetailRetrieve.as_view()),
    
```
    
<p align="center">
<img width="828" alt="Screen Shot 2021-08-23 at 3 49 03 PM" src="https://user-images.githubusercontent.com/31994778/130449853-a6bca098-6966-492e-8e7c-36c94f7240bd.png">
 </p>
 
 We can also implement Post operation.
 
 Also, look at the endpoint structure
 
 `api/students/2/details/`

Actually, let's not use mixins. This is all repetitive work, let's use generic views.

```py
class StudentDetailRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer


class StudentDetailList(generics.ListCreateAPIView):

    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
```

This is amazingly succinct. Because generics.py does inheritance on the background. [Refer Here](https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py)

<p align="center">
 <img width="584" alt="Screen Shot 2021-08-23 at 7 29 40 PM" src="https://user-images.githubusercontent.com/31994778/130483501-72cc6b09-602d-40fe-a0d8-a2522beee71b.png">
</p>

 ---

<div id="user-model">
<h2>User Model</h2>
 </div>
 
 So far, we didn't do anything about User model. We will do this in this part.
 
 I have an idea. Wouldn't it be great if we have teachers as users that can login to the system and set grades for students who take their class?
 
 Let's do this.

Now, I want only a superuser status to be able to do POST, PATCH, PUT operations.

<p align="center">
 <img width="800" alt="Screen Shot 2021-08-25 at 7 55 01 AM" src="https://user-images.githubusercontent.com/31994778/130729404-e4b5e264-12f8-41f4-9fe6-caa915196295.png">
 </p>

sending a PATCH request to `api/students/1/details/`.

This is achieved by adding the following code piece to our views.

```py
is_super_user = self.request.user.is_superuser
        if not is_super_user:
            raise ValidationError('Only Admin account can do this operation.')
```

In our views, PUT, DELETE, PATCH, POST operations all have this code.

So, unless user is marked as `super user`, they won't be able to make changes regarding these HTTP methods.

We can see this if we debug our code, let's send a POST request to`/api/students/`

<p align="center">
 <img width="800" alt="Screen Shot 2021-08-25 at 8 10 47 AM" src="https://user-images.githubusercontent.com/31994778/130730394-1543c5ba-fc87-44e3-8e97-f70d577ba09d.png">
 </p>
 
 So, user `burak` doesn't have a superuser status. This can also be seen on the admin panel.
 
 <p align="center">
 <img width="550" alt="Screen Shot 2021-08-25 at 8 16 48 AM" src="https://user-images.githubusercontent.com/31994778/130730717-6ad1c851-6eb1-4a7d-aae5-9540a31d28a5.png">
 </p>

But, then again, It's not very safe to give superuser status to every user that needs to make use of  update, delete, add, or list operations.

This should be done with Django's permission classes.

---

<div id="permissions">
 <h2>Permissions</h2>
 </div>
 
 Permissions are very important in Django.
 
 Let's talk about global permissions.
 
 <i>"Permission checks are always run at the very start of the view, before any other code is allowed to proceed. Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted."</i>
 
>Permissions in REST framework are always defined as a list of permission classes.

Before running the main body of the view each permission in the list is checked. If any permission check fails an exceptions.PermissionDenied or exceptions.NotAuthenticated exception will be raised, and the main body of the view will not run.

<p align="center">
 <img width="550" alt="Screen Shot 2021-08-27 at 8 59 25 PM" src="https://user-images.githubusercontent.com/31994778/131169698-682f554a-7f1e-4276-9b08-e8a88b730131.png">
 </p>
 
 <h3>Global Permissions</h3>
 
 Global permissions are very strict and they are not very useful in the sense that the developer does not have the liberty to select which views should be permitted or not. In other words, Global permissions override other permissions, i.e., all class and/or function based views. 
 
 First of all, to use permissions, we need to add `path('api-auth/', include('rest_framework.urls'))` to urls.py.
 
 ```
 urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
```

This will help us determining users login and logout.

If we don't use `path('api-auth/', include('rest_framework.urls'))`, the following login page can't be used

<p align="center">
<img width="374" alt="Screen Shot 2021-08-28 at 10 09 46 AM" src="https://user-images.githubusercontent.com/31994778/131209871-8aeb0708-3272-43fe-966e-d6d81cefe2ed.png">
 </p>

Then, we go to settings.py and make some changes.

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

I also created a user called `burakhan` with only `active` status ticked.

If I don't make a login with any user, I receive the following for all endpoints

<p align="center">
 <img width="800" alt="Screen Shot 2021-08-27 at 9 16 00 PM" src="https://user-images.githubusercontent.com/31994778/131171533-6bb97dad-18cf-4d26-b558-9242b46b7524.png">
 </p>
 
 But If I make a login, then I get to see any api endpoint
 
 <p align="center">
 <img width="800" alt="Screen Shot 2021-08-27 at 9 15 50 PM" src="https://user-images.githubusercontent.com/31994778/131171602-d2879daa-fe8b-4dca-bf5d-50a89ee575e1.png">
 </p>
 
 We can also use some other permission types such as `IsAuthenticatedOrReadOnly`.
 
 Using that will let authenticated users to list and make changes in the endpoints but let unauthenticated users to only see the endpoints.
 
 Like this
 
 <p align="center">
 <img width="800" alt="Screen Shot 2021-08-27 at 9 20 39 PM" src="https://user-images.githubusercontent.com/31994778/131171952-c7968045-5b63-40e3-b1d8-29f992b2d9d0.png">
 </p>
 
 If nothing is provided in settings.py regarding permissions, then django use `AllowAny` as default.
 
 ---
 
 <div id="object-level-permissions">
<h3>Object Level Permissions</h3>
</div>

<i>"Object level permissions are used to determine if a user should be allowed to act on a particular object, which will typically be a model instance."</i>

This is particularly useful when we want to define specific restrictions on specific views.

In our case, <b>everyone</b>(anonymous user as well), will be able to see `/students/`, `/teachers/` endpoints, but only the teachers and/or admin would be able to see`/students/details/`.

```py
from rest_framework.permissions import IsAuthenticated

class StudentDetailView(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving student details.
    """
    permission_classes = [IsAuthenticated]
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
```

 <p align="center">
<img width="1200" alt="Screen Shot 2021-08-28 at 10 37 28 AM" src="https://user-images.githubusercontent.com/31994778/131210621-861f33d3-59aa-491b-bb6e-5184cac7fe04.png">

 </p>
 
  <p align="center">
<img width="1186" alt="Screen Shot 2021-08-28 at 10 40 02 AM" src="https://user-images.githubusercontent.com/31994778/131210624-f85eedfe-fe71-426c-98cc-cc6aa19da482.png">
 </p>
 
 ---
 
 <h3>Custom Permissions</h3>
 
 As we said in [<b>Object Level Permissions</b>](#object-level-permissions)
 
 ><b>everyone</b>(anonymous user as well), will be able to see `/students/`, `/teachers/` endpoints, but only the teachers and/or admin would be able to see`/students/details/`.

For that, we use custom permissions

In our `api` folder, we open up `permissions.py` file, inside

```py
from rest_framework import permissions


class AdminOrTeacherOnly(permissions.BasePermission):
    """
    Object-level permission to only allow teachers of a student to edit.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'Only admin or teacher can list and/or edit student detail.'

    def has_object_permission(self, request, view, obj):
        # Only teacher and/or admin user will be able to,
        # edit and/or list this view.
        is_staff = bool(request.user and request.user.is_staff)

        return obj.student.teacher.first_name == request.user.username or is_staff
```

This will check whether the user is admin via `is_staff`, also checks if requesting user is the teacher.

Let's test it

<p align="center">
 <img width="1177" alt="Screen Shot 2021-08-28 at 1 06 35 PM" src="https://user-images.githubusercontent.com/31994778/131214594-10e14c96-8776-4a8d-b4a7-56744e3b8130.png">
 <b>Admin can do anything, both listing and changing student information.</b>
 </p>

<p align="center">
<img width="1168" alt="Screen Shot 2021-08-28 at 1 07 09 PM" src="https://user-images.githubusercontent.com/31994778/131214656-bf1812d6-758b-4459-a6bb-6bae929b5f16.png">
 <b>Ahmet can only list and change his student's information.</b>
 </p>
 
 <p align="center">
<img <img width="1190" alt="Screen Shot 2021-08-28 at 1 07 24 PM" src="https://user-images.githubusercontent.com/31994778/131214682-016bae4b-bb3b-4ba1-ba43-ecc7e6ac759c.png">
 <b>Ahmet cannot list or change another teacher's student's information.</b>
 </p>
 
 <p align="center">
<img width="1186" alt="Screen Shot 2021-08-28 at 1 09 13 PM" src="https://user-images.githubusercontent.com/31994778/131214723-acc0286e-546d-41fa-a954-a51c19c2556d.png">
 <b>Only related teacher can list or change their student's information.</b>
 </p>
 
 <b>Note:</b> All permission classes should inherit from `permissions.BasePermission`.
 
 Also, as we can see here, that, writing our custom permissions is sometimes more logical than using ready-made permissions. This is so because we can do much more with custom permissions, imagination is the limit.
 
 Also, we should always return a Boolean value when we are creating our custom permissions. Django will run permissions prior to running the view it self, returning True and False in permissions will , in other words, determine if the related view would be executed or not.
 
 ---

<div id="custom-calculations">
 <h2>Custom Calculations</h2>
 </div>
 
 Now, it's time to get fancy. In this part, we are going to create a new endpoint called `add-grade/`, which will be used only by teachers and admin users to add grades to `StudentDetail`.
 
 Our strategy will be as follows:
 
 1- Create a new endpoint and make it accessible only to admins or teachers.
 
 2- Endpoint should only allow `PUT`, `PATCH` request.
 
 3- `StudentDetail` model should have it's`grade` field changed as an Integer List field.
 
 4- `StudentDetail` model hould have a new field called `average_grade` that stores the average of all the grades received.
 
<p align="center">
<img width="600" alt="Screen Shot 2021-08-29 at 9 31 56 AM" src="https://user-images.githubusercontent.com/31994778/131241043-6734ab48-a1f1-4cb9-830c-fd63e93a8dc4.png">
 </p>
 
 <p align="center">
  <b>Adding our `add-grade/` endpoint to urls.py.</b>
 </p>
 
 <p align="center">
 <img width="609" alt="Screen Shot 2021-08-29 at 9 42 45 AM" src="https://user-images.githubusercontent.com/31994778/131242046-c55ff1b2-a28c-493c-9a4d-f5d4a1697b6b.png">
 </p>
 
 <p align="center">
  <b>We introduce grade_no and avg_grade field in our StudentDetail model.</b>
 </p>
 
 <p align="center">
 <img width="800" alt="Screen Shot 2021-08-29 at 9 37 54 AM" src="https://user-images.githubusercontent.com/31994778/131241187-6003eae2-69db-43b9-830f-3e947f6f719e.png">
 </p>
 
 <p align="center">
  <b>We make related calculations here, calculating the avg_grade everytime a teacher submits a grade.</b>
 </p>
 
 <p align="center">
 <img width="1171" alt="Screen Shot 2021-08-29 at 10 40 28 AM" src="https://user-images.githubusercontent.com/31994778/131242760-b3ea9150-fe73-46c6-a290-a457668210ec.png">
 </p>
 
 <p align="center">
 <b>avg_grade and grade fields appears successfully.</b>
 </p>
 
 ---
 
 <div id="authentication">
 <h2>Authentication</h2>
 </div>
 
 So far, every request that we handled, which doesn't require authentication, was through django api interface.
 
 In this chapter, we will learn about different types of authentication, i.e., Basic & Token authentication.
 
 <h3>Basic Authentication</h3>
 
 Weak security. Should only be used for testing purposes.
 
 We add `path('api-auth/', include('rest_framework.urls')),` to our urls.py as:
 
 <img width="535" alt="Screen Shot 2021-10-12 at 10 01 12 PM" src="https://user-images.githubusercontent.com/31994778/137013881-a3eba47b-035f-4a03-9b9e-5f094a90c1e5.png">

 Then, in settings.py, we add:
 
 ```js
 REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication'
    ]
}
```

and inside INSTALLED_APPS

```
INSTALLED_APPS = [
    ...,
    'rest_framework.authtoken',
]
```

Inside our students view, we have

<img width="515" alt="Screen Shot 2021-10-12 at 10 03 19 PM" src="https://user-images.githubusercontent.com/31994778/137014132-0eea2594-e493-4de1-9f49-142c7e3ba5e8.png">

This means that our requests to this view through related url will return 403 Forbidden, as follows:

<img width="832" alt="Screen Shot 2021-10-12 at 10 05 14 PM" src="https://user-images.githubusercontent.com/31994778/137014315-8bfd47ed-8ec3-482d-8cd7-a12ba5b49a71.png">

Here, for Basic Authentication, we need to pass Authorization: Basic <Base64 encoded username:password> inside our headers.

<img width="824" alt="Screen Shot 2021-10-12 at 10 06 20 PM" src="https://user-images.githubusercontent.com/31994778/137014503-a8b07170-5471-4657-ab6d-e5b15cc41061.png">

---

<h3>Token Authentication</h3>

Token authentication is much safer to use than Basic authentication since the latter can be compromised easily given the username and password is stolen. Token authentication, on the other hand, is obtained by a unique token stored inside DB, which makes it much safer than Basic authentication.
 
In order to utilize Token Authentication, we need to add `'rest_framework.authtoken'` to `INSTALLED_APPS` in settings.py:
 
```js
 INSTALLED_APPS = [
    ...,
   'rest_framework.authtoken',
    ...

]
```
 
 After that, since our APPS changed, we need to run `manage.py makemigrations` and `manage.py migrate` once again to create tables in the DB.
 
 Secondly, we need to add `DEFAULT_AUTHENTICATION_CLASSES` to `REST_FRAMEWORK` dict.
 
 ```js
 REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}
```

 Having done these steps, let's login to the admin panel.
 
 As we can see, TOKEN table is created in DB and reflected on the admin panel.
 
 <img width="864" alt="Screen Shot 2021-10-13 at 10 37 51 PM" src="https://user-images.githubusercontent.com/31994778/137201575-cf7eb1e1-5ee0-4c1b-ad74-5db937362e3a.png">

 Here, each user should have their unique token for authentication. For now, we added tokens manually, but we should automate this process later on.
 
 Let's go to our student_details.py view and verify that we have permission and authentication classes.
 
 ```py
from api.permissions import AdminOnly
 
 class StudentDetailView(viewsets.ModelViewSet):
    """
    View for displaying student detail information.
    [
        {
            "student": 1,
            "info": {
                "first_name": "Burakhan",
                "last_name": "Aksoy"
            },
            "age": 26,
            "course": "CS101",
            "teacher": "Ahmet Cevdet",
            "grade": 0,
            "avg_grade": 0.0,
            "city": "Istanbul",
            "email": "burakhan.aksoy@test.com",
            "phone": "218382181221"
        }
    ]
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOnly]
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
 ```
 
 This means that users should be authenticated and also only the admin user can reach this view (permission).
 
 Let's try sending a GET request without authentication...
 
 <img width="1006" alt="Screen Shot 2021-10-13 at 10 31 43 PM" src="https://user-images.githubusercontent.com/31994778/137201983-429d6ed6-4b79-4bae-9c84-bdb864f303e6.png">
 
 As we can see, the Authorization header is not used, that's why we get `401 Unauthorized`.
 
 Let's authenticate but send request with a non-admin user.
 
 <img width="1016" alt="Screen Shot 2021-10-13 at 10 32 12 PM" src="https://user-images.githubusercontent.com/31994778/137202121-93cc99df-f067-4dea-9042-c8b8c1f65479.png">

 This time, we get `403 Forbidden`.
 
 <img width="1068" alt="Screen Shot 2021-10-15 at 1 06 45 AM" src="https://user-images.githubusercontent.com/31994778/137402277-a1eb4871-067a-4542-8f58-7da1d3dc8b0d.png">

 The reason that we got 403 Forbidden is because `burak` does not have permission to access this endpoint.
 
 Let's take a look at our permission_classes...
 
 <img width="483" alt="Screen Shot 2021-10-15 at 1 18 11 AM" src="https://user-images.githubusercontent.com/31994778/137403236-ba837c21-87a0-476a-b595-170543446fac.png">

 As we can see, only the admin user, in other words, `is_staff == True`, will be able to access this endpoint.
 
 
 Let's try with the admin user.
 
 Now, let's use admin token `77a1cdd41bbc138da80ea96e1a378aff7b245c31`.
 
 <img width="570" alt="Screen Shot 2021-10-15 at 1 21 47 AM" src="https://user-images.githubusercontent.com/31994778/137403723-8bb6f96f-885a-4419-ab30-02f8977b7851.png">
 
 After the permission is granted...
 
 <img width="801" alt="Screen Shot 2021-10-15 at 1 24 39 AM" src="https://user-images.githubusercontent.com/31994778/137403859-3b416a3f-d8a6-4327-b3aa-d395483420da.png">

 Voila!
 
 ---
 
 <h2>Handling Login, Logout, Registration</h2>
 
 So far, we added token's to our users manually through Django admin panel. Then, we copied these tokens and pasted as `Authorization: Token asd293104sadk123`.
 
 This is fine and dandy. But of course automating these things would be much better. Imagine we register our users, give them a token, get token, and delete token on logout without using Django admin panel. Let's do that in this part.
 
 <h3>Login</h3>
 
 Let's create a new Django application called `user_app`, just like `classroom_app`. We will use the newly created app only for handling Login, Logout, and Registration.
 
 Firstly, let's create our `user_app` through `python3 manage.py startapp user_app`.
 
 <img width="343" alt="Screen Shot 2021-10-16 at 4 10 19 PM" src="https://user-images.githubusercontent.com/31994778/137588886-813756fa-ec24-44a3-a00b-8a672a18649a.png">

 Then, let's create a new folder `api` to contain our urls.py, views.py, and serializers.py.
 
 <img width="344" alt="Screen Shot 2021-10-16 at 4 11 39 PM" src="https://user-images.githubusercontent.com/31994778/137588929-197d1121-f5a1-4426-ba59-203d4edb367d.png">

 Then, under our Django project folder's settings.py, add the following:
 
 ```js
 INSTALLED_APPS = [
    ...,
    'user_app.apps.UserAppConfig'
]
 ```

 Run makemigrations and migrate again.
 
 Now, inside urls.py of user_app, let's use Django's `obtain_auth_token` view to handle login.
 
 ```py
 from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='login')
]
```
 
 Of course, inside our project urls.py, include the new endpoints coming from `user_app`.
 
 ```js
 urlpatterns = [
    ...,
    path('account/', include('user_app.api.urls'))
]
 ```

 Let's try...
 
 <img width="824" alt="Screen Shot 2021-10-16 at 4 16 28 PM" src="https://user-images.githubusercontent.com/31994778/137589042-0c7dec93-6255-4c87-a625-d98fce01656e.png">

 Awesome.
 
 From now on, we don't have to login through Django admin panel and get the authentication token. We can simply send a POST request to this endpoint.
 
 ---
 
 <h3>Registration</h3>
 
 Firstly, we need a new endpoint, for that, inside our user_app's urls.py:
 
 ```js
 urlpatterns = [
    ...,
    path('register/', RegisterUser.as_view(), name='register'),
]
 ```
 
 Then, inside our user_app's serializers.py:
 
 ```py
 from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    ...
 
    class Meta:
        ...

    def validate(self, attrs):
        ...

    def create(self, validated_data):
        ...
```
 
 Then, inside our user_app's views.py:
 
 ```py
 from django.contrib.auth.models import User
from rest_framework import generics
from user_app.api.serializers import RegisterSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []
```
 
 <img width="600" alt="Screen Shot 2021-10-16 at 7 12 31 PM" src="https://user-images.githubusercontent.com/31994778/137594606-45de46e5-1e7c-4bee-a9ed-2d9058bd6b90.png">

 Checking Django admin panel
 
 <img width="600" alt="Screen Shot 2021-10-16 at 7 13 27 PM" src="https://user-images.githubusercontent.com/31994778/137594623-bc153931-21f1-4bef-acd8-2c7d07581487.png">

 Then, if we login with this user, we should obtain the Token.
 
 <img width="600" alt="Screen Shot 2021-10-16 at 7 15 01 PM" src="https://user-images.githubusercontent.com/31994778/137594689-a97989f6-3220-4a6b-8e6f-c3ce0cb7e505.png">
 
 Now, the main question is:
 
 <b>1- How can we stay logged in when the new user is registered?</b>
  
  <b>2- How can we delete token when the user logs out?</b>
   
 ---
 
   <h3>Automatically Generate Token in Registration</h3>
   
   In the previous parts, we talked about registration and login functionalities. However, we didn't generate our User tokens automatically when we register them.
   
   In this part, let's tackle that challenge.
   
   For reference please read [this document](https://www.django-rest-framework.org/api-guide/authentication/).
   
   For starters, we need to do some touch-up on our `user_app`'s models.py:
 
 ```py
 from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```
 
 This is a great use of the `Observer Pattern` by Django. Here, as soon as a model's save() method is called, Django will dispatch `create_user_auth_token` method.
 
 <img width="629" alt="Screen Shot 2021-10-17 at 11 49 47 AM" src="https://user-images.githubusercontent.com/31994778/137619534-e0da89d6-dcb4-43c8-ab41-eed54a5ce64c.png">

For more on this, refer to [here](https://docs.djangoproject.com/en/3.2/topics/signals/).
 
 <b>Now that we know as soon as we create a new User, this code snippet will be triggered as a callback function and a token will be generated for the registered user.</b>
 
 Let's take a look at our `RegisterSerializer`:
 
 ```py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    ...

    class Meta:
       ...

    def validate(self, attrs):
        ...

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        validated_data.pop('password')
        validated_data.pop('password2')
        validated_data['token'] = Token.objects.get(user=user).key
        return validated_data
```
 
 Here, let's focus on the `create` method. This method will be called when we call `serializer.save()` in our registration view.
 
 Here, we pop `password` and `password2` fields from the validated_data and add `validated_data['token'] = Token.objects.get(user=user).key`. Removing password fields from validated_data wouldn't be a problem because we do that after we call `user.save()`.
 
 Let's take a look at the `views.py`:
 
 ```py
from django.contrib.auth.models import User
from rest_framework import generics
from user_app.api.serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response


class RegisterUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = {}
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
        else:
            data['errors'] = serializer.errors

        if 'errors' in data.keys():
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_201_CREATED)
```
 
 Here, if the serializer is valid, we call serializer.save() and return a 201_Created response, else 400 Bad Request.
 
 <img width="600" alt="Screen Shot 2021-10-17 at 11 58 40 AM" src="https://user-images.githubusercontent.com/31994778/137619928-d033ffcb-d2f0-47e7-9fc2-9c0054ad47c7.png">
 
 Let's check the Django admin panel to verify whether we created our user successfully or not.
 
 <img width="600" alt="Screen Shot 2021-10-17 at 12 00 23 PM" src="https://user-images.githubusercontent.com/31994778/137619988-cd98c82b-47b1-4ede-92ac-95ab919a6f88.png">
 
 Now, let's check if the Token is generated automatically.
 
 <img width="600" alt="Screen Shot 2021-10-17 at 12 00 49 PM" src="https://user-images.githubusercontent.com/31994778/137620003-235483c1-96a6-4242-92e4-1294a871d05c.png">
 
 Awesome
 
 Of course, if we want to register the same user again, we should have errors.
 
 <img width="600" alt="Screen Shot 2021-10-17 at 12 41 14 PM" src="https://user-images.githubusercontent.com/31994778/137621535-817a85e1-aeae-4d34-8aaa-cfc42dde44d7.png">
 
 Here, I used Mr. Yunus Emre Cevik's serializer class that I bumped into on medium. 
 
 Please check out his great [article](https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5).
 
 ---
 
 <h3>Logout</h3>
 
 We previously asked the following question, <b>How can we delete token when the user logs out?</b>.
 
 Let's handle that.
 
 Inside `user_app` app folder, created views folder and added logout.py file.
 
 <img width="348" alt="Screen Shot 2021-10-17 at 1 33 21 PM" src="https://user-images.githubusercontent.com/31994778/137623431-f20cbd35-f363-47d4-b97f-e8ee50d7ed35.png">

 Then, inside our logout.py, we have:
 
 ```py
 from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication

class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        data = {"msg":"logout successfully."}
        return Response(data, status= status.HTTP_200_OK)
```
 
 Of course, under urls.py of our app `user_app`, added the new endpoint:
 
 ```js
 urlpatterns = [
    ...,
    path('logout/', logout.as_view(), name='logout'),
]
 ```

 Our aim is as follows:
 
 1- If user is registered and logged in, logout should delete their token.
 
 2- If user is not logged in, logout should return 401.
 
 Currently, I am logged in as `burakhan`, and newly generated Token matches with the one in Django admin panel.
 
 <img width="600" alt="Screen Shot 2021-10-17 at 1 37 11 PM" src="https://user-images.githubusercontent.com/31994778/137623573-b8e066ba-d9fb-47a8-a12b-79ac203bf002.png">

<img width="600" alt="Screen Shot 2021-10-17 at 1 37 30 PM" src="https://user-images.githubusercontent.com/31994778/137623580-e383841e-0b5f-488f-a25e-27155f910a15.png">

 Now, let's logout.
 
 <img width="830" alt="Screen Shot 2021-10-17 at 1 39 56 PM" src="https://user-images.githubusercontent.com/31994778/137623657-acd0ed9e-4853-477a-bb56-b571c0ebaa7f.png">
 
 And check the Django admin panel.
 
 <img width="741" alt="Screen Shot 2021-10-17 at 1 40 55 PM" src="https://user-images.githubusercontent.com/31994778/137623673-013af8b5-34e1-4c5b-9c01-6e3f7f66b2a4.png">
 
 As we can see, `burakhan`'s token is deleted. However, as a user, `burakhan` still exists in our DB.
 
 <img width="758" alt="Screen Shot 2021-10-17 at 1 41 52 PM" src="https://user-images.githubusercontent.com/31994778/137623719-c807fd7b-09fb-485b-b390-75167949433a.png">

---
 
 <h3>JWT</h3>
 
 <b>"JSON Web Token is a fairly new standard which can be used for token-based authentication. Unlike the built-in TokenAuthentication scheme, JWT Authentication doesn't need to use a database to validate a token."</b> [ref](https://www.django-rest-framework.org/api-guide/authentication/)
 
 <h4>Why JWT?</h4>
 
 - No need for DB: Using JWT doesn't require server side lookup. This means that in each request we send using JWT, since the authentication token is not stored in the DB, the server doesn't have to look for the authentication token. This comes in handy when we have microservices on our server side acting as a load balancer. If we use session authentication, each server side microservice would have a different session and the user needs to authenticate again and again when a different microservice is used.
 
 - No need to regenerate token for different servers: Imagine that we have a web app for a banking site. On the background we have different servers and we don't want our users to login again and again for reaching to different servers.
 
 <img width="399" alt="Screen Shot 2021-10-23 at 5 27 02 PM" src="https://user-images.githubusercontent.com/31994778/138560566-a886285b-e328-4f38-8453-4a3ea1a422fe.png">
 
 Here, we have `Bank` and `Retirement` servers. If we use session based authentication, then our users have to relogin(re-authenticate) for displaying features of these servers. This is due to the fact that one server's session wouldn't be recognized by the other because in each session, the related server will generate a session in server memory and when our users want to display content from the other server this session will not match and they have to relogin for that server to generate a session. [ref](https://www.youtube.com/watch?v=7Q17ubqLfaM)
 
 Session based authentication is displayed as follows:
 
 <img width="670" alt="Screen Shot 2021-10-23 at 4 57 59 PM" src="https://user-images.githubusercontent.com/31994778/138560731-367bb22e-c98d-47a2-a6a1-cd3c9c9d38d5.png">
 
 <h4>Structure of JWT</h4>
 
 JWT has three main parts, i.e., `Header`, `Payload` and `Signature`.
 
 <h4>Header</h4>
 
 <img width="573" alt="Screen Shot 2021-10-23 at 5 36 19 PM" src="https://user-images.githubusercontent.com/31994778/138560830-f82371d7-7adf-4d42-a7f6-9d3b237033fc.png">
 
 <b>"The header typically consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA."</b> [ref](https://jwt.io/introduction)
 
 For example:
 
 ```js
 {
  "alg": "HS256",
  "typ": "JWT"
}
 ```
 
 Then, this JSON is <b>Base64Url encoded</b> to form the first part of the JWT.

 <h4>Payload</h4>
 
 <b>"The second part of the token is the payload, which contains the claims. Claims are statements about an entity (typically, the user) and additional data. There are three types of claims: registered, public, and private claims."</b>
 
 An example payload could be:
 
 ```js
 {
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
 ```
 
 The payload is then <b>Base64Url encoded</b> to form the second part of the JSON Web Token.
 
 <h4>Signature</h4>
 
 The signature might be the most important part of the JWT structure. It is the part that lets the server recognize client.
 
 The signature consists of Base64Url encoded version of the header and the payload. Also, the `secret`, which is only known by the server, is added to this composition and the signing algorithm, in our case HS256 -> Hash-based Message Authentication Code using SHA-256 hashing function, is used to create the signature. [ref](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.hmacsha256?view=net-5.0)
 
 To be concise, signature is created as follows:
 
 ```js
 HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
 ```
 
 The signature is used to make sure that the client didn't change anything on the get-go.
 
 For example, we used the above header and the above payload to create the signature as:
 
 `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`
 
 If something's changed on the client side, then the signature is also changed and the server now knows that the signatures do not match and restricts access to the client.
 
 <img width="288" alt="Screen Shot 2021-10-23 at 5 57 17 PM" src="https://user-images.githubusercontent.com/31994778/138561483-490e12eb-f01c-44c7-bde7-ba3c668196ef.png">

 But if the client doesn't change anything, then the server matches the signature and knows that everything is okay and permits access.
 
 <img width="315" alt="Screen Shot 2021-10-23 at 5 57 03 PM" src="https://user-images.githubusercontent.com/31994778/138561503-2857666e-96b0-41de-9020-3b7e235fc404.png">

Here, the most important thing is that we need to make sure our `secret` is protected well enough so that intruders wouldn't have access to it. If they have access to the `secret`, then they can fake it and create a signature and send requests successfully.
 
 <img width="572" alt="Screen Shot 2021-10-23 at 5 58 37 PM" src="https://user-images.githubusercontent.com/31994778/138561606-e07d87e8-911d-4621-b655-bf2c905f4432.png">

 JWT based authentication is displayed as follows: 
 
 <img width="665" alt="Screen Shot 2021-10-23 at 4 57 49 PM" src="https://user-images.githubusercontent.com/31994778/138561664-df4c4146-d37f-4211-a7c2-3f53f06d80c6.png">

 ---
 
 <h3>Changing Our Project with JWT</h3>
 
Under `user_app.api`, inside urls.py, let's add the url patterns:
 
```py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    ...,
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Also, in our views let's make the following change for all
 
 ```py
 from rest_framework_simplejwt.authentication import JWTAuthentication
 
 class StudentList(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrTeacherOnly]

    def get(self, _, format=None):
      ...
 ```

 Then, send a POST request to `/account/api/token/` with username and password to get access token and refresh token
 
 <img width="600" alt="Screen Shot 2021-10-24 at 1 06 36 PM" src="https://user-images.githubusercontent.com/31994778/138589387-df3db37c-5974-44f2-9f6c-e5e450ae9b98.png">

 Now, let's use the access token in one of our endpoints:
 
 <img width="600" alt="Screen Shot 2021-10-24 at 1 08 28 PM" src="https://user-images.githubusercontent.com/31994778/138589428-adcbf556-bd39-4de1-8e89-348874f118ab.png">

 Note that for JWT tokens, we should use it as `Bearer {{ access token }}`.
 
 However, access token is only valid for 5 minutes. When 5 minutes is due, we will have the following:
 
 <img width="604" alt="Screen Shot 2021-10-24 at 1 12 48 PM" src="https://user-images.githubusercontent.com/31994778/138589516-e133a218-562b-41c2-9aef-333490248535.png">
 
 Then, we need to use refresh token (which is available for 24 hours) to get a new access token.
 
 <img width="600" alt="Screen Shot 2021-10-24 at 1 13 40 PM" src="https://user-images.githubusercontent.com/31994778/138589539-9dff5615-4cdf-4cae-902d-3e68712b99a2.png">
 
 This is a new access token.
 
 ---
 
 <h3>Handling Registration</h3>
 
 We can refer [here](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html) for handling registration.
 
 The only thing we need to do is to go to `user_app.api.serializers` and make the following changes:
 
 ```py
...
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    ...

    def create(self, validated_data):
        ...
        ...
        refresh_token = str(RefreshToken.for_user(user))
        access_token = str(RefreshToken.for_user(user).access_token)
        validated_data['token'] = {
            "refresh": refresh_token, "access": access_token}
        return validated_data
```
 
 After this, let's register.
 
 <img width="600" alt="Screen Shot 2021-10-24 at 6 56 03 PM" src="https://user-images.githubusercontent.com/31994778/138602066-2e541e83-d4b3-4706-afd1-e28cf33c1d33.png">
 
<img width="600" alt="Screen Shot 2021-10-24 at 6 56 29 PM" src="https://user-images.githubusercontent.com/31994778/138602076-f3fcad5d-4f3e-4bd9-812c-28dc16543ffc.png">

 And then, send a request.
 
 <img width="600" alt="Screen Shot 2021-10-24 at 6 57 44 PM" src="https://user-images.githubusercontent.com/31994778/138602097-ff2fc75c-119c-4652-a24c-292f6ebd265e.png">
 
 ---
 
 ---
 
 <p id = "unit-tests">
  <h2>
  Unit Tests
 </h2>
 </p>
 
 Now that we finished most of our project. We can start introducing unit tests.
 
 One thing to remember is that <b>Each app should have their own testing module</b>.
 
 Let's start by writing unit tests for our `user_app`, which handles registeration, login, and logout features.
 
 <h4>Refactoring our project structure</h4>
 
 ```
Project
├── app
│   ├── __init__.py
│   ├── ... # Here we have other apps and some related files
│   ├── ...
│   ├── ...
│   └── user_app # This is the app which we want to write UTs
│       ├── __init__.py
│       ├── admin.py
│       ├── api
│       │   ├── serializers.py
│       │   └── urls.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py
│       ├── tests # This is our test module 
│       │   ├── __init__.py
│       │   ├── test_login.py
│       │   ├── test_logout.py
│       │   └── test_register.py
│       └── views
│           ├── __init__.py
│           ├── logout.py
│           └── register.py
├── django_env
│   
├── requirements.txt
```

We refactor our project like this. We need to emphasize once again that <b>Each app should have their own testing module.</b>

<img width="348" alt="Screen Shot 2021-10-31 at 11 01 01 AM" src="https://user-images.githubusercontent.com/31994778/139573832-c5a91ba6-0bfc-43ab-9e33-2e6a9a30beaa.png">

Inside our `user_app`, we have such structure:

<img width="193" alt="Screen Shot 2021-10-31 at 11 04 23 AM" src="https://user-images.githubusercontent.com/31994778/139573905-9319f9cb-eac1-40ae-b649-fb3fb5819de8.png">

We created a `tests` module which consists of our unit test suites.

Inside `tests` module:

<img width="192" alt="Screen Shot 2021-10-31 at 11 06 59 AM" src="https://user-images.githubusercontent.com/31994778/139573958-e6219abe-37ad-40e9-b731-5bb3ba964ce2.png">

Now that we re-structured our project, we can dive deep into writing our unit tests.

---

<h3>Testing Registration</h3>

Registration is an important part of our app. As we previously mentioned, our `register.py` view in `user_app` app handles the following:

- Registering a new user with the following conditions:
    
    - Each user should have a <b>unique email</b>
    - Each user should have a <b>unique username</b>
    - Entered passwords should match
    - Registered user cannot register again

We need to test these requirements.

```py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
import json

expected_responses = {...} # this dict contains the responses we expect for different test cases

class TestAccountCreate(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''
        
    ... # other test cases that we have comes here
    
```

Before diving into the actual code, let's mention the classes that we imported.

<h4>User Class from django.contrib.auth.models</h4>

User class of django.contrib.auth.models is the class that Django has for managing users.

For example, creating a super user, creating staff users, creating normal users. All happens with this class.

We use this class for our tests to verify that a token is generated for the registered user.

<h4>APITestCase Class from rest_framework.test</h4>

<a href="https://www.django-rest-framework.org/api-guide/testing/#api-test-cases">
<img width="600" alt="Screen Shot 2021-10-31 at 3 03 03 PM" src="https://user-images.githubusercontent.com/31994778/139582137-178656fe-a120-4b6c-9e03-72a4909bd871.png">
</a>

APITestCase class inherits from TestCase class, which has the necessary methods and properties for creating a test suite.

<h4>APIClient</h4>

APIClient is the client, just like Postman, to make requests. It supports the HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

<h4>reverse</h4>

Reverse is used for fetching the related endpoint to test.

Using reverse, we can fetch the related endpoint through endpoint's `name`, as follows:

<img width="440" alt="Screen Shot 2021-10-31 at 3 13 39 PM" src="https://user-images.githubusercontent.com/31994778/139582765-cd747fb3-4339-4215-a358-4f3a659ddd91.png">

---

<h3>Testing Registration</h3>

Now, we are ready to test registration.

```py
class TestAccountCreate(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''

    def test_user_create(self):
        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test@test.com",
            "password": "testtest1234",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')
        generated_token = response.data.pop('token')

        expected_result = expected_responses.get('user_create_success')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected_result)
        self.assertIsNotNone(generated_token)
```

In this test suite, we have total of 7 cases, all of which starts with `def test_*`.

`setUp` method is run before each test case execution.

We write test case names verbosely, meaning that they should be clear and definitive of what they are supposed to do.

Here, we send a success case, i.e., successfully registering a user. For that we have `data` dict. We get the response by sending a POST request with the client, get generated_token for that user and make assertions.

Here, we test 3 things:

- Returned status code is 201.
- response.data equals the expected result.
- generated token is not None.

Let's make another test case.

```py
def test_user_create_same_username_different_email_error(self):
        User.objects.create(username="test_user")

        self.url = reverse('register')
        data = {
            "username": "test_user",
            "email": "test1@test.com",
            "password": "testtest1234",
            "password2": "testtest1234",
            "first_name": "test",
            "last_name": "test"
        }
        response = self.client.post(self.url, data=data, format='json')

        expected_result = json.dumps(expected_responses.get(
            'same_username_different_email_error'))

        result = json.dumps(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result, expected_result)
```

Here, test case name is very verbose, which is okay, `test_user_create_same_username_different_email_error`.

It tels us what this test case is about, <b>testing registration of the same username but email is different</b>.

By default, APITestCase flushes the DB, so the first test case's created user is flushed after first test case is executed. That's why we run `User.objects.create(username="test_user")` at the beginning of this test case.

Then, we try to register a user with the same username, `test_user`. We expect 400 response and make the necessary assertions.

---

<p id="vs-code-integration">
<h2>Running Our Tests Through VSCode</h2>
</p>

Using VSCode for running our tests is just awesome. It makes our job easier.

On the debugger, when I click on this:

<img width="348" alt="Screen Shot 2021-10-31 at 3 34 25 PM" src="https://user-images.githubusercontent.com/31994778/139583435-0df73ebc-cb07-4b67-b669-89e2138a21f1.png">

I get:

<img width="493" alt="Screen Shot 2021-10-31 at 3 35 33 PM" src="https://user-images.githubusercontent.com/31994778/139583467-9c33ef82-427f-4c6e-b8dd-0cf1baa1a8af.png">

Awesome. So, let's do the configuration to realize this.

Under `.vscode` folder, we have `settings.json` and `launch.json`.

<img width="350" alt="Screen Shot 2021-10-31 at 3 36 21 PM" src="https://user-images.githubusercontent.com/31994778/139583527-4b86642e-b2a7-4709-a171-96fca14db586.png">

Under settings.json, let's use this configuration:

```js
{
    "python.pythonPath": "/usr/local/bin/python3",
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./app/user_app/tests",  # This is the directory pointing to our test module
        "-p",
        "test_*.py"  # This will run every test file starting with "test_"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true
}
```

This is the configuration for our test runner, which is `unittest`.

Then, let's configure VSCode debugger, under `launch.json`:

```js
{
  "version": ...
  "configurations": [
     ...,
    {
      "name": "test-user-app",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/app/manage.py",
      "args": [
        "test",
        "user_app.tests"
      ],
      "django": true
    }
  ]
}
```

This creates our debugger.

Which makes it available on the bottom left corner as:

<img width="641" alt="Screen Shot 2021-10-31 at 3 44 04 PM" src="https://user-images.githubusercontent.com/31994778/139583907-1d60df08-cada-4ce4-9343-61aede2b9640.png">

---

<div id="throttling">
 
 <h2>Throttling</h2>
 
<b><i> "Throttling is similar to permissions, in that it determines if a request should be authorized. Throttles indicate a temporary state, and are used to control the rate of requests that clients can make to an API."</i></b> [ref](https://www.django-rest-framework.org/api-guide/throttling/)
 
 <b><i>"As with permissions and authentication, throttling in REST framework is always defined as a list of classes.

Before running the main body of the view each throttle in the list is checked. If any throttle check fails an exceptions.Throttled exception will be raised, and the main body of the view will not run."</i></b> [ref](https://www.django-rest-framework.org/api-guide/throttling/#how-throttling-is-determined)
 
 For starters, we add the following fields to settings.py, resulting in:
 
 ```py
 REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'api.permissions.AdminOrTeacherOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1/day',
        'user': '2/day'
    }
}
 ```
 
 This is applied globally, meaning that each API endpoint will heed these settings. Let's try!
 
 <img width="600" alt="Screen Shot 2021-11-21 at 5 27 03 PM" src="https://user-images.githubusercontent.com/31994778/142765896-e2ac3c96-1968-4b2b-bb8d-c39d1bd73b5c.png">

 Here, I made two requests to `api/students/` endpoint and the second one is throttled.
 
 The same will be applied to an authenticated user on the 3rd request.
 
 <b>Caveat:</b> When we apply throttling settings globally, this causes the following:
 
 - Each and every view is affected by the global setting. When you run out of x requests per day, minute, hour, you cannot send another to a different view.
 
 For example, here I cannot send any requests to `api/teachers/` endpoint since ran out of my requests on `api/students/` endpoint.
 
 <img width="600" alt="Screen Shot 2021-11-21 at 5 48 22 PM" src="https://user-images.githubusercontent.com/31994778/142766721-bebf878c-4bcd-46d4-8573-83c4777b0abc.png">

 ---
 
 <h3>Local Throttling</h3>
 
 Local throttling is only applied to a specific view in your application.
 
 For local throttling, remove `DEFAULT_THROTTLE_CLASSES` key from settings.py
 
 <img width="395" alt="Screen Shot 2021-11-21 at 5 50 49 PM" src="https://user-images.githubusercontent.com/31994778/142766888-6b4c3ed0-9bbc-49de-8050-c29637ffdba1.png">

Having removed it, import `UserRateThrottle` and `AnonRateThrottle` in your view file such as:
 
 ```py
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class StudentList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AdminOrTeacherOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get(self, _, format=None):
         ...
 ```
 
 In this way, we will be able to send requests to other views without being cut down by throttling error.
 
 Throttled for `api/students/` api :
 
 <img width="600" alt="Screen Shot 2021-11-21 at 5 54 13 PM" src="https://user-images.githubusercontent.com/31994778/142767031-601efa48-4735-48c4-b460-0d390541eb8b.png">

 Sending another view (`api/teachers/`) successfully:
 
 <img width="600" alt="Screen Shot 2021-11-21 at 5 55 15 PM" src="https://user-images.githubusercontent.com/31994778/142767070-da04ba9d-2e2f-4eb9-818b-69c4181d18f3.png">

 
 </div>
 
---

<h2>Custom Throttling</h2>

After seeing Global and Local throttling, it's now time for us to discover and move on with Custom Throttling.

The difference between Global and Custom Throttling might be obvious, however, the same might not go for that of Local and Custom Throttling.

<b>Differences Between Custom and Local Throttling</b>

- Local throttling, at least for our example, is shared across implementing views, i.e., API count is shared between the views.
  - For example, total of 10 requests/day, we can spend 9 for one view and 1 for another.
- This phenomenon does not apply to custom throttling. Custom throttling is unique to a view, hence the name custom, so it's not shared with another view. Well, it shouldn't be shared.
 
- Custom throttling is implemented by inheriting from a base throttle class and overriding it's `allow_request(self, request, view)` method.

---

<h3>Writing Our Custom Throttling Class</h3>

<img width="377" alt="Screen Shot 2021-11-26 at 8 02 56 PM" src="https://user-images.githubusercontent.com/31994778/143613110-7d04ab08-8f8c-4d5f-87c1-cc0af276e31c.png">

Now, we just created `throttling.py`, and inside, we have:

```py
from rest_framework import throttling


class StudentListUserThrottle(throttling.UserRateThrottle):
    scope = 'get_student_usr_throttle'

    def allow_request(self, request, view):
        return super().allow_request(request, view)


class StudentListAnonThrottle(throttling.AnonRateThrottle):
    scope = 'get_student_anon_throttle'

    def allow_request(self, request, view):
        return super().allow_request(request, view)
```

Here, defining `scope` variable is important. So that we can use them inside settings.py, as follows:

```py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'api.permissions.AdminOrTeacherOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1/day',
        'user': '2/day',
        'get_student_usr_throttle': '5/day',
        'get_student_anon_throttle': '2/day'
    }
}
```

Last but not least, we should make use of the throttling classes we created inside views of choice.

We are inside students.py file

<img width="374" alt="Screen Shot 2021-11-26 at 8 08 50 PM" src="https://user-images.githubusercontent.com/31994778/143613589-00d30e6c-dbac-49c1-b4f0-45333c650012.png">

```py
...
...
from api.throttling import StudentListUserThrottle, StudentListAnonThrottle


class StudentList(APIView):
    """
    Method: POST,
    Query: Body
       {
        "first_name": "Burakhan",
        "last_name": "Aksoy",
        "age": 26,
        "teacher": 1 (PK of the Teacher)
        }
    """
    authentication_classes = [...]
    permission_classes = [...]
    throttle_classes = [StudentListUserThrottle, StudentListAnonThrottle]
```

And the rest is easy peasy 🏌️

---

<div id="swagger">
 
 <h2>Swagger</h2>
 
 </div>
 
<b> Swagger is a tool for documenting our APIs. It works live redoc. </b>

Giving us a UI like this

<img width="800" alt="Screen Shot 2021-11-27 at 3 29 54 PM" src="https://user-images.githubusercontent.com/31994778/143681367-2c18b146-abdf-4b23-810d-ad69f6f684f4.png">

This UI let's us see what different endpoints are doing in app, what their purposes are and etc.

<h2>Configuration of Swagger</h2>

In order to use Swagger as a documentation for our endpoints, we firstly need to install 

```
drf-yasg==1.20.0
click==8.0.3
```

[drf-yasg](https://pypi.org/project/drf-yasg/) is an open-source project, using coreapi package to provide Swagger UI.

[click](https://pypi.org/project/click/) is a project related to command-line. I am really not very knowledgable on this. 

After installing these two packages, we need to change `INSTALLED_APPS` in settings.py as:

```py
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'drf_yasg',
    ...
]
```

`django.contrib.staticfiles` is needed for static files such as css and etc.

Then, we need to run `python manage.py makemigrations` and later `python manage.py migrate`.

---

<h2>Authentication of Swagger</h2>

As we know, some of our endpoints require authorization and permissions.

In order to handle authentication, we need to add the following snippet to our settings.py

```py
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}
```

This will ask us to insert user token. Let's show it with an example:



https://user-images.githubusercontent.com/31994778/143682720-6acc38ee-137d-414c-b3ce-1a435a2be9bc.mov

Here, when we check the Django admin panel, we see that the teacher is deleted successfully.

<img width="800" alt="Screen Shot 2021-11-27 at 4 10 14 PM" src="https://user-images.githubusercontent.com/31994778/143682738-00086453-502e-4f8c-bff1-a44cc882f33a.png">

For other endpoints that do not require authentication, we can directly make an API call via Swagger.

Lastly, as an important note, we reach to Swagger UI at `http://127.0.0.1:8081/api/swagger/`. Here, port and domain could differ.

---

