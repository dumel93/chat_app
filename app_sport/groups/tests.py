from django.test import TestCase
from django.test.client import Client
# Create your tests here.
import unittest


from . models import Group

class GroupTestCase(TestCase):

    def setUp(self):

        self.client = Client()
        self.group = Group.objects.create(name='Zuzel')

    def tearDown(self):
        self.group=None

    def test_group_name(self):
        self.assertEqual(self.group.name,'Zuzel')
        self.assertEqual(self.group.slug,'zuzel')

    def test_group_details(self):
        # Issue a GET request.
        response = self.client.get('/groups/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.

        self.assertEqual(len(response.context['group_list']), 1)

    def test_group_create(self):

        response=self.client.get('/groups/posts/in/zuzel/')
        self.assertEqual(response.status_code,200)
        response = self.client.get('/groups/posts/in/zuzel1/')
        self.assertEqual(response.status_code, 404)

