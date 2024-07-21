from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from jazzmin.templatetags.jazzmin import User

from .models import News

import re


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }
        ))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
        ))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }
        ))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
        ))
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
        ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-2'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control mb-2'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise forms.ValidationError('Title should not contain numbers')
        return title
