from django.db import models

# Create your models here.
class Animals(models.Model):
    first_name =models.CharField(max_length=64, default=None)
    last_name=models.CharField(max_length=64, default=None)


    def __str__(self):
        return f" firstname : {self.first_name} , last_name:{self.last_name}"
