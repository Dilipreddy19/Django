from django.shortcuts import render,redirect
from testApp import forms
from django.http import HttpResponse
# from testApp.forms import RegistationForm
# from testApp.forms import LoginForm
from testApp.forms import RegistrationForm

from testApp.forms import loginForm
from django.contrib.auth import authenticate,login,logout


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

# def signupform(request):
#     form=forms.RegistationForm()
#     if request.method=='POST':
#         form=forms.RegistationForm(request.POST)
#         if form.is_valid():
#             print("Form validation is sucess")
#             print('UserName:',form.cleaned_data['UserName'])
#             print('Password:',form.cleaned_data['Password'])
#             print('Email:',form.cleaned_data['Email'])
#             print('Gender:',form.cleaned_data['Gender'])   
#     return render(request,'signup.html',{'form':form})

# def loginView(request):
#     form=forms.LoginForm()
#     if request.method=='POST':
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             print('Login form is sucess')
#             print('UserName:',form.cleaned_data['UserName'])
#             print('Password',form.cleaned_data['Password'])
            
#     return render(request,'login.html',{'form':form})

def register_view(request):
     form= RegistrationForm()
     if request.method=="POST":
            form=RegistrationForm(request.POST)
            if form.is_valid():
                user=form.save()
                # response= redirect('login')
                return redirect("login")
                # response.set_cookie("username",user.username,max_age=3600)
                # return response
     return render(request,"signup.html",{'form':form})
    
def login_view(request):
    form=loginForm()
    if request.method=="POST":
         form=loginForm(request.POST)
         if form.is_valid():
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                #   response= redirect("dashboard")
                #   response.set_cookie("username",user.username,max_age=3600)
                #   response.set_cookie("last_login",str(user.last_login),max_age=3600)
                #   return response
                request.session["username"]=user.username
                request.session["last_login"]=str(user.last_login)
                return redirect("dashboard")
            #   return HttpResponse("invalid Credentials")
    else:
        return render(request,"login.html",{"form":form,"error":"Invalid Credentials"})
    return render(request,"login.html",{'form':form})
     
def logout_view(request):
     logout(request)
     return redirect("login")
def dashboard_view(request):
    username=request.session.get("username")
    last_login=request.session.get("last_login")
    return render(request,"dashboard.html",{"username":username,"last_login":last_login})
    