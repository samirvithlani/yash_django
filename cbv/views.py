from django.shortcuts import render
from django.views.generic import ListView
from .models import Contacts
from django.views.generic.edit import CreateView,DeleteView

# Create your views here.
class ContactListView(ListView):
    model = Contacts
    template_name = 'cbv/contact_list.html'
    contacts = Contacts.objects.all().values()
    context_object_name = 'contacts'
    
    
class ContactCreateView(CreateView):
    model = Contacts
    fields = ['name','email','phone','address','city','state','country','pincode']
    template_name = 'cbv/contact_form.html'
    #redicrect
    success_url = '/cbv/contactlist/'
   
class ContactDeleteView(DeleteView):
    model = Contacts
    template_name = 'cbv/contact_delete.html'
    success_url = '/cbv/contactlist/'    
    
  