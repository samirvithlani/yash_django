from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label='Recipe name', max_length=100)
    ingredients = forms.CharField(label='Ingredients', widget=forms.Textarea)
    instructions = forms.CharField(label='Instructions', widget=forms.Textarea)
