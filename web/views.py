from django.shortcuts import render
from .models import Flan,ContactForm
from .forms import ContactFormForm, ContactFormModelForm, CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    
    return render(
        request,
        'index.html',
        {
            'public_flans': public_flans,
        }
    )
    
def acerca(request):
    return render(request, 'about.html', {})
    
@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    
    return render(
        request,
        'welcome.html',
        {
            'private_flans': private_flans,
        }
    )

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/exito")
    
    else:
        form = ContactFormModelForm()
    
    return render(request, 'contacto.html',{'form': form})
    
    
    
    

def exito(request):
    return render(request,'success.html',{})

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return HttpResponseRedirect('/registrado')
        data["form"] = formulario
    
    return render(request, 'registration/register.html', data)
            
def registrado(request):
    return render(request,'registrado.html',{})
