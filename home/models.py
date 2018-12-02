from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.street}"
