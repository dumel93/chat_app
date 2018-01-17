from django.test import TestCase
from django.test.client import Client
# Create your tests here.
import unittest


from accounts.models import User
from .models import Post
from groups.models import Group

class GroupTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='dumel0', email='test@wp.pl', password="test123")
        self.group = Group.objects.create(name='Siatkowka')
        self.client.login(username='dumel0',password="test123")
        self.post = Post.objects.create(message="dzien dobry",user_id=1,group_id=1)


    def test_post_message(self):
        self.assertEqual(self.post.message, 'dzien dobry')

    def test_posts_details(self):
        # Issue a GET request.
        response = self.client.get('/posts/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['post_list']), 1)

    def test_post_delete(self):
        response1=self.client.get('/groups/posts/in/siatkowka/')
        self.assertEqual(response1.status_code,200)
        response2=self.client.get('/posts/delete/1')
        self.assertEqual(response2.status_code, 301)
        response3 = self.client.post('/posts/delete/1')
        self.assertEqual(response3.status_code, 301)

if __name__ == "__main__":
    unittest.main()