from django.test import TestCase
from django.urls import reverse, resolve, reverse_lazy
from product.views import ProductDetailView
from product.models import Product, Category, Brand, ProductAnotherColor, ProductImage


class ProductDetailTest(TestCase):
    product_credentials = {
        'name': "testProduct",
        "description": "testProduct",
        'price': 10.5,
        'quantity': 2,
        'color': "red",
        'is_active': True,
        'image': r"C:\Users\Amir\Desktop\projects\anado-web\amado\media\products\img"
    }
    category_credentials = {
        'name': "testCategory",
        'description': "testCategory"
    }
    brand_credentials = {
        'name': "testBrand"
    }
    another_color_credentials = {
        "name": "red"
    }
    another_image_credentials = {
        "image": r"C:\Users\Amir\Desktop\projects\anado-web\amado\media\products\img"
    }

    def setUp(self):
        self.category = Category.objects.create(**self.category_credentials)
        self.brand = Brand.objects.create(**self.brand_credentials)
        self.product = Product.objects.create(
            **self.product_credentials, brand=self.brand, category=self.category
        )
        self.another_color = ProductAnotherColor.objects.create(**self.another_color_credentials, product=self.product)
        self.another_image = ProductImage.objects.create(**self.another_image_credentials, product=self.product)

        self.url = reverse("product", args=(str(self.product.pk),))
        self.response = self.client.get(self.url)

    def test_category_instance(self):
        self.assertEqual(self.category.name, self.category_credentials['name'])
        self.assertEqual(self.category.description, self.category_credentials['description'])

    def test_brand_instance(self):
        self.assertEqual(self.brand.name, self.brand_credentials['name'])

    def test_product_model_instance(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.name, self.product_credentials["name"])
        self.assertEqual(self.product.is_active, self.product_credentials["is_active"])
        self.assertEqual(
            self.product.image, self.product_credentials["image"]
        )
        self.assertEqual(self.product.color, self.product_credentials["color"])
        self.assertEqual(self.product.quantity, self.product_credentials["quantity"])

    def test_another_color_instance(self):
        self.assertEqual(self.another_color.product.colors.first().name, self.another_color_credentials["name"])
        self.assertEqual(self.another_color.product, self.product)

    def test_another_image_instance(self):
        self.assertEqual(self.another_image.product.images.first().image, self.another_image_credentials["image"])
        self.assertEqual(self.another_image.product, self.product)

    def test_templates_used(self):
        self.assertTemplateUsed(self.response, 'product-details/product-details.html')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_loginpage_url_resolves_views(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, ProductDetailView.as_view().__name__)
