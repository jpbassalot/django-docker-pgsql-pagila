from django.db import models

# Model examples. I'm adding these here to help things get up to speed.
# Most of these are random/contrived examples meant to available field types and other django model features
# https://docs.djangoproject.com/en/4.0/topics/db/models/


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Country(models.Model):
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city


class Address(models.Model):
    # First address line
    address = models.CharField(max_length=50)
    # Optional second address line
    address2 = models.CharField(max_length=50, blank=True)
    # Optional region or province
    district = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
