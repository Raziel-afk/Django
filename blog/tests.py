from django.test import TestCase
from django.urls import reverse


class BlogTests(TestCase):
    def test_index_page(self):
        """Тест главной страницы"""
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Лента записей')

    def test_post_detail_page(self):
        """Тест страницы деталей поста"""
        response = self.client.get(reverse('blog:post_detail', args=[0]))
        self.assertEqual(response.status_code, 200)

    def test_category_page(self):
        """Тест категории"""
        response = self.client.get(reverse(
            'blog:category_posts', args=['travel']))
        self.assertEqual(response.status_code, 200)
