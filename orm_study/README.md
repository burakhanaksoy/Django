<h1>Django Migrations</h1>

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

  <h3>Conclusion</h3>
  
  This concludes your deep dive into Django migrations. Congratulations! You’ve covered quite a lot of advanced topics and now have a solid understanding what happens under the hood of migrations.

You learned that:

- Django keeps track of applied migrations in the Django migrations table.
- Django migrations consist of plain Python files containing a Migration class.
- Django knows which changes to perform from the operations list in the Migration classes.
- Django compares your models to a project state it builds from the migrations.

  ---
  
  <h1>Django ORM</h1>
  
  <p align="center">
    <img width="600" src="https://user-images.githubusercontent.com/31994778/156921120-9d26c81a-dd13-4107-a00b-6d326bc841ac.png">
  </p>
  
  [ref](https://medium.com/@gr8temi/object-relation-mappers-a-beginners-backpack-e5d82e67ffb)
  
  
<b>Table Of Contents</b> |
------------ | 
[Relationships](#relationships)
  
  ---
  
  <div id="relationships">
    <h2>Relationships</h2>
  </div>
  
  <b>Relationships are provided by Django to simplify and smoothly implement connection between different tables.</b>
  
  There are three most used relationship types, these are:
  
  <b>1- Many-to-one Relationship</b>
  
  <b>2- Many-to-many Relationship</b>
  
  <b>3- One-to-one Relationship</b>
  
  Let's start with `Many-to-one`.
  
  <h3>Many-to-one Relationship</h3>
  
  <div align="center">
  <img width="450" src="https://user-images.githubusercontent.com/31994778/156929451-a7387d00-d963-46d0-8c8b-bfed7f3099f1.png">
  </div>
  
  [ref](https://www.jimwritescode.com/the-3-types-of-database-model-relationships-and-how-to-use-them-in-django/)
  
  customer - order relationship would be a great example for many-to-one since each order is owned by one customer, but one customer can have many orders.
  
  Our example would be person - company. A company can have many employees (person), but one person can only work for one company. (legally, I assume :))
  
  <img width="450" alt="Screen Shot 2022-03-06 at 6 24 55 PM" src="https://user-images.githubusercontent.com/31994778/156929829-9bdf298f-0a51-4c26-9d1b-655b526d08c7.png">

  We can fill `Company` and `Person` data through terminal as:
  
  ```py
  company_1 = {"name":"Huawei", "country":"CH", "net_worth_usd":"134.67"}
  company_2 = {"name":"Exxon", "country":"US", "net_worth_usd":"92.91"}
  Company.objects.bulk_create([Company(**company_1), Company(**company_2)])

  Company.objects.all()
  <QuerySet [<Company: Company: Huawei>, <Company: Company: Exxon>]>
  ```
  
  We just used `Model.objects.bulk_create()` to save Companies.
  
  Then, we add user.
  
  ```py
  p1 = {"name":"Burakhan", "age":26, "gender": "M"}
  Person.objects.create(**p1)
  person = Person.objects.get(name__iexact= "burakhan")
  person.company = Company.objects.filter(name='Huawei')[0]
  person.save()
  ```
  
  After adding more persons, Now, our db tables are as follows:
  
  <img width="300" height="150" alt="Screen Shot 2022-03-06 at 7 43 30 PM" src="https://user-images.githubusercontent.com/31994778/156932844-f959e6d2-5ccc-45bb-ba6a-4d389421ed47.png" align="left">
  
<img width="300"  height="150" alt="Screen Shot 2022-03-06 at 7 48 22 PM" src="https://user-images.githubusercontent.com/31994778/156933034-27340bf3-d580-4a2e-88bd-fcaeaf81d26d.png">


  <br clear="left"/>
  
  <h3>Making Queries & Backward Relationship</h3>
  
  Let's say that we want to find all the employees work for a company.
  
  1- Get the related company
  
  2- Get person objects having a foreign key to that company
  
  ```py
  huawei = Company.objects.filter(name__iexact="Huawei").get()
  list(huawei.person.values_list('name', flat=True))
  ['Burakhan', 'Sevde', 'Faruk', 'Ahmet', 'Berna']
  ```
  
  Here, `name__iexact` means `filter Company objects with name = "Huawei" by ignoring case sensitivity`.
  
  Then, we used `huawei.person.values_list()` to find `person` values of `huawei` company.
  
  We can also easily extract the number of employees with `.count()` method.
  
  ```py
  huawei.person.values_list('name', flat=True).count()
  5
  ```
  
  If we want to repeat these steps for `Exxon`, we can just do:
  
  ```py
  exxon = Company.objects.filter(name__iexact="Exxon").get()
  list(exxon.person.values_list('name', flat=True))
  ['Inanc', 'Utku']
  exxon.person.values_list('name', flat=True).count()
  2
  ```
  
  Here, one thing wort mentioning is that even though `Company` model doesn't have `person` field, we can still reach to `person` values with
  `exxon.person`.
  
  This is because `Company` model has a backward relation to `Person` model.
  
  <img width="450" alt="Screen Shot 2022-03-06 at 8 12 18 PM" src="https://user-images.githubusercontent.com/31994778/156934014-e5500ce2-6d18-4eb5-ba6b-1fd1c8ed7e31.png">

  Passing `related_name` is optional, thanks to it's value "person", we can reach Person table from Company table.
  
  If we didn't passed `related_name`, we'd have to use `Exxon.person_set` to reach the Person table, as in:
  
  ```py
  exxon = Company.objects.filter(name="Exxon").get()
  exxon.person_set.all()
  <QuerySet [<Person: Person: Inanc>, <Person: Person: Utku>]>
  exxon.person_set.all().count()
  2
  ```
  
  <b>When passing `related_name`, it's suggested to use related model's name in lowercase.</b>
  
  ---

  <h3>order_by()</h3>
  
  By default, results returned by a QuerySet are ordered by the ordering tuple given by the ordering option in the model’s Meta.
  
  You can override this on a per-QuerySet basis by using the order_by method. [ref](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by)
  
  What happens if we want to sort person table with respect to age field (descending / ascending)?
  
  ```py
  from pprint import pprint
  pprint(list(Person.objects.values('name','age').order_by("age")))
  [{'age': 22, 'name': 'Utku'},
   {'age': 24, 'name': 'Ahmet'},
   {'age': 24, 'name': 'Faruk'},
   {'age': 24, 'name': 'Sevde'},
   {'age': 26, 'name': 'Burakhan'},
   {'age': 33, 'name': 'Berna'},
   {'age': 45, 'name': 'Inanc'}]
  ```
  
  If we want descending order, we put `-` on the ordered field as:
  
  ```py
  pprint(list(Person.objects.values('name','age').order_by("-age")))
  [{'age': 45, 'name': 'Inanc'},
   {'age': 33, 'name': 'Berna'},
   {'age': 26, 'name': 'Burakhan'},
   {'age': 24, 'name': 'Ahmet'},
   {'age': 24, 'name': 'Faruk'},
   {'age': 24, 'name': 'Sevde'},
   {'age': 22, 'name': 'Utku'}]
  ```
  
  We can also order persons related to a company by 
  
  ```py
  huawei = Company.objects.filter(name="Huawei").get()
  pprint(list(huawei.person_set.values('name','age').order_by('age')))
  [{'age': 24, 'name': 'Sevde'},
   {'age': 24, 'name': 'Faruk'},
   {'age': 24, 'name': 'Ahmet'},
   {'age': 26, 'name': 'Burakhan'},
   {'age': 33, 'name': 'Berna'}]
  ```
  
  ---
  
  <h3>gt</h3>
  
  We can select persons whose age greater than `x` with
  
  ```Person.objects.filter(age__gt = x)```
  
  ```py
  Person.objects.filter(age__gt=30)
  <QuerySet [<Person: Person: Berna>, <Person: Person: Inanc>]>
  ```
  
  which can be more readable with
  
  ```py
  Person.objects.filter(age__gt=30).values('name','age')
<QuerySet [{'name': 'Berna', 'age': 33}, {'name': 'Inanc', 'age': 45}]>
```
  
  Like `gt`, we can also use `lt`, `gte`, and `lte`.
  
  Also, it's worth mentioning that `count()` method can be used with any queryset.
  
  ```py
  Person.objects.filter(age__gt=30).count()
  2
  ```
  
  ---
  
  <h3>startswith & istartswith</h3>
  
  Case-sensitive / insensitive starts-with.
  
  ```py
  Person.objects.filter(name__startswith="B").values('name','age')
<QuerySet [{'name': 'Berna', 'age': 33}, {'name': 'Burakhan', 'age': 26}]>
```
  
  ```py
  Person.objects.filter(name__istartswith="i").values('name','age')
<QuerySet [{'name': 'Inanc', 'age': 45}]>
```
  
  ---
  
  <h3>range</h3>
  
  Range can be used to find objects with specified field located in the range between values of range (inclusive).
  
  Let's say that we want to find employees in `Huawei` between 20-26 years of age, inclusive.
  
  ```py
huawei = Company.objects.get(name="Huawei")
huawei.person_set.filter(age__range=(20,26))
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Sevde>, <Person: Person: Faruk>, <Person: Person: Ahmet>]>
```
  
  <img width="450" alt="Screen Shot 2022-03-10 at 9 16 18 PM" src="https://user-images.githubusercontent.com/31994778/157728667-c28b00ef-cc22-415c-aa67-da0ae795090f.png">
  
  This can also be done by querying `Person` objects directly, as:
  
  ```py
  Person.objects.filter(age__range=(20,26),company__name__iexact='huawei')
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Sevde>, <Person: Person: Faruk>, <Person: Person: Ahmet>]>
```

  ---
  
  <h3>Chaining Queries</h3>
  
  Since filter operation returns a `queryset`, and queryset has attribute `filter`, we can chain queries by using `filter()` method.
  
  ```py
  some_queryset = huawei.person_set.filter(age__gt=20)
hasattr(some_queryset,'filter')
True
```
  
  since hasattr(some_queryset,'filter') returns True, we can chain many queries together.
  
  ```py
  huawei.person_set.filter(gender__iexact="M").filter(age__gt=20)
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Faruk>, <Person: Person: Ahmet>]>
```
  
  In this sense, chaining in Django ORM works very similar to `aggregation pipeline` in `MongoDB`.
  
  For example:
  
  ```py
  huawei.person_set.filter(age__lt=30).filter(age__gt=25)
<QuerySet [<Person: Person: Burakhan>]>
```
  
  <b>Chaining filters and filtering with multiple kwargs works as and `AND` condition for the most of the time, however, for `ManytoMany` relationships and `reverse foreign key search` Chaining filters works as `OR` and filtering with multiple kwargs works as `AND`.</b>
  
  <img width="343" alt="Screen Shot 2022-03-10 at 10 12 51 PM" src="https://user-images.githubusercontent.com/31994778/157737882-d1cd5d93-99c6-4273-8137-261b9aa93690.png">

  Here, filtering with multiple kwargs acts as an `AND` condition:
  
  ```py
  Company.objects.filter(person__gender="M" , person__age__gt=25)
<QuerySet [<Company: Company: Huawei>, <Company: Company: Exxon>]>
```
  
  
  However, chaining filters acts as an `OR` condition:
  
  ```py
  Company.objects.filter(person__gender="M" ).filter(person__age__gt=25)
<QuerySet [<Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Exxon>, <Company: Company: Exxon>]>
  ```
  
  If we hadn't used a reverse foreign key here, then both multiple kwargs and chain filters would have acted as `AND` condition:
  
  ```py
  Person.objects.filter(gender="M", age__gt=25)
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Inanc>]>
Person.objects.filter(gender="M" ).filter(age__gt=25)
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Inanc>]>
```
  
  [ref](https://stackoverflow.com/questions/5542874/difference-between-filter-with-multiple-arguments-and-chain-filter-in-django)
  
  ---
  
  <h3>isnull</h3>
  
  Takes either True or False, which correspond to SQL queries of IS NULL and IS NOT NULL, respectively. [ref](https://docs.djangoproject.com/en/4.0/ref/models/querysets/)
  
  For example, create a person with `company` not assigned, in other words, `NULL`.
  
  ```py
  person = {"name":"Cevdet", "age":18, "gender":"M"}
Person.objects.create(**person)
Person: Cevdet
```
  
  <img width="280" alt="Screen Shot 2022-03-10 at 10 29 27 PM" src="https://user-images.githubusercontent.com/31994778/157740044-1ee3f90b-89f1-4657-96dd-10a5809e2741.png">
  
  Then,
  
  ```py
  Person.objects.filter(company__isnull=True)
<QuerySet [<Person: Person: Cevdet>]>
```
  
  ```py
  Person.objects.filter(company__isnull=False)
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Sevde>, <Person: Person: Faruk>, <Person: Person: Ahmet>, <Person: Person: Berna>, <Person: Person: Inanc>, <Person: Person: Utku>]>
  ```
  
  ---
  
  <h3>regex</h3>
  
  Used for pattern matching. Recommended to use with `r`(raw) strings.
  
  ```py
  Person.objects.filter(name__regex=r"(et)$")
<QuerySet [<Person: Person: Ahmet>, <Person: Person: Cevdet>]>
```
  
  `field__iregex` is used for case insensitive regex matching.
  
  ```py
  Person.objects.filter(name__regex=r"A")
<QuerySet [<Person: Person: Ahmet>]>
Person.objects.filter(name__iregex=r"A")
<QuerySet [<Person: Person: Burakhan>, <Person: Person: Faruk>, <Person: Person: Ahmet>, <Person: Person: Berna>, <Person: Person: Inanc>]>
```
  
  <h3>distinct()</h3>
  
  <img width="800" alt="Screen Shot 2022-03-15 at 7 10 17 PM" src="https://user-images.githubusercontent.com/31994778/158421851-012d8ee7-62f6-4558-9119-05c8315e2b27.png">

  For example, when we make the following query:
  
  ```py
  Company.objects.filter(person__gender = "M")
<QuerySet [<Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Huawei>, <Company: Company: Exxon>, <Company: Company: Exxon>]>
```
  
  Here, we only want companies that have `person` whose gender is male, since this is a backward foreign key relation, result has repeated objects, which is not very meaningful. Instead, we can use `distinct()` to find out the companies without repetition.
  
  ```py
  Company.objects.filter(person__gender = "M").distinct()
<QuerySet [<Company: Company: Huawei>, <Company: Company: Exxon>]>
```
  
  Now, we know that both companies `Huawei` and `Exxon` have employees whose gender is male.
  
  ---
  
  <h3>Many-to-many Relationship</h3>
  
  

    


  
  
  
  
  
