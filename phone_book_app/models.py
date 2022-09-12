from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField()
    created_date = models.DateTimeField('date published')

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Phone(models.Model):
    PhoneNumber = models.CharField(max_length=200)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)  