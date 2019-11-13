from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home
from .models import Log
from .templatetags.calculations import calculate_total_calories


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

    def test_new_log_valid_post_data(self):
        url = reverse('new_log')
        data = {
            'date': '2019-11-01',
            'distance': 4.9,
            'time': 22,
            'weight': 80,
        }
        self.client.post(url, data)
        self.assertTrue(Log.objects.exists())

class CalculationTests(TestCase):
    def test_calculate_total_calories(self):
        calories = calculate_total_calories(4.66, 28, 80)
        assert round(calories) == 368

