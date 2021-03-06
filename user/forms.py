from django import forms
from user.models import ProfileModel 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('user', 'status', 'created_on', 'updated_on')

class LoginForm (forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs= {"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs= {"class":"form-control"}))