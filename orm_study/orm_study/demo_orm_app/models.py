from django.db import models

from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
# Create your models here.


class Company(models.Model):
    COUNTRIES = (
        ('US', 'United States'),
        ('CH', 'China'),
        ('UK', 'United Kingdom'),
        ('IR', 'Ireland'),
        ('GER', 'Germany'),
        ('TR', 'Turkey')
    )

    name = models.CharField(max_length=100, primary_key=True)
    country = models.CharField(max_length=3, choices=COUNTRIES)
    net_worth_usd = models.DecimalField(max_digits=7, decimal_places=2,
                                        validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f'Company: {self.name}'


class Person(models.Model):
    GENDERS = (
        ('M', 'male'),
        ('F', 'female')
    )

    name = models.CharField(max_length=45)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)])
    gender = models.CharField(max_length=1, choices=GENDERS)
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        unique_together = ('name', 'age')

    def __str__(self) -> str:
        return f'Person: {self.name}'
