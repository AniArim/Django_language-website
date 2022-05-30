from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

from .models import *


class AddLanguagePost(forms.ModelForm):
    #captcha = CaptchaField(label='Проверка', widget=CaptchaTextInput(attrs=({'class': 'captcha', 'id': 'id_captcha'})))

    class Meta:
        model = Language
        fields = ['title', 'icon', 'content', 'subcategories']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название языка:'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'data'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com', 'form-text': 'Мы никогда никому не передадим вашу электронную почту.'}))
    first_name = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control-sm'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control-sm'}))
    captcha = CaptchaField(label='Проверка', widget=CaptchaTextInput(attrs=({'class': 'captcha', 'id': 'id_captcha'})))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control-sm'}))

