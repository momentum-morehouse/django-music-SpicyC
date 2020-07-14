from django.db import models
#from django.contrib.auth.models
# import AbstractUser
# Create your models here.



class Album(models.Model):
    artistname = models.CharField(max_length=255)
    albumtitle = models.CharField(max_length=255)
    released = models.DateField()

    def __str__(self):
        return f"{self.albumtitle} by {self.artistname}"
        return f"{self.released}"

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#     pass
