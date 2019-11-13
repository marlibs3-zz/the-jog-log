from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home
from .views import new_log
from .models import Log


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class NewLogTests(TestCase):
    def setUp(self):
        Log.objects.create(date='2019-11-01', distance=4.7, time=20, weight=80)

    def test_csrf(self):
        url = reverse('new_log')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'date': '2019-11-01',
            'distance': 4.9,
            'time': 22,
            'weight': 80,
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())