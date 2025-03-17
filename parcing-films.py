import requests
from bs4 import BeautifulSoup


def parsing_film():
    url = 'https://en.wikipedia.org/wiki/Lists_of_films#By_topic'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headers_item = soup.find_all('div', class_='mw-heading mw-heading3')
        start = 0
        for ind, item in enumerate(headers_item):
            if item.find('h3')['id'] == 'Historical':
                start = ind
        for item in headers_item[start:]:
                list_of_titles = item.next_sibling.next_sibling
                for ul in list_of_titles.find_all('li'):
                    title = ul.find('a').text
                    link = ul.find('a')['href']
                    print(f'Заголовок - {title}, ссылка - http://{link}')
                if item.next_sibling.next_sibling.next_sibling.next_sibling['class'][1] =='nw-heading2':
                    break


# def write_film_text (films: str):
#     with open ('films.txt', 'w', encoding='utf-8') as file:
#         text = file.write(films)

parsing_film()