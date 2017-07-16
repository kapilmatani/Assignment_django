from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from mysite.core.models import UserProfile
from django.db import models

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(min_length=1, max_length=30, help_text='Required. ', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))

    department = forms.CharField(min_length=1, max_length=30,help_text='Required. Add your Branch', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))

    last_name = forms.CharField(min_length=1, max_length=30, help_text='Required.', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    dob = forms.DateField(help_text='Required. Add dob in format yyyy-mm-dd')

    year = forms.CharField(min_length=4,max_length=4,help_text='Required. Add year of Graduation', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[ 0-9 ]+', 'title':'Enter Integer Only '}))

    mobile = forms.CharField(min_length=10,max_length=10,help_text='Reqired. Add phone No - 10 digits allowed', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[ 0-9 ]+', 'title':'Enter Integer Only '}))

    enrollment_no = forms.CharField(min_length=5,max_length=5,help_text='Required. Add your Enrollment No should be 5 digits', widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[ 0-9 ]+', 'title':'Enter Integer Only '}))

    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput() , help_text='Minimum 6 characters Required')

    class Meta:
        model = User
       # fields = ('username', 'first_name', 'dob','last_name', 'email','password1', 'password2', 'department','dob','year','mobile','enrollment_no',)
        fields = ('username', 'first_name','last_name','dob', 'email','mobile', 'department', 'year', 'enrollment_no','password1', 'password2',)
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.save()
#	user_profile = UserProfile(user=user, department=self.cleaned_data['department'],dob=self.cleaned_data['dob'],year=self.cleaned_data['year'], mobile=self.cleaned_data['mobile'], enrollment_no=self.cleaned_data['enrollment_no']) 
	user_profile = UserProfile(user=user, department=self.cleaned_data['department'],year=self.cleaned_data['year'],mobile=self.cleaned_data['mobile'], enrollment_no=self.cleaned_data['enrollment_no'],dob=self.cleaned_data['dob']) 
	user_profile.save()
        return user, user_profile
