from django.shortcuts import render,HttpResponseRedirect
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
    print("hello")
    context = {}
    students = Student.objects.all().values()
    context['students'] = students
    return render(request,"crud/student_list.html",context)


def student_list_sort(request):

    print("sort")
    context ={}
    student = Student.objects.all().order_by('-roll').values()
    context['students'] = student
    return render(request,"crud/student_list.html",context)
    
        
def student_delete_view(request,id):
    context = {}
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect('/crud/list/')
    return render(request,"crud/student_delete.html",context)    

def student_detail_view(request,id):
    context = {}
    student = Student.objects.get(id=id)
    context['student'] = student
    return render(request,"crud/student_detail.html",context)

def student_update_view(request,id):
    context = {}
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/crud/list/')
    
    context['form'] = form
    return render(request,"crud/update_student.html",context)