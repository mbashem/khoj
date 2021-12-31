from django.test import SimpleTestCase
from .models import *

# import unittest


# Create your tests here.
 
class  SimpleTest(SimpleTestCase):
     def test_cluster_view_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

   