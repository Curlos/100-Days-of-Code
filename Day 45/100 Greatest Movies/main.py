from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
movies = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")[:-1]
movieTitles = []

for movie in movies:
    movieTitle = movie.getText().replace('\n', '').replace('\xa0', ' ').strip(' ') + '\n'
    movieTitles.append(movieTitle)

with open('100 Best Movies of All Time.txt', mode="w") as file:
    file.writelines(movieTitles)

print('All movies written to file!')