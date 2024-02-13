from django.db import models

class User(models.Model):
  name = models.CharField(max_length=20)
  location = models.CharField(max_length=30)
  profile_photo = models.TextField()
  description = models.TextField(max_length=500)