from datetime import datetime, timezone
import pytz
import time

from django.test import TestCase

# Create your tests here.

from .models import Link
from redirect.settings import TIME_ZONE

class TestGetLink(TestCase):

    test_link = None
    inactive_link = None


    def setUp(self) -> None:
        self.test_link = Link.objects.create(original_link="https://docs.djangoproject.com")
        self.inactive_link = Link.objects.create(
            original_link="https://docs.djangoproject.com",
            lifetime=datetime.now(pytz.timezone(TIME_ZONE)),
        )

    def test_get_original_link(self):
        response = self.client.get(f'/{self.test_link.short_link}')
        assert str(response) == '<HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="https://docs.djangoproject.com">'


    def test_inactive_link(self):
        time.sleep(5)
        response = self.client.get(f'/{self.inactive_link.short_link}')
        assert response.status_code == 404

class TestCreateLink(TestCase):

    def test_create_link(self):
        response = self.client.post("/links/create/", data={
            "original_link": 'https://docs.djangoproject.com'
        })
        assert response.status_code == 201

    def test_create_with_lifetime(self):
        response = self.client.post("/links/create/", data={
            "original_link": 'https://docs.djangoproject.com',
            "lifetime": datetime.now()
        })
        assert response.status_code == 201