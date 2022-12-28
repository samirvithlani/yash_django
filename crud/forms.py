from django import forms
#model
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =["name","roll","city","email","per","status"]