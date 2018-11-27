from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    realname=forms.CharField(max_length=30, required=True, help_text='Mandatory.')


    class Meta:
        model = User
        fields = ('username', 'realname','email', 'password1', 'password2', )



class EditProfileForm(UserChangeForm):
    realname=forms.CharField(max_length=30, required=True, help_text='Mandatory.')
    class Meta:
        model=User
        exclude= ()
