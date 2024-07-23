from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CheckoutForm
from .views import CheckoutView
from .models import Checkout, Country


class CheckoutPageTest(TestCase):
    def setUp(self):
        self.url = reverse("checkout")
        self.credentials = {
            'username': "test", 'email': "test@gmail.com", 'password': "test1382"
        }

        self.user = self.create_simple_user()
        self.client.login(**self.credentials)
        self.response = self.client.get(self.url)

    def create_simple_user(self):
        user = get_user_model().objects.create_user(**self.credentials)
        return user

    def test_status_code_for_login(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'checkout/checkout.html')

    def test_form_is_valid(self):
        self.assertIsInstance(self.response.context["form"], CheckoutForm)

    def test_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, CheckoutView.as_view().__name__)

    def test_status_code_for_logout(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class CheckoutModelTest(TestCase):
    credentials = {
        "first_name": "testUser",
        "last_name": "testLastName",
        "company_name": "testCompanyName",
        "email": "testEmail@gamil.com",
        "address": "testAddress",
        "city": "testCity",
        "zipcode": 1222321,
        "phone_number": 9149830000,
        "comment": "testComment"
    }

    def setUp(self):
        self.country = Country.objects.create(
            name="Iran", code=98
        )
        self.checkout = Checkout.objects.create(
            **self.credentials, country=self.country
        )

    def test_country_instance(self):
        self.assertEqual(self.country.name, "Iran")
        self.assertEqual(self.country.code, 98)

    def test_checkout_instance(self):
        self.assertEqual(self.checkout.first_name, self.credentials["first_name"])
        self.assertEqual(self.checkout.last_name, self.credentials["last_name"])
        self.assertEqual(self.checkout.company_name, self.credentials["company_name"])
        self.assertEqual(self.checkout.email, self.credentials["email"])
        self.assertEqual(self.checkout.country, self.country)
        self.assertEqual(self.checkout.address, self.credentials["address"])
        self.assertEqual(self.checkout.city, self.credentials["city"])
        self.assertEqual(self.checkout.zipcode, self.credentials["zipcode"])
        self.assertEqual(self.checkout.phone_number, self.credentials["phone_number"])
        self.assertEqual(self.checkout.comment, self.credentials["comment"])
