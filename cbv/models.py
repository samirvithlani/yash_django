from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'contacts'


class AddPhoto(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'addPhoto'
    
   