from django.test import TestCase

from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_by_url_name(self):
        response = self.client.get(reverse('page'))
        self.assertEqual(response.status_code,200)

    def test_home_page_by_title(self):
        response = self.client.get(reverse('page'))
        self.assertContains(response,'home page')

    def test_home_page_by_url(self):
                response = self.client.get('/')
                self.assertEqual(response.status_code,200)
    
    def test_home_page_template_use(self):
          response = self.client.get(reverse('page'))
          self.assertTemplateUsed(response,'home.html')