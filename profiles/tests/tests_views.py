from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')

    def test_all_blogs(self):

        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 302)
