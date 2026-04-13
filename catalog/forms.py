import os
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from .models import Product

SPAM_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixine:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_ in self.fields.items():
            if isinstance(field_, BooleanField):
                field_.widget.attrs["class"] = "form-check-input"
            else:
                field_.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixine, ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ("created_at", "updated_at")

    def clean_price(self):
        price = self.cleaned_data.get("price", 0)
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name", 0)
        if name:
            for word in SPAM_WORDS:
                if word in name.lower():
                    raise ValidationError(f"Нельзя использовать слово-спам: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", 0)
        if description:
            for word in SPAM_WORDS:
                if word in description.lower():
                    raise ValidationError(f"Нельзя использовать слово-спам: {word}")
        return description

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            # Проверка на размер
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise ValidationError("Размер файла не должен превышать 5MB")

            # Проверка на расширение
            extension = os.path.splitext(image.name)[1].lower()
            if extension not in [".jpeg", ".png"]:
                raise ValidationError("Файл должен быть в формате jpeg или jpg")

        return image
