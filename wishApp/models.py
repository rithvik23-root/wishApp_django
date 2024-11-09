from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Note: Storing passwords in plain text is insecure.

class Gift(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    gift_name = models.CharField(max_length=200)
