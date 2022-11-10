from django.db import models

# Create your models here.

class UsersModel(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField(default='https://reqres.in/img/faces/1-image.jpg')

    def __str__(self):
        return self.email