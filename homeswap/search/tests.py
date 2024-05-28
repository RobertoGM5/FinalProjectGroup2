from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import BlogPost
from accounts.models import AppUser, HomePhoto
from datetime import datetime, timedelta
from .forms import BlogPostSearchForm


class BlogPostSearchFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'search_destination': 'DestinationCity',
            'search_start_date': datetime.now().strftime('%Y-%m-%d'),
            'search_end_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'search_num_travelers': 3
        }

        self.invalid_data = {
            'search_destination': '',  
            'search_start_date': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),  
            'search_end_date': datetime.now().strftime('%Y-%m-%d'),
            'search_num_travelers': 'invalid'
        }

    def test_form_valid_data(self):
        form = BlogPostSearchForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = BlogPostSearchForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('search_destination', form.errors)
        self.assertIn('search_start_date', form.errors)
        self.assertIn('search_num_travelers', form.errors)

    def test_form_missing_required_fields(self):
        form = BlogPostSearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('search_destination', form.errors)
        self.assertIn('search_start_date', form.errors)
        self.assertIn('search_end_date', form.errors)
        self.assertIn('search_num_travelers', form.errors)

    def test_form_invalid_dates(self):
        data = self.valid_data.copy()
        data['search_start_date'] = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
        data['search_end_date'] = datetime.now().strftime('%Y-%m-%d')
        form = BlogPostSearchForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('search_start_date', form.errors)
        self.assertIn('search_end_date', form.errors)

    def test_form_invalid_travelers(self):
        data = self.valid_data.copy()
        data['search_num_travelers'] = 'invalid'
        form = BlogPostSearchForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('search_num_travelers', form.errors)


class SearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.app_user = AppUser.objects.create(user=self.user, location='TestCity')
        self.blog_post = BlogPost.objects.create(
            user=self.user,
            location='DestinationCity',
            to_city='TestCity',
            start_date=datetime.now() - timedelta(days=1),
            end_date=datetime.now() + timedelta(days=1),
            max_capacity=5
        )
        self.search_url = reverse('search')
        self.details_url = reverse('blog_post_details', args=[self.blog_post.id])  

    def test_search_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.search_url, {
            'search_destination': 'DestinationCity',
            'search_start_date': datetime.now().strftime('%Y-%m-%d'),
            'search_end_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'search_num_travelers': 3
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post_list.html')
        self.assertContains(response, self.blog_post.title)

    def test_search_view_unauthenticated_user(self):
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search_form.html')
        self.assertContains(response, 'Authentication credentials were not provided.')

    def test_blog_post_details_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/blog_post_details.html')
        self.assertContains(response, self.blog_post.title)

        HomePhoto.objects.create(user=self.user, photo='photo1.jpg')
        HomePhoto.objects.create(user=self.user, photo='photo2.jpg')

        response = self.client.get(self.details_url)
        self.assertIn('user_photos', response.context)
        self.assertEqual(len(response.context['user_photos']), 2)
