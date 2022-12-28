from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.create_student_view,name='create_student'),
    path('list/',views.student_list_view,name='student_list')
    
]
