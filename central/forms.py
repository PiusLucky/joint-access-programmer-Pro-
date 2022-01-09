import re

from django import forms
from central.models import Contact, EmailList
from django.contrib.auth import authenticate

class Contact_Me_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
        	"email",
            "subject",
            "comment"
        )


class EmailList_Form(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = ('email',)

class SigninForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
	password = forms.CharField(widget=forms.PasswordInput( 
		attrs={'class':'form-control', 'placeholder':'Enter Password'}))
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password :
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Invalid login details. Try Again.")
			if not user.is_active:
			    raise forms.ValidationError("This User is no longer active.")
			return super(SigninForm, self).clean(*args, **kwargs)