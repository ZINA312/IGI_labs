from django import forms
import re
from main.models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, get_user_model

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'category', 'image', 'price']
        
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Имя пользователя'} ))
    password = forms.CharField(required=True, min_length=8, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Пароль', 'type': 'password'}))
    email = forms.CharField(required=True, min_length=6, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Почта'}))
    phone_number = forms.CharField(required=True, initial="+37529", min_length=13, max_length=13, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Номер телефона'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'\+37529[0-9]{7}', phone_number):
            raise forms.ValidationError('Неправильный номер телефона', code='invalid')
        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'[a-zA-Z@_\-.]+', email):
            raise forms.ValidationError('Неправильная почта', code='invalid')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже существует")
    
        return username
    

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Имя пользователя'} ))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Пароль', 'type': 'password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Неправильное имя пользователя или пароль", code='invalid')
        return cleaned_data
    
class ChangeForm(forms.Form):
    username = forms.CharField(required=False, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Имя пользователя'} ))
    email = forms.CharField(required=False, min_length=6, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Почта'}))
    phone_number = forms.CharField(required=False, initial="+37529", max_length=13, widget=forms.TextInput(attrs={'class': 'def_input', 'placeholder': 'Номер телефона'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number == "+37529":
            return phone_number

        if not re.match(r'\+37529[0-9]{7}', phone_number):
            raise forms.ValidationError('Неправильный номер телефона', code='invalid')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email == "":
            return email
        
        if not re.match(r'[a-zA-Z@_\-.]+', email):
            raise forms.ValidationError('Неправильная почта', code='invalid')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже существует")
    
        return username

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'description', 'photo', 'phone', 'email']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'category', 'image', 'price']
