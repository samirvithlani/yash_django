from django.shortcuts import render
from django.views.generic import ListView
from .models import Contacts,AddPhoto
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from user.decorators import manager_required
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from .models import Product2
from django.http import JsonResponse
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler



# Create your views here.
# @method_decorator([login_required(login_url="/user/login"),manager_required],name='dispatch')
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
    
    def form_valid(self, form):
        # Modify the form data here
        form.instance.user = self.request.user
        form.instance.name = form.cleaned_data['name'].upper()
        # Call the parent form_valid() method to save the object to the database
        return super().form_valid(form)


def create_order(product):
     # code to create order goes here
     print("here......",product)
    # try:
    #     # code to send order to API goes here
    #     print(f'Order placed for product {product.name}')
    # except Exception as e:
    #     print(f'Error placing order for product {product.name}: {e}')


def check_quantity(request, product_id):
    product = get_object_or_404(Product2, id=product_id)
    if product.quantity < 0:
        create_order(product)
        return JsonResponse({'status': 'Order placed'})
    else:
        return JsonResponse({'status': 'Quantity is sufficient'})

        
    success_url = '/cbv/contactlist/'
   
class ContactDeleteView(DeleteView):
    model = Contacts
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/cbv/contactlist/'    

class ContactUpdateView(UpdateView):
    model = Contacts
    fields ='__all__'
    template_name = 'cbv/contact_Updateform.html'
    success_url = '/cbv/contactlist/'
  
class AddImage(CreateView):
    model = AddPhoto
    fields = '__all__'  
    success_url = '/cbv/contactlist/'
    template_name = 'cbv/add_image.html'
    
class getAllImages(ListView):
    model = AddPhoto
    context_object_name = 'images'
    template_name = 'cbv/get_all_images.html'

from .forms import RecipeForm

def add_recipe(request):
    RecipeFormSet = formset_factory(RecipeForm, extra=1)

    if request.method == 'POST':
        formset = RecipeFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                ingredients = form.cleaned_data.get('ingredients')
                instructions = form.cleaned_data.get('instructions')
                # Do something with the form data
                #save to db
                print(name,ingredients,instructions)
                
    else:
        formset = RecipeFormSet()

    return render(request, 'add_recipe.html', {'formset': formset})        

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

@scheduler.scheduled_job(trigger='interval', minutes=2)
def check_all_products():
    products = Product2.objects.all()
    print("here........***")
    for product in products:
        if product.quantity < 0:
            create_order("called....")

scheduler.start()
