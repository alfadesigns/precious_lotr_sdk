import unittest
from unittest.mock import patch
import requests_mock
from precious_lotr_sdk import LOTRSDK

class TestLOTRSDK(unittest.TestCase):
    API_KEY = 'your_api_key'

    def setUp(self):
        self.sdk = LOTRSDK(TestLOTRSDK.API_KEY)

    @requests_mock.Mocker()
    def test_get_movies(self, mock_request):
        mock_request.get('https://the-one-api.dev/v2/movie', json={'docs': [{'name': 'Test Movie'}]})
        movies = self.sdk.get_movies()
        self.assertEqual(len(movies['docs']), 1)
        self.assertEqual(movies['docs'][0]['name'], 'Test Movie')

    @requests_mock.Mocker()
    def test_get_movie(self, mock_request):
        movie_id = '5cd95395de30eff6ebccde5b'
        mock_request.get(f'https://the-one-api.dev/v2/movie/{movie_id}', json={'docs': [{'name': 'Test Movie'}]})
        movie = self.sdk.get_movie(movie_id)
        self.assertEqual(movie['docs'][0]['name'], 'Test Movie')

    @requests_mock.Mocker()
    def test_get_movie_quotes(self, mock_request):
        movie_id = '5cd95395de30eff6ebccde5b'
        mock_request.get(f'https://the-one-api.dev/v2/movie/{movie_id}/quote', json={'docs': [{'character': 'Gandalf', 'dialog': 'Fly, you fools!'}]})
        quotes = self.sdk.get_movie_quotes(movie_id)
        self.assertEqual(len(quotes['docs']), 1)
        self.assertEqual(quotes['docs'][0]['character'], 'Gandalf')
        self.assertEqual(quotes['docs'][0]['dialog'], 'Fly, you fools!')


if __name__ == '__main__':
    unittest.main()
