import sys
from precious_lotr_sdk import LOTRSDK

def main():
    print("Welcome to The Lord of the Rings API Explorer!")
    print("Please enter your API key:")
    api_key = input().strip()
    
    if len(api_key) < 13:
        api_key = 'JiWYLCEOboEgzPoi14gd'
    sdk = LOTRSDK(api_key)
    movies = sdk.get_movies()
    movie_ids = [movie['_id'] for movie in movies['docs']]

    while True:
        print("\nChoose an option:")
        print("1. List all movies")
        print("2. Get details of a movie")
        print("3. Get quotes from a movie")
        print("4. Exit")

        choice = input().strip()

        if choice == '1':
            print("\nFetching all movies...")
            for index, movie in enumerate(movies['docs'], start=1):
                print(f"{index}. {movie['name']}")

        elif choice == '2':
            print("\nMovie Details Selected")
            print("\nEnter the movie index (1-6):")
            for index, movie in enumerate(movies['docs'], start=1):
                print(f"{index}. {movie['name']}")
            try:
                movie_index = int(input().strip()) - 1
                if movie_index not in range(len(movie_ids)):
                    raise IndexError
                movie_id = movie_ids[movie_index]
            except (ValueError, IndexError):
                print("Invalid movie index. Please try again.")
                continue

            print("\nFetching movie details...")
            movie_dict = sdk.get_movie(movie_id)['docs'][0]
            print(f"ID: {movie_dict['_id']}")
            print(f"Name: {movie_dict['name']}")
            print(f"Runtime: {movie_dict['runtimeInMinutes']} minutes")
            print(f"Budget: {movie_dict['budgetInMillions']} million")
            print(f"Box Office Revenue: {movie_dict['boxOfficeRevenueInMillions']} million")
            print(f"Academy Award Nominations: {movie_dict['academyAwardNominations']}")
            print(f"Academy Award Wins: {movie_dict['academyAwardWins']}")
            print(f"Rotten Tomatoes Score: {movie_dict['rottenTomatoesScore']}")

        elif choice == '3':
            print("\nQuotes Selected")
            print("\nEnter the movie index (1-6):")
            for index, movie in enumerate(movies['docs'], start=1):
                print(f"{index}. {movie['name']}")
            try:
                movie_index = int(input().strip()) - 1
                if movie_index not in range(len(movie_ids)):
                    raise IndexError
                movie_id = movie_ids[movie_index]
            except (ValueError, IndexError):
                print("Invalid movie index. Please try again.")
                continue

            print("\nFetching movie quotes...")
            quotes = sdk.get_movie_quotes(movie_id)
            for quote in quotes['docs']:
                print(f"{quote['character']} said: \"{quote['dialog']}\"")

        elif choice == '4':
            print("Thank you for using The Lord of the Rings API Explorer! Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid option. Please try again.")

if __name__ == '__main__':
    main()
