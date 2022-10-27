from email.policy import default
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class User(models.Model):
    slackUsername = models.CharField(max_length=150)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField(max_length=1000)


    def __str__(self) -> str:
        return f"my slack username is {self.name} my age is {self.age},here is detailed information about me {self.bio}"
