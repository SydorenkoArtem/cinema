from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserProfileTestCase(TestCase):
    """User Profile creation test"""

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('film:list'))
        self.assertRedirects(resp, '/')
