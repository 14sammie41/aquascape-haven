from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from community.models import Community

class TestCommunityViews(TestCase):
    def setUp(self):
        # create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
    def test_logged_in_user_can_post(self):
        """
        This test verifies that an authenticated user can successfully
        create a Community post and is redirected after submission.
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('community:create_post'), {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after post creation
        self.assertEqual(Community.objects.count(), 1)
        
    def test_post_requires_content(self):
        """
        This test verifies that a Community post cannot be created
        without content, and the form returns an error.
        """
        self.client.force_login(self.user)
        response = self.client.post(reverse('community:create_post'), {
            'title': 'Test Post',
            'content': ''
        })
        self.assertEqual(response.status_code, 200)  # Form re-rendered with errors
        self.assertFormError(response.context['form'], 'content', 'This field is required.')
        
    def test_anonymous_user_cannot_post(self):
        """
        This test verifies that an anonymous user is redirected to the login page
        when attempting to create a Community post.
        """
        response = self.client.post(reverse('community:create_post'), {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, '/accounts/login/?next=' + reverse('community:create_post'))
        self.assertEqual(Community.objects.count(), 0)
        