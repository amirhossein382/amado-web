from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='baskets', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    @classmethod
    def get_basket_prefetch_or_none(cls, pk):
        """get basket with prefetch lines or None to reduce the number of queries"""
        try:
            instance = cls.objects.prefetch_related('lines__product').get(id=pk)
        except cls.DoesNotExist:
            instance = None
        return instance

    @classmethod
    def get_basket_or_none(cls, pk):
        """get basket with prefetch lines or None to reduce the number of queries"""
        try:
            instance = cls.objects.prefetch_related('lines').get(id=pk)
        except cls.DoesNotExist:
            instance = None
        return instance

    def add(self, product, quantity):
        """create basket line if it doesn't exist and add products to basket"""
        qs = self.lines.filter(product=product)
        if qs.exists():
            product_line = qs.first()
            product_line.quantity = quantity
            product_line.save()
        else:
            product_line = self.lines.create(product=product, quantity=quantity)

        return product_line

    def get_basket_count(self) -> int:
        """get basket lines count"""
        return self.lines.count()

    def get_total(self) -> int:
        """Total shopping cart"""
        line_total = [
            line.product.price * line.quantity for line in self.lines.all()
        ]

        return sum(line_total)


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lines')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
