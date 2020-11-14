from django import forms
from core.models import Contactus, UserProfile


class ContactusForm(forms.ModelForm):
    """
    Contact us form template
    """

    name = forms.CharField(help_text="Enter your name", max_length=25, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Tell us your name'
    }))
    email = forms.EmailField(help_text="enter your mail", max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Email'
    }))
    subject = forms.CharField(help_text="Enter Subject", max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Subject'
    }))
    comments = forms.CharField(required=True, max_length=1000, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Write to us'
    }))

    class Meta:
        model = Contactus
        exclude = ('created',)


class UserProfileForm(forms.ModelForm):
    gender = forms.CharField(required=True, max_length=25)
    picture = forms.ImageField(required=False)
    department = forms.CharField(required=True, max_length=10)
    year = forms.CharField(required=True, max_length=10)
    college = forms.CharField(required=True, max_length=60)

    class Meta:
        model = UserProfile
        exclude = ('user', 'clear', 'is_previously_logged', 'color_mode', 'dark_mode',)
