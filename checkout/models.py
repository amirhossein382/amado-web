from django.db import models
from common.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name


class Checkout(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='checkouts')
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveBigIntegerField(unique=True)
    phone_number = models.PositiveIntegerField(unique=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
