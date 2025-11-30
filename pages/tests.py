from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):
    def test_about_page(self):
        """Тест страницы о проекте"""
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)

    def test_rules_page(self):
        """Тест страницы правил"""
        response = self.client.get(reverse('pages:rules'))
        self.assertEqual(response.status_code, 200)
