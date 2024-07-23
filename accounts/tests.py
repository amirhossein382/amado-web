from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTestCase(TestCase):
    username = "testUser"
    email = "testUserEmail"
    password = "testUser1382"

    def test_create_normal_user(self):
        user = get_user_model().objects.create_user(
            username=self.username, email=self.email, password=self.password
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            username=self.username, email=self.email, password=self.password
        )
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
