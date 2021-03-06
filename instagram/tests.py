from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='alinur')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_photo='default.jpg', bio='this is a test profile')

    

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)



