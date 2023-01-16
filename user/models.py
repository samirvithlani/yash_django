from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#auth_user table -->
class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    
    #meta
class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
class Worker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)    
    