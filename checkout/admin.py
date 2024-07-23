from typing import override

from django.contrib import admin
from checkout.models import Checkout, Country


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_filter = ("phone_number", "city", "country", "zipcode")

    @override
    def has_add_permission(self, request):
        return False


@admin.register(Country)
class CountriesAdmin(admin.ModelAdmin):
    pass
