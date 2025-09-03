"""
URL configuration for newproject3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish/',views.wish_view,name='wish'),
    path('home/',views.home_view,name='home'),
    path('about/',views.about_view),
    path('contact/',views.contact_view),
    path('product/',views.product_view),
    # path('signUp/',views.signupform),
    # path('Login/', views.loginView),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard_view),
    path('logout/',views.logout_view,name='logout'),
]
