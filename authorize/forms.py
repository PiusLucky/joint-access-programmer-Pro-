import re
from django import forms
from central.models import Contact
import string
import random
from django.contrib.auth import authenticate
from django import forms
from django.forms import ModelForm, CharField
from django.contrib.auth.hashers import make_password,is_password_usable,check_password
from django.forms import BaseModelFormSet
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password, password_validators_help_text_html
from django.shortcuts import render,redirect
from datetime import *
from django.http import HttpResponseRedirect, HttpResponse,QueryDict

def make_salt():
	letters=string.ascii_letters
	result=random.sample(letters,5)
	return ''.join(result)


class SignupForm(ModelForm):
	verify_password = forms.CharField(label="Re-enter password",widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','password','verify_password','email']
		widgets = {
			'password':forms.PasswordInput(),
		}
	def clean(self):
		cleaned_data=super(SignupForm,self).clean()
		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		ps1 = cleaned_data.get('password')
		ps2 = cleaned_data.get('verify_password')
		if ps1!=ps2:
			msg="Password does not match!"
			self.add_error('verify_password',msg)
		encoded_password=make_password(ps1,make_salt())
		cleaned_data['password'] = encoded_password
		if email and User.objects.filter(email=email).exclude(username=username).count():
			msg=""
			self.add_error('email',msg)
		if ps1:
			try:
				validate_password(ps1,user=self)
				cleaned_data['help_text']=None
			except ValidationError:
				cleaned_data['help_text']=password_validators_help_text_html()
				self.add_error('password','Your password is too weak. Please choose another password!')
		return cleaned_data

class SigninForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
	password = forms.CharField(widget=forms.PasswordInput( 
		attrs={'class':'form-control', 'placeholder':'Enter Password'}))
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			try:
				user = authenticate(username=User.objects.get(email=username), password=password)
			except:
				user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Invalid login details. Try Again.")
			if not user.is_active:
			    raise forms.ValidationError("This User is no longer active.")
			return super(SigninForm, self).clean(*args, **kwargs)

	
