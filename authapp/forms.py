import hashlib
import random
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'general-form-input', 'placeholder': 'Подтвердите пароль'}), help_text='Пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'password2': 'Пароль'
        }

    def save(self):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'general-form-input general-form-input-read-only', 'readonly': True
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'general-form-input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'general-form-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'general-form-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'general-form-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('tagline', 'about_me', 'gender', 'birth_date')

    tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'general-form-input'}))
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class': 'general-form-input', 'rows': 5}))
    gender = forms.ChoiceField(
        choices=UserProfile.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'general-form-input'})
    )
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'general-form-input'}))
