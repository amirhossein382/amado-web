from django import forms
from django.core.exceptions import ValidationError

from product.models import Product


class DetailsForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=10, widget=forms.NumberInput(
        attrs={"class": "qty-text", "id": "qty", "step": "1"}
    ))

    def save(self, basket):
        basket.add(
            self.cleaned_data.get("product"),
            self.cleaned_data.get("quantity"),
        )
        return basket

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        product = self.cleaned_data.get("product")
        if product.quantity < quantity:
            raise ValidationError(f"{quantity} not in stock; in stock{product.quantity}")
        return quantity
