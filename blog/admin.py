from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)