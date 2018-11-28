from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(attrs={'class':'form-control'}))


    email = forms.EmailField(max_length=254, required=True,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    realname=forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    Password=forms.CharField(max_length=30, required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    Confirm_Password=forms.CharField(max_length=30, required=True,
    widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'realname','email', 'password1', 'password2', )



class EditProfileForm(UserChangeForm):
    realname=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    dob=forms.DateField(widget=forms.DateInput())

    country=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    city=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    phone=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields= ('realname','city','country','phone','dob',)
