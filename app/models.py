from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Gift(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='gifts')
    gift_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.gift_name} (User: {self.user.username})"
