from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerSignUpForm, WorkeeSignupForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

# Create your views here.
class ManagerSignUpView(CreateView):
    model = User
    form_class =ManagerSignUpForm
    template_name = 'user/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    
    
    def form_valid(self,form):
        user = form.save()
        #seesion
        login(self.request,user)
        return redirect('/crud/list/')

class WorkerSignView(CreateView):
    model = User
    form_class = WorkeeSignupForm
    template_name = 'user/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'worker'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        #seesion
        login(self.request,user)
        return redirect('/crud/list/')
    
    
   
     

  
#worker....    
# class ManagerSignUpView(CreateView):
#     model = User
#     form_class =ManagerSignUpForm
#     template_name = 'user/signup_form.html'
    
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'manager'
#         return super().get_context_data(**kwargs)
    
    
#     def form_valid(self,form):
#         user = form.save()
#         #seesion
#         login(self.request,user)
#         return redirect('/crud/list/')


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
    
    #success url.....
        