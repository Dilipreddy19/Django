from django.shortcuts import render


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
    items=[
        {"name": "Classic Tee", "price": 19.99, "desc": "100% cotton comfort."},
        {"name": "Running Shoes", "price": 64.95, "desc": "Light and responsive."},
        {"name": "Smart Watch", "price": 129.00, "desc": "Track fitness & notifications."},
        {"name": "Backpack", "price": 39.50, "desc": "Daily carry with padded straps."},
    ]
    return render(request,'wish.html',{'items':items})
