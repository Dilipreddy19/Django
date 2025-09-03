from django import forms
# from django.core import validators 
# from testApp.models import Registation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# class RegistationForm(forms.Form):
#     UserName=forms.CharField(max_length=25)
#     Password=forms.CharField(widget=forms.PasswordInput())
#     Email=forms.EmailField(max_length=30)
#     Gender_choices=[
#         ('male','Male'),
#         ('Female','Female'),
#         ('Others','Others')
#     ]
#     Gender=forms.ChoiceField(choices=Gender_choices,widget=forms.RadioSelect)
# class LoginForm(forms.Form):
#     UserName=forms.CharField(max_length=30)
#     Password=forms.CharField(widget=forms.PasswordInput())

# def clean_UserName(self):
#     print("Validating Username")
#     inputname=self.cleaned_data['UserName']
#     if len(inputname)<4:
#         raise forms.ValidationError("the minimum no of characterin the name field should be >4")
#     return inputname
# def clean_Password(self):
#     print("validating password")
#     inputpassword=self.cleaned_data['Password']
#     if len(inputpassword)<8:
#         raise forms.ValidationError("The password must be atleast 8 characters above ")
#     if not inputpassword.search(r"[A-Z]",inputpassword):
#      raise forms.ValidationError("Atleat one charcter should uperCase")
#     if not inputpassword.search(r"[a-z]",inputpassword):
#         raise forms.ValidationError("Atleat one charcter should Lowercase")
#     if not inputpassword.search(r"\d", inputpassword):
#         raise forms.ValidationError("Atleat one charcter should be Digit")
#     if not inputpassword.search(r"[@$!%*?&#]",inputpassword):
#         raise forms.ValidationError("password must contain at least one special character")
#     return inputpassword
# def cleaned_Email(self):
#     print("Validating Email")
#     inputEmail=self.cleaned_data['Email']
#     if not inputEmail.endswith("@gmail.com"):
#         raise forms.ValidationError('Gmail address must follow')
#     return inputEmail
# def cleaned_Gender(self):
#     print("Validating gender")
#     inputGender=self.cleaned_data["Gender"]
#     if inputGender not in ['Male','Female','Others']:
#         raise forms.ValidationError("Invalid gender section")
#     return inputGender
# class Registation(forms.ModelForm):
#     class Meta:
#      model=Registation
#      fields='__all__'

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model= User
        fields=['username','email','password1','password2']
        # fields="__all__"
        help_texts={
            "username":None,
            "email":None,
            "Password1":None,
            "Password2":None,
        }
        

class loginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())