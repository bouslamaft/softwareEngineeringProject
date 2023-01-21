from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

def get_expiry():
    return datetime.today() + timedelta(days=15)

class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'

class User(models.Model):
    id=models.PositiveIntegerField()
    name=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    is_staff = models.BooleanField(default="false")

    def __str__(self):
        return str(self.name)+str(self.first_name)+str(self.last_name)+"("+str(self.username)+")"