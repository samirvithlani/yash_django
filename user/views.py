from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerSignUpForm, WorkeeSignupForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

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
        #get email if form valid
        email = form.cleaned_data.get('email')
        print(email)
        res = sendMail(email)
        if res>0:
            login(self.request,user)
            
        return redirect('/crud/list/')
    

class WorkerSignView(CreateView):
    model = User
    form_class = WorkeeSignupForm
    template_name = 'user/signup_form.html'
    
    
    
    def get_context_data(self, **kwargs):
        #get emal from request
        email = self.request.POST.get('email')
        print(email)
        kwargs['user_type'] = 'worker'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        #seesion
        
        login(self.request,user)
            
        return redirect('/crud/list/')
    

def sendMail(mailid):
    subject = 'Welcome to our site'
    message = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject,message,email_from,recipient_list)
    print(res)
    return res
   
     

  
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
        