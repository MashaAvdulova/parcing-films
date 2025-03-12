import requests
from bs4 import BeautifulSoup


def parsing_film():
    url = 'https://en.wikipedia.org/wiki/Lists_of_films#By_topic'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url, headers=headers)
    films = ''
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # content = soup.find('div', class_='mw-content-ltr mw-parser-output')
        # start = content.find_all('h2', id='By_topic')
        # films_content = content.find_next_siblings()

        # print(films_content)
    return films


def write_film_text (films: str):
    with open ('films.txt', 'w', encoding='utf-8') as file:
        text = file.write(films)

films = parsing_film()
write_film_text(films)
