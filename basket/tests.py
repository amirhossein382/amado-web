from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import BasketView
from .models import Basket
from product.models import Product, Category, Brand


class BasketPageTest(TestCase):
    def setUp(self):
        self.url = reverse("basket")
        self.response = self.client.get(self.url)

    def test_page(self):
        self.assertTemplateUsed(self.response, 'cart/cart.html')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_used(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, BasketView.as_view().__name__)
        self.assertContains(self.response, '<h2>Shopping Cart</h2>')


class BasketModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testUser", email="testUser@gamil.com",
                                                    password="amir1382")
        self.basket = Basket.objects.create(user=self.user)
        self.setUp_product()

    def setUp_product(self):
        self.category = Category.objects.create(name="testCategory", description="testCategory")
        self.brand = Brand.objects.create(name="testBrand")
        self.product = Product.objects.create(
            name="testProduct",
            description="testProduct",
            price=10.5,
            category=self.category,
            brand=self.brand, quantity=2, color="red", is_active=True,
            image=r"C:\Users\Amir\Desktop\projects\anado-web\amado\media\products\img"
        )

    def test_basket_model(self):
        self.assertEqual(self.basket.user, self.user)

    def test_basket_add_method(self):
        product_line = self.basket.add(self.product, 1)
        self.assertEqual(product_line.basket, self.basket)
        self.assertEqual(product_line.product, self.product)
        self.assertEqual(product_line.quantity, 1)

    def test_basket_count_method(self):
        count = self.basket.get_basket_count()
        self.assertEqual(count, 0)
