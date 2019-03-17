from django.apps import apps
from django.test import TestCase
from .apps import IssuetrackerConfig


class TestIssuetrackerConfig(TestCase):

    def test_app(self):
        self.assertEqual("issuetracker", IssuetrackerConfig.name)
        self.assertEqual("issuetracker", apps.get_app_config("issuetracker").name)
