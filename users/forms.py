from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixine
from users.models import User


class UserRegisterForm(StyleFormMixine, UserCreationForm):
    # phone_number = models.CharField(max_length=25, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    usable_password = None
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone_number')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('В номере телефона могут быть только цифры')
        return phone_number

