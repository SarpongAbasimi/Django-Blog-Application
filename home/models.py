from django.db import models

# Create your models here.
class Animals(models.Model):
    def __init__(self,first_name,last_name):
        self.first_name =models.charField(max_length=64)
        self.last_name=models.charField(max_length=64)

    def get_firstName(self):
        return self.first_name

    def get_lastName(self):
        return self.last_name

    def __str__(self):
        return f" firstname : {self.first_name} , last_name:{self.last_name} "
