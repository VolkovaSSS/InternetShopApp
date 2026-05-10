from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixine
from users.models import CustomUser


class CustomUserRegisterForm(StyleFormMixine, UserCreationForm):
    phone_number = forms.CharField(
        max_length=25, required=False, help_text="Введите номер телефона"
    )
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2", "phone_number")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("В номере телефона могут быть только цифры")
        return phone_number
