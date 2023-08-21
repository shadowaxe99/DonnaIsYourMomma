
import unittest
from django.test import TestCase, Client
from django.urls import reverse
from app.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')
        self.payment_url = reverse('payment')

    def test_user_registration(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123'
        })

        self.assertEquals(response.status_code, 302)

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123'
        })

        self.assertEquals(response.status_code, 302)

    def test_dashboard_access(self):
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code, 200)

    def test_payment_gateway(self):
        response = self.client.get(self.payment_url)
        self.assertEquals(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
