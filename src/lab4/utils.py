import os


def read_file(file_path):
    """
    Reads a text file and returns its content as a list of lines.
    Each line is stripped of whitespace and split if necessary.

    :param file_path: Path to the file to be read.
    :return: List of lines in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)  # Exit the program if the file is missing
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        exit(1)


def parse_movies(file_path):
    """
    Parses a movie file and returns a dictionary of movie IDs and their titles.

    :param file_path: Path to the movie file.
    :return: Dictionary {movie_id: title}.
    """
    lines = read_file(file_path)
    movies = {}
    for line in lines:
        try:
            movie_id, title = line.split(",", 1)  # Split into ID and title
            movies[int(movie_id)] = title
        except ValueError:
            print(f"Error: Malformed line in movie file: '{line}'")
    return movies


def parse_histories(file_path):
    """
    Parses a history file and returns a list of sets representing user watch histories.

    :param file_path: Path to the history file.
    :return: List of sets, where each set contains watched movie IDs for a user.
    """
    lines = read_file(file_path)
    histories = []
    for line in lines:
        try:
            # Convert each line into a set of movie IDs
            histories.append(set(map(int, line.split(","))))
        except ValueError:
            print(f"Error: Malformed line in history file: '{line}'")
    return histories
