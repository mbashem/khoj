from django.test import SimpleTestCase
# import unittest


# Create your tests here.
 
class  SimpleTest(SimpleTestCase):
     def test_index_view_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


     def test_search_view_exist(self):
        response = self.client.get('?SearchResults//')
        self.assertEqual(response.status_code, 200) 


     def test_clusters_view_exist(self):
        response = self.client.get('?CreateClusters///')
        self.assertEqual(response.status_code, 200) 

     def test_logout_view_exist(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)      
         

     def test_admin_view_exist(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)      

     def test_accounts_view_exist(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 404)     

     def test_api_view_exist(self):
        response = self.client.get('/API/')
        self.assertEqual(response.status_code, 200)     
