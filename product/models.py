import uuid
from django.db import models
from django.urls import reverse
from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    image = models.ImageField(upload_to='products/img/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail-view", args=(str(self.pk,),))

    def in_stock(self) -> bool:
        if self.quantity > 0:
            return True
        return False

    def update_stock(self, new_quantity) -> None:
        self.quantity = new_quantity
        self.save()


class ProductAnotherColor(BaseModel):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Product another image"
