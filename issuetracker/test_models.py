from django.test import TestCase
from .models import Issues


class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        issues = Issues(name="Create a Test")
        issues.save()
        self.assertEqual(issues.name, "Create a Test")
        self.assertFalse(issues.done)
    
    def test_can_create_an_issue_with_a_name_and_status(self):
        issues = Issues(name="Create a Test", done=True)
        issues.save()
        self.assertEqual(issues.name, "Create a Test")
        self.assertTrue(issues.done)