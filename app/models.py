from django.db import models  # type: ignore

class Users(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(unique=True, max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)


