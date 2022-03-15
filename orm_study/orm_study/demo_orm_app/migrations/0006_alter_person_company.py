# Generated by Django 3.2.6 on 2022-03-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_orm_app', '0005_alter_person_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to='demo_orm_app.company'),
        ),
    ]