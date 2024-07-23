from typing import override

from django.contrib import admin

from basket.models import Basket, BasketLine


class BasketLineInline(admin.TabularInline):
    model = BasketLine


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = (BasketLineInline,)

    @override
    def has_add_permission(self, request):
        return False

    @override
    def has_change_permission(self, request, obj=None):
        return False
