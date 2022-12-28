from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.

def create_student_view(request):
    context = {}
    form = StudentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
    context['form'] = form
    return render(request,"crud/create_student.html",context)    


def student_list_view(request):
    context = {}
    students = Student.objects.all().values()
    context['students'] = students
    return render(request,"crud/student_list.html",context)
    