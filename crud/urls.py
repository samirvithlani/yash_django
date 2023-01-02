from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.create_student_view,name='create_student'),
    path('list/',views.student_list_view,name='student_list'),
    path('listsort/',views.student_list_sort,name='student_sort'),
    path('delete/<int:id>',views.student_delete_view,name='student_delete'),
    path('detail/<int:id>',views.student_detail_view,name='student_detail'),
    path('update/<int:id>',views.student_update_view,name='student_update')
    
    
]
