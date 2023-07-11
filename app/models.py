from django.db import models
# Create your models here.
 
class YourModel(models.Model):
    firstname=models.CharField(max_length=64)
    lastname=models.CharField(max_length=64)
    email=models.EmailField()
    