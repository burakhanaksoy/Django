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
[Writing Views for StudentsDetail](#students-detail-views)
[User Model](#user-model)
[Permissions](#permissions)

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
 
 It is important to see that Views receive HTTP requests and respond with HTTP Responses.
 
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
<h2>OR Queries</h2>
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
<h2>AND Queries</h2>
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
 
 
