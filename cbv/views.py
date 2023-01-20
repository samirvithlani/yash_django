from django.shortcuts import render
from django.views.generic import ListView
from .models import Contacts
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import manager_required

# Create your views here.
@method_decorator([login_required(login_url="/user/login"),manager_required],name='dispatch')
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

class ContactUpdateView(UpdateView):
    model = Contacts
    fields ='__all__'
    template_name = 'cbv/contact_Updateform.html'
    success_url = '/cbv/contactlist/'
  