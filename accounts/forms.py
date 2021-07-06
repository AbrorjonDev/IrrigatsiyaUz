from django import forms
from .models import Profile
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','faculty', 'cafedra', 'level', 'avatar')

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='Enter your name..')
    email = forms.EmailField(help_text='Enter your email..')
    phone = PhoneNumberField(help_text='Enter your phone number..')
    message = forms.CharField(widget=forms.Textarea(attrs={'row':7}))
 
    class Meta:
        fields = ('subject', 'email', 'phone', 'message')



        
