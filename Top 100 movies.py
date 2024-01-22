from bs4 import BeautifulSoup
import requests

URL = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = URL.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_='title')

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
print(movies)

with open("top_100.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")



