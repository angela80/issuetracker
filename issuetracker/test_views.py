from django.test import TestCase
from django.shortcuts import get_object_or_404
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
        
        
    def test_post_create_an_issues(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        issues= get_object_or_404(Issues, pk=1)
        self.assertEqual(issues.done, False)
    
    def test_post_edit_an_issues(self):
        issues = Issues(name="Create a Test")
        issues.save()
        id = issues.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        issues = get_object_or_404(Issues, pk=id)

        self.assertEqual("A different name", issues.name)
    
    def test_toggle_status(self):
        issues = Issues(name="Create a Test")
        issues.save()
        id = issues.id

        response = self.client.post("/toggle/{0}".format(id))

        issues = get_object_or_404(Issues, pk=id)
        self.assertEqual(issues.done, True)   