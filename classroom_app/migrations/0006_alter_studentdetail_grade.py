# Generated by Django 3.2.6 on 2021-08-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_app', '0005_alter_studentdetail_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='grade',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]