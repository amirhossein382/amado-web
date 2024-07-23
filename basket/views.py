from typing import override

from django.views.generic import ListView
from basket.models import BasketLine, Basket


class BasketView(ListView):
    model = BasketLine
    template_name = "cart/cart.html"
    context_object_name = "basket"

    @override
    def get_queryset(self):
        basket_id = self.request.COOKIES.get('basket_id')
        queryset = Basket.get_basket_prefetch_or_none(basket_id)
        return queryset
