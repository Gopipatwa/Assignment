from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {'first_name','last_name','email','password','username'}
		labels = {'first_name':'First Name','last_name':'Last Name','email':'Email','password':'Password','username':'Username'}
		widgets = {
		'first_name':forms.TextInput(attrs={'class':'form-controls','required':""}),
		'last_name':forms.TextInput(attrs={'class':'form-controls','required':""}),
		'email':forms.EmailInput(attrs={'class':'form-controls','required':""}),
		'password':forms.PasswordInput(attrs={'class':'form-controls','required':""}),
		'username':forms.TextInput(attrs={'class':'form-controls','required':""}),
		}
