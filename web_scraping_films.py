import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the HTML content of the webpage
response = requests.get(URL)
website_html = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie title elements
movies = soup.find_all("h3", class_="title")

# Extract the text from each title element
movie_titles = [movie.getText() for movie in movies]


movie_titles = movie_titles[::-1]

# Write the movie titles to a file
with open("movies.txt", "w") as file:
    for title in movie_titles:
        file.write(title + "\n")
