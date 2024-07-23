from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomeListView, ShopListView


class HomePageTestCase(TestCase):

    def setUp(self):
        self.url = reverse("home")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "home/index.html")

    def test_view_used(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, HomeListView.as_view().__name__)


class ShopPageTestCase(TestCase):
    def setUp(self):
        self.url = reverse("shop")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "shop/shop.html")

    def test_view_used(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, ShopListView.as_view().__name__)
