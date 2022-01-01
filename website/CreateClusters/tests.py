from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from .models import *
from auth_app.models import AuthUser



# Create your tests here.

class SimpleTest(SimpleTestCase):
    def test_cluster_view_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)



class TestView(SimpleTestCase):

    def test_index_GET(self):

        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'CreateClusters/ClusterIndex.html')


import unittest

from .spiders import *

class StrategySpiderTestCase(unittest.TestCase):

    def test_ispdf(self):

        value = pdf_spider.ispdf(self, 'testpdf.pdf')

        self.assertEqual(value, True)

    def test_istxt(self):
        value = txt_spider.istxt(self, 'testtxt.txt')
        self.assertEqual(value, True)

    def test_isdocx(self):
        value = docx_spider.isdocx(self, 'testdocx.docx')
        self.assertEqual(value, True)









