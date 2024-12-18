from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=4)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)


class DeleteModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=4)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

class CompleteModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=4)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)