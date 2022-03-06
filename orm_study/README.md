<h1>Django ORM</h1>

<p align="center">
<img width="600px" src="https://user-images.githubusercontent.com/31994778/156621497-70d7aa7f-3183-4e15-b91c-26cd191ec83b.png">

  [ref](https://swapps.com/blog/quick-start-with-django-orm/)
 </p>
 
 <b><i>"Django ORM is a wrapper for SQL, enabling developers to use Python language for SQL queries."</i></b>
 
 ---
 
<b>Table Of Contents</b> |
------------ | 
[Introduction migrations](#intro-to-migrations)
[Creating our model](#creating-our-model)
[Inserting our first data](#inserting-data)

---

<div id="intro-to-migrations">
  <h2>Introduction to Migrations</h2>
  </div>
  
<b>Migrations are the tools for creating and modifying database tables without having to learn SQL language.</b>[ref](https://realpython.com/lessons/what-django-migrations-and-problems-they-solve/)

All database systems supported by Django use SQL to handle CRUD operations in a relational db.

Django orm(object relational mapper) is a mapper that maps Python objects (models) to SQL tables. Using Django orm, we don't have to use SQL to create database tables.

Here, we have a model `PriceHistory` and it's fields mapped to db as a table and it's columns.

<img width="600px" src="https://user-images.githubusercontent.com/31994778/156626713-c5c05367-7e50-48c1-bf79-ba3c3444b99f.png">

>But just defining a model class in a Python file does not make a database table magically appear out of nowhere. Creating the database tables to store your Django models is the job of a database migration. Additionally, whenever you make a change to your models, like adding a field, the database has to be changed too. Migrations handle that as well. [ref](https://realpython.com/django-migrations-a-primer/#the-problems-that-migrations-solve)

Here are a few ways Django migrations make your life easier.

<h3>Making database changes without SQL</h3>

In traditional SQL, if you want to make changes on your db tables, you'd have to write more SQL codes. (This is what I've read on the internet, not that I know SQL :)) However, with migrations, you can easily change your db models with plain Python coding. We only have to run `python manage.py makemigrations` to make database changes effective.

<b>We can also run `makemigrations` and `migrate` for a specific app as:</b>

`python3 manage.py makemigrations demo_orm_app`

`python3 manage.py migrate demo_orm_app`

When created, the database tables can be check through `dbshell` as:

```py
$ python3 manage.py dbshell
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  demo_orm_app_person       
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions
```
If we do these only for a specific app, though,

```py
sqlite> .tables
demo_orm_app_person  django_migrations
```

<b>Here, `demo_orm_app_person` is the table that we created with our `Person` model.</b>

We can get more info about the table we want through `.schema --indent <table name>`.

<img width="450" alt="Screen Shot 2022-03-05 at 11 59 25 AM" src="https://user-images.githubusercontent.com/31994778/156876494-9b70a0ea-3af2-4784-8b8c-8b6d4c92afe7.png">

`--indent` is used to format output nicely.

In order to display migrations of other apps, we can do `python3 manage.py showmigrations`

<img width="450" alt="Screen Shot 2022-03-05 at 12 40 46 PM" src="https://user-images.githubusercontent.com/31994778/156877844-6c7e0469-953e-4850-9f5f-0dc602415b56.png">

<div id="unapplying-migrations">
  <h3>Unapplying migrations</h3>
  
  We might want to revert a migration in these cases: [ref](https://realpython.com/django-migrations-a-primer/#the-problems-that-migrations-solve)
  
  - Want to test a migration a colleague wrote
  - Realize that a change you made was a bad idea
  - Work on multiple features with different database changes in parallel
  - Want to restore a backup that was created when the database still had an older schema
  
  >To unapply a migration, you have to call migrate with the name of the app and the name of the migration before the migration you want to unapply.
  
  Imagine we have such a migration `0001_initial.py`
  
  <img width="450" alt="Screen Shot 2022-03-05 at 1 34 19 PM" src="https://user-images.githubusercontent.com/31994778/156879653-5d51a944-d6c3-4f87-9cdd-dc90b2c314b2.png">

  We add a new field `some_field`, provide one-off default and migrate.
  Now we have another migration file `0002_person_some_field.py`.
  
  <img width="450" alt="Screen Shot 2022-03-05 at 1 40 49 PM" src="https://user-images.githubusercontent.com/31994778/156881284-e0c8f881-f754-4f23-8443-2850b2f5b60a.png">

  Then, we want to revert the last migration and go back to `0001_initial`.
  
  `python3 manage.py migrate demo_orm_app 0001`
  
  ```py
  $ python3 manage.py migrate demo_orm_app 0001
  Operations to perform:
    Target specific migration: 0001_initial, from demo_orm_app
  Running migrations:
    Rendering model states... DONE
    Unapplying demo_orm_app.0002_person_some_field... OK
  ```
  
  After reverting the migration, we will see that `some_field` column is removed from db tables.
  
  <img width="450" alt="Screen Shot 2022-03-05 at 2 38 44 PM" src="https://user-images.githubusercontent.com/31994778/156881412-3b817c4e-98d6-4575-9926-cff496be97b9.png">

  
  <b>It is wort noting that when we make migrations again, this wil re-apply reverted migrations, because we are not removing `.py` files.</b>
  
  </div>
  
<h3>Naming migrations</h3>

Normally, Django names migrations automatically, reflecting change happened in the model.
Here are our migration files for `demo_orm_app` app.

<img width="450" alt="Screen Shot 2022-03-05 at 2 54 34 PM" src="https://user-images.githubusercontent.com/31994778/156881901-76ceeed3-624a-4b24-836e-1d41eea51e02.png">

If we want, we can name our migrations with `python manage.py makemigrations <app name> --name <given name>`.

<img width="450" alt="Screen Shot 2022-03-05 at 2 58 52 PM" src="https://user-images.githubusercontent.com/31994778/156882530-49071431-b2b4-4809-9ecc-76ef51fba7bf.png">


<h3>makemigrations vs migrate</h3>

These two commands can be easily mixed up. To clarify, we can say that:

- `makemigrations` will look for changes in models.py, if there's a change, it will apply, if not it will say `No changes detected`.
- `migrate` will implement migration. 

These can be shown as follows:

<img width="450" alt="Screen Shot 2022-03-05 at 11 43 45 AM" src="https://user-images.githubusercontent.com/31994778/156875808-f92878cf-40a8-4585-bd7d-1a0ecc3673f3.png">

---

<div id="creating-our-model">
  <h2>Creating our model</h2>
  </div>
  
 Let's have `Person` model(table).
 
 ```py
 class Person(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'M'
        female = 'F'

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    
    class Meta:
        unique_together = ('name', 'age') 
 ```
 
 After we make our migrations by `python manage.py makemigrations`, we will have a python file `0001_initial.py` like this.
 
 ```py
 # Generated by Django 3.2.6 on 2022-03-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
```

The more changes (and migrations after) we make, the more `*?_initial.py` files we would have. For the second migration we make, we'll have 0002_foo_bar.py...

For example, we added `unique_together` to `name` and `age` fields and makemigrations again. We will have the following .py file.

<img width="333" alt="Screen Shot 2022-03-03 at 11 09 47 PM" src="https://user-images.githubusercontent.com/31994778/156644801-ddd401f8-8e1a-4f02-84f0-2ba44a55c6b8.png">

<b>Here, important thing to notice is that every subsequent migration creates a new python file and they stack. (By stack, we mean that each subsequent file inherit from the previous migration's .py file)</b>

---

<div id="inserting-data">
<h2>Inserting our first data</h2>
  </div>
  
  Making migrations are just a way of creating tables and schema for our database. We can create real data through django's views and serializers.
  
  Here, we create a serializer in accordance with our Person model.
  
  <img width="442" alt="Screen Shot 2022-03-05 at 11 09 19 AM" src="https://user-images.githubusercontent.com/31994778/156874741-2c9d4139-2c21-4e68-8a5d-ad1e74c04f05.png">

  This means that we will validate `name`, `age`, and `gender` fields.
  
  Also, we need to have an API (view file), helping us persist data in database.
  
  <img width="450" alt="Screen Shot 2022-03-05 at 11 10 46 AM" src="https://user-images.githubusercontent.com/31994778/156874856-6dbebd4a-9113-4c82-9de3-8f90201d6407.png">

  Sending data through our endpoint, `demo_orm/user/create/`, 
  
  We have data in our database as follows:
  
  <img width="450" alt="Screen Shot 2022-03-05 at 11 17 32 AM" src="https://user-images.githubusercontent.com/31994778/156875002-c9a1a03b-13ef-416f-a3ce-953a3df888f4.png">

<b>It's important that we have a serializer, which let's us return 400 immediately if sent data is incompatible with data we expect</b>.

For example, if we send `age` less than zero,
  
<img width="450" alt="Screen Shot 2022-03-05 at 11 26 42 AM" src="https://user-images.githubusercontent.com/31994778/156875267-9079414a-0234-4881-b54f-c42e0b4e6c15.png">

---

<h1>Digging Deeper Into Django Migrations</h1>

<p align="center">
<img width="600" src="https://user-images.githubusercontent.com/31994778/156883375-56a0099f-1a5e-4aa5-8029-a42fce2e5893.png">
  
  [ref](https://realpython.com/digging-deeper-into-migrations/)
</p>

<b>Table Of Contents</b> |
------------ | 
[How Django Knows Which Migrations to Apply](#how-does-django-know-which-migration-to-apply)
[The Migration File](#the-migration-file)

By the end of this article, you’ll know:

- How Django keeps track of migrations
- How migrations know which database operations to perform
- How dependencies between migrations are defined

<div id="how-does-django-know-which-migration-to-apply">
<h2>How Django Knows Which Migrations to Apply</h2>
  </div>
  
  The first time we run `python manage.py migrate <app_name>` command, django creates `django_migrations` table in the database and writes each migration it ran as a record.
  
<div>

<img width="383" alt="Screen Shot 2022-03-05 at 4 09 05 PM" src="https://user-images.githubusercontent.com/31994778/156884527-e4d9f593-6410-44aa-ab1f-1f702edfa6a8.png">
  
<img width="450" alt="Screen Shot 2022-03-05 at 4 09 35 PM" src="https://user-images.githubusercontent.com/31994778/156884539-bddbb28c-5cff-4fd5-99aa-991a260379d1.png">
  
  </div>
  
<b>  If there's a migration file except for these, Django will run and apply that, however, migration files that are already in `django_migrations` table as a record won't be run with subsequent migrations.</b>
  
  >The next time migrations are run, Django will skip the migrations listed in the database table. This means that, even if you manually change the file of a migration that has already been applied, Django will ignore these changes, as long as there’s already an entry for it in the database.

[ref](https://realpython.com/digging-deeper-into-migrations/)

---

<div id="the-migration-file">
<h2>The Migration File</h2>
</div>

>What happens when you run python manage.py makemigrations <appname>? Django looks for changes made to the models in your app <appname>. If it finds any, like a model that has been added, then it creates a migration file in the migrations subdirectory. This migration file contains a list of operations to bring your database schema in sync with your model definition.
  
  <img width="450" alt="Screen Shot 2022-03-05 at 5 14 18 PM" src="https://user-images.githubusercontent.com/31994778/156887066-7420d7bb-9746-4994-881b-baf134e649ff.png">

  Let's take a closer look at the migration file `0001_initial.py`.
  
```py
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'unique_together': {('name', 'age')},
            },
        ),
    ]
```
 
The Migration class contains two main lists:

  <b>1 - dependencies</b>
  
  <b>2 - operations</b>
  
  <h3>Migration Operations</h3>
  
  Let's talk about `operations` list first.
  Operations list will contain the operations to be performed as part of the migration. 
  Operations are subclasses of the class django.db.migrations.operations.base.Operation. 
  Here are the common operations that are built into Django:
  
<img src="https://user-images.githubusercontent.com/31994778/156892711-11c6efb5-d7b6-4303-b381-7a337800257c.png" align="left" width="450"/>
  <b>Operations are subclasses of the class django.db.migrations.operations.base.Operation. Here are the common operations that are built into Django:</b>

<br clear="left"/>
  
  <h3>Migration Dependencies</h3>
  
  Dependencies list holds relationships of different migrations with each other. In `initial.py` migration file, dependencies = [ ] will be an empty list because this is the very first migration file and does not depend on any other.
  
  On the other hand, when we change anything in the model and re-migrate, we will have 0002 migration file.
  
  <img width="450" alt="Screen Shot 2022-03-05 at 8 30 25 PM" src="https://user-images.githubusercontent.com/31994778/156893904-1ccfa31f-9d78-4fc1-b9d7-6527ec8f8d10.png">

  This makes sense because in order to make a change in the db table, you need to wait for the creation of the db table.
  
  A migration can also have a dependency on a migration of another app, such as:
  
  <img width="450" alt="Screen Shot 2022-03-05 at 8 36 27 PM" src="https://user-images.githubusercontent.com/31994778/156894073-5513b593-0ef0-4984-bc77-bfc5007ddfc3.png">

  <b>run_before</b>:
  
  <img width="450" alt="Screen Shot 2022-03-05 at 8 38 35 PM" src="https://user-images.githubusercontent.com/31994778/156894162-7e7f5652-6539-4aaf-b05a-69b523685b8d.png">

  Dependencies can also be combined so you can have multiple dependencies. This functionality provides a lot of flexibility, as you can accommodate foreign keys that depend upon models from different apps.

The option to explicitly define dependencies between migrations also means that the numbering of the migrations (usually 0001, 0002, 0003, …) doesn’t strictly represent the order in which migrations are applied. You can add any dependency you want and thus control the order without having to re-number all the migrations.
  
  <h3>Viewing the Migration</h3>
  
  If you want to view what SQL code your migration will implement beforehand, you can run
  
  `python manage.py sqlmigrate <app_name> <migration_file>`.
  
  For example:
  
  <img width="450" alt="Screen Shot 2022-03-06 at 1 22 20 PM" src="https://user-images.githubusercontent.com/31994778/156919280-32369c3e-d79c-4e1c-a4ca-4dce6db2715c.png">
  
  
 When you pass the parameter --backwards, Django generates the SQL to unapply the migration:

<img width="450" alt="Screen Shot 2022-03-06 at 1 34 28 PM" src="https://user-images.githubusercontent.com/31994778/156919422-7f591cbd-fe3b-42c1-a4fd-67f8c30000ff.png">
