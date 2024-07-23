from typing import override

from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from basket.models import Basket
from checkout.forms import CheckoutForm


class CheckoutView(LoginRequiredMixin, FormView):
    template_name = 'checkout/checkout.html'
    form_class = CheckoutForm
    success_url = '/'

    def queryset(self):
        basket_id = self.request.COOKIES.get('basket_id')

        queryset = Basket.get_basket_prefetch_or_none(basket_id)
        return queryset

    @override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["basket"] = self.queryset()
        return context
