from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    real_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, label='Repeat Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'real_name', 'email', 'password1', 'password2',)


class EditProfileForm(UserChangeForm):
    real_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.FileField(required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': '2018-01-30'}))
    country = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('real_name', 'city', 'country', 'phone', 'dob', 'avatar')
