
import unittest
import os
from src.lab4.task1 import RecommendationSystem  # Import the RecommendationSystem class


class TestRecommendationSystem(unittest.TestCase):
    """Unit tests for the RecommendationSystem class."""

    def setUp(self):
        """Initialize the test setup. This will run before each test."""
        # Sample movie data (movie ID and title)
        self.sample_movies = """1,Movie A
2,Movie B
3,Movie C
4,Movie D
5,Movie E
"""
        # Sample user history (list of movie IDs watched by users)
        self.sample_history = """1,2,3
2,3,4
3,4,5
"""

        # Create temporary files for movies and histories
        self.movie_file_path = 'test_movies.txt'
        self.history_file_path = 'test_history.txt'

        with open(self.movie_file_path, 'w', encoding='utf-8') as file:
            file.write(self.sample_movies)
        
        with open(self.history_file_path, 'w', encoding='utf-8') as file:
            file.write(self.sample_history)

        # Initialize the RecommendationSystem with the file paths
        self.system = RecommendationSystem(self.movie_file_path, self.history_file_path)

    def test_parse_movies(self):
        """Test that movie file is parsed correctly."""
        movies = self.system.parse_movies(self.movie_file_path)
        # Assert that the movies dictionary contains the expected values
        self.assertEqual(len(movies), 5)
        self.assertEqual(movies[1], "Movie A")
        self.assertEqual(movies[5], "Movie E")

    def test_parse_histories(self):
        """Test that history file is parsed correctly."""
        histories = self.system.parse_histories(self.history_file_path)
        # Assert that the histories list contains sets of movie IDs
        self.assertEqual(len(histories), 3)
        self.assertEqual(histories[0], {1, 2, 3})
        self.assertEqual(histories[1], {2, 3, 4})

    def test_recommend(self):
        """Test the movie recommendation based on user's watch history."""
        user_watch_history = [1, 2, 3]
        recommendation = self.system.recommend(user_watch_history)
        # Assert that the recommendation is correct based on the mock data
        self.assertEqual(recommendation, "Movie D")

def test_get_relevant_movies(self):
    """Test the relevance score calculation for recommended movies."""
    user_watch_history = {1, 2, 3}
    relevant_movies = self.system.get_relevant_movies(user_watch_history)
    
    # Assert that the relevant movies dictionary contains the correct relevance score
    # For movie 4, the expected score is 2/3 = 0.6666666666666666 based on the common movies with User 2
    self.assertEqual(relevant_movies[4], 0.6666666666666666)
    self.assertEqual(relevant_movies[5], 0.5)  # The score for movie 5 is expected to be 0.5 based on User 3


    def tearDown(self):
        """Clean up after each test."""
        # Remove the temporary test files
        if os.path.exists(self.movie_file_path):
            os.remove(self.movie_file_path)
        if os.path.exists(self.history_file_path):
            os.remove(self.history_file_path)


if __name__ == "__main__":
    unittest.main()






