from django.test import TestCase
from .models import Issues


class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issues_list.html")
    
    def test_get_add_issues_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_issues_page(self):
        issues = Issues(name="Create a Test")
        issues.save()

        page = self.client.get("/edit/{0}".format(issues.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_page_for_issues_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)