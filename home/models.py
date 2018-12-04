from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    class Meta:
        verbose_name_plural='Posts'

    textArea=models.TextField(max_length=240)
    date_posted=models.DateTimeField(default=timezone.now)
    authour=models.ForeignKey(User,on_delete=models.CASCADE)
