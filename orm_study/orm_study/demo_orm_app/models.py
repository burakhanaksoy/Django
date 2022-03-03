from django.db import models

# Create your models here.


class Person(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'M'
        female = 'F'

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)

    class Meta:
        unique_together = ('name', 'age') 
