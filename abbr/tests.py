import json

from django.test import RequestFactory, TestCase
from django.urls import reverse

from . import views
from .models import Abbr


class AbbrModelTests(TestCase):
    def test_model(self):
        pass


class AbbrViewsTests(TestCase):
    def setUp(self):
        self.abbr = Abbr.objects.create(name="PK", description="Paige Kim")
        self.assertEqual(Abbr.objects.count(), 1)
        self.assertQuerysetEqual(Abbr.objects.all(), ["<Abbr: PK>"])

    def test_list_view(self):
        response = self.client.get(reverse("abbr:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="abbr/abbr_list.html")
        self.assertEqual(len(response.context["object_list"]), 1)

    def test_list_view_possible_matches(self):
        query = "Paige"
        response = self.client.get(reverse("abbr:list"), {"q": query})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], query)
        self.assertContains(response, "PK")
        self.assertEqual(len(response.context["object_list"]), 1)
        self.assertNotContains(response, "Did you mean")

        query = "Page"
        response = self.client.get(reverse("abbr:list"), {"q": query})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["query"], query)
        self.assertEqual(len(response.context["object_list"]), 0)
        self.assertContains(response, "Did you mean")

    def test_detail_view(self):
        response = self.client.get(reverse("abbr:detail", args=[self.abbr.id]))
        self.assertTemplateUsed(response, template_name="abbr/abbr_detail.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paige Kim")

    def test_backup_file_fullpath_exist(self):
        import os

        self.assertTrue(os.path.exists(views.BACKUP_FILE_FULLPATH))

    def test_save_wiki_summary(self):
        pass

