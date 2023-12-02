from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'style2-input ps-5 form-control text-grey-900 font-xsss fw-600'})
        self.fields['email'].widget.attrs.update({'class': 'style2-input ps-5 form-control text-grey-900 font-xsss fw-600'})
        self.fields['password1'].widget.attrs.update({'class': 'style2-input ps-5 form-control text-grey-900 font-xss ls-3'})
        self.fields['password2'].widget.attrs.update({'class': 'style2-input ps-5 form-control text-grey-900 font-xss ls-3'})
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = CustomUser.objects.filter(email=email)
        if r.count():
            raise ValueError("Email already exists")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = CustomUser.objects.filter(username=username)
        if r.count():
            raise ValueError("Username already exists")
        return username
    
    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
    


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'display_name', 'profile_pic']