from django import forms
from django.contrib.auth.models import User
from anab_app.models import UserProfileInfo, DemandeSimple

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('profile_pic',)

class DemandeSimpleForm(forms.ModelForm):
    class Meta:
        model = DemandeSimple
        fields = ('__all__')