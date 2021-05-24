from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'general-form-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'general-form-input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'general-form-input'}))
