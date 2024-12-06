import os


class RecommendationSystem:
    """Class to implement the recommendation system logic."""

    def __init__(self, movie_file, history_file):
        # Load movies and user histories using internal methods
        self.movies = self.parse_movies(movie_file)
        self.user_histories = self.parse_histories(history_file)

    def parse_movies(self, file_path):
        """
        Parses a movie file and returns a dictionary of movie IDs and their titles.

        :param file_path: Path to the movie file.
        :return: Dictionary {movie_id: title}.
        """
        movies = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        movie_id, title = line.strip().split(",", 1)
                        movies[int(movie_id)] = title
                    except ValueError:
                        print(f"Error: Malformed line in movie file: '{line}'")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while reading the movie file: {e}")
            exit(1)
        return movies

    def parse_histories(self, file_path):
        """
        Parses a history file and returns a list of sets representing user watch histories.

        :param file_path: Path to the history file.
        :return: List of sets, where each set contains watched movie IDs for a user.
        """
        histories = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        histories.append(set(map(int, line.strip().split(","))))
                    except ValueError:
                        print(f"Error: Malformed line in history file: '{line}'")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while reading the history file: {e}")
            exit(1)
        return histories

    def recommend(self, user_watch_history):
        """
        Recommend a movie based on user watch history.

        :param user_watch_history: List of movie IDs watched by the user.
        :return: Recommended movie title or a message if no recommendations are available.
        """
        user = set(map(int, user_watch_history))
        relevant_movies = self.get_relevant_movies(user)

        if not relevant_movies:
            return "No recommendations available."

        recommended_movie_id = max(relevant_movies, key=relevant_movies.get)
        return self.movies[recommended_movie_id]

    def get_relevant_movies(self, user_watch_history):
        """
        Find relevant movies to recommend based on user watch history.

        :param user_watch_history: Set of movie IDs watched by the user.
        :return: Dictionary of movie IDs and their relevance scores.
        """
        relevant_movies = {}
        for other_user in self.user_histories:
            common_movies = user_watch_history & other_user
            if len(common_movies) >= len(user_watch_history) / 2:
                unseen_movies = other_user - user_watch_history
                for movie_id in unseen_movies:
                    relevant_movies[movie_id] = relevant_movies.get(movie_id, 0) + len(common_movies) / len(user_watch_history)
        return relevant_movies


# File paths for movies and user histories
MOVIE_FILE = os.path.join("src", "lab4", "taskinput", "film.txt")
HISTORY_FILE = os.path.join("src", "lab4", "taskinput", "history.txt")

if __name__ == "__main__":
    # Initialize the recommendation system with the input files
    system = RecommendationSystem(MOVIE_FILE, HISTORY_FILE)

    # Take user input for their watch history
    user_input = input("Enter the list of movie IDs you have watched (comma-separated): ")
    user_watch_history = user_input.strip().split(",")  # Convert input to a list of integers

    # Generate and print the recommendation
    recommendation = system.recommend(user_watch_history)
    print(f"Recommendation: {recommendation}")
