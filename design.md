# The Lord of the Rings SDK Design

This document describes the design and structure of the LOTR SDK, a Python package that simplifies the interaction with The Lord of the Rings API.

## Design Goals

The main goals of this SDK are:

1. Provide a simple, user-friendly interface to interact with the API.
2. Promote code readability and maintainability.
3. Handle common tasks, such as authentication and request handling, within the SDK.

## SDK Structure

The SDK follows a class-based approach with a single class `LOTRSDK`. The class is responsible for handling the authentication and making API calls to the movie-related endpoints:

1. /movie
2. /movie/{id}
3. /movie/{id}/quote

### LOTRSDK Class

The `LOTRSDK` class has the following methods:

- `__init__(self, api_key)`: Initializes the SDK with the provided API key.
- `_make_request(self, endpoint)`: A private method that handles making API requests. It accepts an endpoint as input and returns the JSON response from the API.
- `get_movies(self)`: Fetches all movies from the API.
- `get_movie(self, movie_id)`: Fetches a specific movie by its ID.
- `get_movie_quotes(self, movie_id)`: Fetches all quotes from a specific movie by its ID.

The class uses the `requests` library to make HTTP requests and handle the responses.

## Error Handling

The SDK handles HTTP errors by raising exceptions using the `response.raise_for_status()` method from the `requests` library. This ensures that any errors from the API are propagated to the user and can be handled appropriately.