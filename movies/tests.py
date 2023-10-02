from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Movie
from django.urls import reverse

class MovieAPITest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            genre='Test Genre',
            release_date='2023-10-01',
            director='Test Director'
        )

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')

    def test_movie_detail(self):
        response = self.client.get(reverse('movie-retrieve-update-delete', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')