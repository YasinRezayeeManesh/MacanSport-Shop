from django import forms
from account_module.models import User
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError


class EditUserPanelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'about_user': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره شخص',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control margin-bottom-30',
        }),
        validators=[
            MaxLengthValidator(100)
        ]
    )
    new_password = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control margin-bottom-30',
        }),
        validators=[
            MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control margin-bottom-30',
        }),
        validators=[
            MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return password
        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
