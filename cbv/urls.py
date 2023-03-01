
from django.contrib import admin
from django.urls import path,include
from .views import ContactListView,ContactCreateView,ContactDeleteView,ContactUpdateView,AddImage,getAllImages
from . import views

urlpatterns = [
    path('contactlist/',ContactListView.as_view(),name='contactlist'),
    path('contactcreate/',ContactCreateView.as_view(),name='contactcreate'),
    path('contactdelete/<int:pk>',ContactDeleteView.as_view(),name='contactdelete'),
    path('contactupdate/<int:pk>',ContactUpdateView.as_view(),name='contactupdate'),
    path('addimage/',AddImage.as_view(),name='addimage'),
    path('getimages/',getAllImages.as_view(),name='getimages'),
    path('addrecipe/',views.add_recipe,name='addrecipe')
    
]