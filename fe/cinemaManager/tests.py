from django.test import TestCase
from django.urls import reverse

class TestMyView(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse('my-view'))
        self.assertEqual(response.status_code, 200)