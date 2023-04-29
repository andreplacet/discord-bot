import requests
from bs4 import BeautifulSoup

class LeagueLegends:
    def __init__(self):
        self.patch_notes_url = 'https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/'

    def get_last_patch_notes(self):
        response = requests.get(self.patch_notes_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        img = soup.find('a', {'class': 'post-list__item__image'})

        return response.text