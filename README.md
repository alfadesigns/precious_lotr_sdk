# The Lord of the Rings SDK

The LOTR SDK is a Python package that simplifies the interaction with The Lord of the Rings API. This SDK allows developers to easily fetch data about the movies, including specific movie details and quotes.

## Installation

You can install the LOTR SDK using pip:

```
pip install precious-lotr-sdk==1.0.2

```

## Usage

To use the SDK, you need to import the `LOTRSDK` class and instantiate it with your API key:

```
import precious_lotr_sdk

api_key = 'your_api_key'
sdk = LOTRSDK(api_key)
```

### Fetch all movies

You can fetch all movies using the `get_movies()` method:

```
movies = sdk.get_movies()
print(movies)
```

### Fetch a specific movie

You can fetch a specific movie using the `get_movie(movie_id)` method:

```
movie_id = '5cd95395de30eff6ebccde5b'
movie = sdk.get_movie(movie_id)
print(movie)
```

### Fetch quotes from a specific movie

You can fetch all quotes from a specific movie using the `get_movie_quotes(movie_id)` method:

```
movie_id = '5cd95395de30eff6ebccde5b'
quotes = sdk.get_movie_quotes(movie_id)
print(quotes)
```

### Fetch movie info and quotes

You can fetch a specific movie's information and quotes using the `get_movie_info_and_quotes(movie_id)` method:

```
movie_id = '5cd95395de30eff6ebccde5b'
movie_info_and_quotes = sdk.get_movie_info_and_quotes(movie_id)
print(movie_info_and_quotes)
```

### Fetch movie info and characters

You can fetch movie information and a set of character names who have quotes in the movie using the 'get_movie_and_characters(movie_id)' method:

```
movie_id = '5cd95395de30eff6ebccde5b'
movie_and_characters = sdk.get_movie_and_characters(movie_id)
print(movie_and_characters)
```


## Testing

To test the SDK, you can create a Python script and include the above code snippets with your actual API key. Run the script to see the SDK in action.

## Contributing

We welcome contributions to improve the LOTR SDK. If you find any issues or have suggestions for enhancements, please submit an issue or create a pull request.

## License

The LOTR SDK is released under the MIT License.