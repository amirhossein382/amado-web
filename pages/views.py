from typing import override

from django.views.generic import ListView

from basket.models import Basket
from product.models import Product, Category, Brand


class HomeListView(ListView):
    template_name = 'home/index.html'
    model = Product
    queryset = Product.objects.filter(is_active=True)[:9]

    @override
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.get_basket_or_none(pk=self.request.COOKIES.get('basket_id'))
        return context


class ShopListView(ListView):
    template_name = 'shop/shop.html'
    model = Product
    paginate_by = 8

    @override
    def get_queryset(self):
        qs = super().get_queryset().filter(is_active=True)
        get_data = self.request.GET

        if get_data.get('category', False):
            qs = qs.filter(category__name=get_data.get('category'))

        if get_data.get('color', False):
            qs = qs.filter(color=get_data.get('color'))

        if get_data.get('brand', False):
            qs = qs.filter(brand__name=get_data.get('brand'))

        if get_data.get('price_min', False):
            qs = qs.filter(price__lte=get_data.get('price_min'))

        if get_data.get('price_max', False):
            qs = qs.filter(price__gte=get_data.get('price_max'))

        if get_data.get("brand", False):
            qs = qs.filter(price__gte=get_data.get('brand'))

        return qs

    @override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['basket'] = Basket.get_basket_or_none(pk=self.request.COOKIES.get('basket_id'))

        return context
