# Generated by Django 3.2.6 on 2021-08-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_app', '0008_alter_studentdetail_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='grade_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]