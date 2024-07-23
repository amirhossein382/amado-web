from typing import override

from django.http import HttpResponseRedirect, Http404
from django.views.generic import DetailView

from basket.models import Basket
from product.forms import DetailsForm
from product.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details/product-details.html'
    context_object_name = 'product'

    @override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DetailsForm({'product': self.object.pk})
        context['basket'] = Basket.get_basket_or_none(pk=self.request.COOKIES.get('basket_id'))
        return context

    def post(self, request, *args, **kwargs):
        response = HttpResponseRedirect(self.request.POST.get('next', '/'))
        basket_id = request.COOKIES.get('basket_id', None)
        if basket_id is not None:
            try:
                basket = Basket.objects.prefetch_related('lines').get(pk=basket_id)
            except Basket.DoesNotExist:
                raise Http404('Basket does not exist')
        else:
            basket = Basket.objects.create()
            if request.user.is_authenticated:
                basket.user = request.user
            response.set_cookie("basket_id", basket.id)

        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save(basket)
        basket.save()
        return response
