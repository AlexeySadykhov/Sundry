from bs4 import BeautifulSoup
import requests

def get_names(URL):
    page_response = requests.get(URL, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    array = [ ]
    for i in page_content.find_all('div', {'class': 'div-col'}):
        links = i.find_all('a', href=True)
        for link in links:
            title = link.get('title')
            array.append(title)
    return array

url = 'https://en.wikipedia.org/wiki/List_of_current_automobile_marques'
print(get_names(url))
print('Number of names:', len(get_names(url)))
