
from django.contrib import admin
from django.urls import path,include
from .views import ContactListView,ContactCreateView,ContactDeleteView

urlpatterns = [
    path('contactlist/',ContactListView.as_view(),name='contactlist'),
    path('contactcreate/',ContactCreateView.as_view(),name='contactcreate'),
    path('contactdelete/<int:pk>',ContactDeleteView.as_view(),name='contactdelete'),
    
]