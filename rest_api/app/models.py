from django.db import models

# Create your models here.

from django.db import models
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    people = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email