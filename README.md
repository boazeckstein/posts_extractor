# Posts Extractor

This Python project is designed to extract posts from various forum websites and save them to text files. It utilizes web scraping techniques to fetch HTML content from specified URLs, parse the HTML structure, and extract relevant information such as post titles, content, publication dates, and author names.

## Features

- Extract posts from different forum websites with varying HTML structures
- Save extracted posts to text files in JSON format
- Reformat publication dates to a consistent format
- Handle nested HTML elements for author information extraction

## Requirements

- Python 3.x
- requests library

## Usage

1. Clone the repository or download the source code from https://github.com/boazeckstein/posts_extractor.
2. Install the required dependencies by running `pip install requests`.
3. Run the `main.py` script using `python main.py`.
4. The extracted posts will be saved in the `phpbb_posts.txt` and `vbulletin_posts.txt` files in the same directory.

## File Structure

- `main.py`: The main entry point of the application, responsible for fetching HTML content and extracting posts.
- `post.py`: Defines the `Post` class to represent a forum post.
- `html_extractor.py`: Contains utility functions for extracting HTML elements based on tags and attributes.
- `utils.py`: Provides helper functions for fetching HTML content from URLs and reformatting dates.
- `handle_posts.py`: Handles the extraction of posts from HTML content and writing them to files.
