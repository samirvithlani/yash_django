from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    per = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'
