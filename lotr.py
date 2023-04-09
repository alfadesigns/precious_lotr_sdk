import requests

class LOTRSDK:
    BASE_URL = 'https://the-one-api.dev/v2/movie'

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, endpoint):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_movies(self):
        return self._make_request(LOTRSDK.BASE_URL)

    def get_movie(self, movie_id):
        return self._make_request(f'{LOTRSDK.BASE_URL}/{movie_id}')

    def get_movie_quotes(self, movie_id):
        return self._make_request(f'{LOTRSDK.BASE_URL}/{movie_id}/quote')

    def get_movie_info_and_quotes(self, movie_id):
        movie_info = self.get_movie(movie_id)
        quotes = self.get_movie_quotes(movie_id)

        return {
            'movie_info': movie_info,
            'quotes': quotes,
        }

    def get_all_movie_info_and_quotes(self):
        movies = self.get_movies()
        all_movie_info_and_quotes = []

        for movie in movies['docs']:
            movie_id = movie['_id']
            movie_info_and_quotes = self.get_movie_info_and_quotes(movie_id)
            all_movie_info_and_quotes.append(movie_info_and_quotes)

        return all_movie_info_and_quotes

    def get_movie_and_characters(self, movie_id):
        movie_info = self.get_movie(movie_id)
        quotes = self.get_movie_quotes(movie_id)
        characters = set(quote['character'] for quote in quotes['docs'])

        return {
            'movie_info': movie_info,
            'characters': characters,
        }