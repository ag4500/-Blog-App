from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
class Sign_Up(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        
        model=User
        fields=['username']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
class Sign_In(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
class Add(forms.ModelForm):
    class Meta:
        model=Post
        fields=('id','title','desc','status','image')
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.TextInput(attrs={'class':'form-control'})}
       
