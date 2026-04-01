from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from .models import Product


class StyleFormMixine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_ in self.fields.items():
            if isinstance(field_, BooleanField):
                field_.widget.attrs['class'] = 'form-check-input'
            else:
                field_.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixine, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ("created_at", "updated_at")

        def clean_price(self):
            price = self.cleaned_data['price']
            if price < 0:
                raise ValidationError('Цена не может быть отрицательной')
            else:
                return price
