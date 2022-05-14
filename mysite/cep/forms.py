from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contact, MyUser


# Create your forms here.

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'name':'email','placeholder':'Email Address','type':'email'})
        self.fields['username'].widget.attrs.update({'name':'username','placeholder':'Username','type':'text'})
        self.fields['password1'].widget.attrs.update({'name':'password1','placeholder':'Password','type':'password'})
        self.fields['password2'].widget.attrs.update({'name':'password2','placeholder':'Confirm Password','type':'password'})
        self.fields['first_name'].widget.attrs.update({'name':'first_name','placeholder':'First Name','type':'text'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['department', 'phonenumber']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'name':'department','placeholder':'Department','type':'text'})
        self.fields['phonenumber'].widget.attrs.update({'name':'phonenumber','placeholder':'Phone Number','type':'text'})

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'type':'name','class':'form-control','name':'username','placeholder':'Username'}))
    password=forms.CharField(widget=forms.TextInput(
        attrs={'type':'password','class':'form-control','name':'password','placeholder':'Password'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'name':'first_name','placeholder':'First Name','type':'text','class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'name':'last_name','placeholder':'Last Name','type':'text','class':'form-control'})
        self.fields['email'].widget.attrs.update({'name':'email','placeholder':'Email Address','type':'email','class':'form-control'})
        self.fields['phonenumber'].widget.attrs.update({'name':'phonenumber','placeholder':'Phone Number','type':'text','class':'form-control'})
        self.fields['subject'].widget.attrs.update({'name':'subject','placeholder':'Subject','type':'text','class':'form-control'})
