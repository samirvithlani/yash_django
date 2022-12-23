from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models.functions import Cast, Coalesce


#orm -->sql query
# Create your views here.
def index(request):
    
    #select * from employee
    #select name from employee
    #employee = Employee.objects.all().values('name','age')
    #select * from employee where id=1
    #employee = Employee.objects.get(id=1)
    #employee = Employee.objects.filter(id=1).values()
    #django lookups
    #employee = Employee.objects.filter(age__gt=20).values()
    #employee = Employee.objects.filter(age__gte=20).values()
    #employee = Employee.objects.filter(age__lt=30).values()
    #employee = Employee.objects.filter(age__lte=30).values()
    #employee = Employee.objects.filter(name__startswith ='a').values()
    #containg
    #employee = Employee.objects.filter(name__contains ='a').values()
    #having a and salry > 20000
    #employee = Employee.objects.filter(name__contains ='a',salary__gt=45000).values()
    #having a or salry > 20000
    #employee = Employee.objects.filter(name__contains ='m').filter(salary__gte=45000).values()
    #query set
    #employee = Employee.objects.filter(Q(name__contains ='m')|Q(salary__gt=45000)).values()
    #employee = Employee.objects.filter(name__istartswith = 'A').values()
    #orderby
    #employee = Employee.objects.filter().order_by('-name').values()
    #employee = Employee.objects.filter(age__gt=25).order_by('name').values()
    #employee = Employee.objects.filter(name__contains ='a').order_by('age').values()
    #desc
    #employee = Employee.objects.order_by(Coalesce('salary','age').desc()).values()
    #employee  = Employee.objects.all().order_by('name','-age').values()
    employee = Employee.objects.all().reverse().values()
    print(employee)
    
    
    return render(request, 'blog/index.html')