from django.shortcuts import render
from testApp import forms
from testApp.forms import RegistationForm
from testApp.forms import LoginForm

# Create your views here.

def wish_view(request):
    return render(request,"wish.html")

def home_view(request):
    return render(request,'home.html')
def contact_view(request):
    return render(request,"contact.html")
def about_view(request):
    return render(request,"about.html")
def product_view(request):
    items = [
        {"name": "Classic Tee", "price": 19.99, "desc": "100% cotton comfort."},
        {"name": "Running Shoes", "price": 64.95, "desc": "Light and responsive."},
        {"name": "Smart Watch", "price": 129.00, "desc": "Track fitness & notifications."},
        {"name": "Backpack", "price": 39.50, "desc": "Daily carry with padded straps."},
    ]
    return render(request, 'product.html', {'items': items})

def signupform(request):
    form=forms.RegistationForm()
    if request.method=='POST':
        form=forms.RegistationForm(request.POST)
        if form.is_valid():
            print("Form validation is sucess")
            print('UserName:',form.cleaned_data['UserName'])
            print('Password:',form.cleaned_data['Password'])
            print('Email:',form.cleaned_data['Email'])
            print('Gender:',form.cleaned_data['Gender'])
    return render(request,'signup.html',{'form':form})

def loginView(request):
    form=forms.LoginForm()
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            print('Login form is sucess')
            print('UserName:',form.cleaned_data['UserName'])
            print('Password',form.cleaned_data['Password'])
    return render(request,'login.html',{'form':form})


    