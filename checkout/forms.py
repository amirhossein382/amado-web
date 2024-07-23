from django import forms
from checkout.models import Checkout, Country


def get_default_country():
    return Country.objects.first()


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "first_name", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "id": "last_name", "placeholder": "Last Name"}
            ),
            "company_name": forms.TextInput(
                attrs={"class": "form-control", "id": "company", "placeholder": "Company Name"}
            ),
            "email": forms.EmailInput(

                attrs={"class": "form-control", "id": "email", "placeholder": "Email"}
            ),
            "country": forms.Select(
                attrs={"class": "w-100", "id": "country"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control mb-3", "id": "street_address", "placeholder": "Address"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "id": "city", "placeholder": "Town"}
            ),
            "zipcode": forms.NumberInput(
                attrs={"class": "form-control", "id": "zipCode", "placeholder": "Zip Code"}
            ),
            "phone_number": forms.NumberInput(
                attrs={"class": "form-control", "id": "phone_number", "placeholder": "Phone Number"}
            ),
            "comment": forms.Textarea(
                attrs={"class": "form-control w-100", "id": "comment", "cols": "30", "rows": "10"
                    , "placeholder": "Leave a comment about your order"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].initial = get_default_country()
