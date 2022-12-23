from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    
    class Meta:
        db_table = 'employee'
        
    def __str__(self):
        return self.name    
        
#one to one
class Post(Employee):
    title = models.CharField(max_length=100)
    words = models.IntegerField()
    
    class Meta:
        db_table = 'post'
        
    def __str__(self):
        return self.title

#one many one author can have many books
bookChoice =(('fiction','Fiction'),('non-fiction','non-Fiction'),('biography','Biography'),('poetry','Poetry'))

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    class Meta:
        db_table = 'author'
        
    def __str__(self):
        return self.name
                   
class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,choices=bookChoice)
    price = models.FloatField()
    copy = models.IntegerField()
    
    class Meta:
        db_table = 'book'
        
    def __str__(self):
        return self.name   
    
class Category(models.Model): 
    cname = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'category'
        
    def __str__(self) :
        return self.cname      
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'product'
        
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    product = models.ManyToManyField(Product)        
    cartName = models.CharField(max_length=100)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cart'
        
    def __str__(self):
        return self.cartName    
      
    
         
                       