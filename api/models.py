from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid
from datetime import date






class User(AbstractUser):
    LEVEL_CHOICES = [
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinium', 'Platinium'),
        ('Tithanium', 'Tithanium')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number", unique=True)
    password = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)
    membership = models.CharField(max_length=100, choices=LEVEL_CHOICES, default="Silver")
    spending = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    price = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name


class UsedList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.ManyToManyField(get_user_model(), null=True, blank=True)
    services = models.ManyToManyField('Services', null=True, blank=True)


    def __str__(self):
        return f"{self.users.all()} ({', '.join([str(service) for service in self.services.all()])})"