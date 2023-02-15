from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Jurado(models.Model):
    jurado = models.ForeignKey(User, on_delete=models.CASCADE)



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Organitation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

class Calification(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    organitation = models.ForeignKey(Organitation, on_delete=models.CASCADE)
    score = models.FloatField()
    timeofcali= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    


