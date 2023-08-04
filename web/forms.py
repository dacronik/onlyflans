from django import forms
from django.forms import ModelForm
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactFormForm(forms.Form):
    # contact_form_uuid No necesita ser declarado en nuestro form
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    subject = forms.CharField(max_length=32, label="Asunto")
    message = forms.CharField(label='Mensaje')
    
class ContactFormModelForm(forms.ModelForm):
    
    class Meta:
        model = ContactForm
        fields = ["customer_email","customer_name","subject","message"]
        labels = {"customer_email":'Email Cliente',"customer_name":"Nombre Cliente","subject":"Asunto","message":"Mensaje"}
        

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')