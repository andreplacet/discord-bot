import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import consts

load_dotenv()

class LeagueLegends:
    def __init__(self):
        self.patch_notes_url = 'https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/'
        self.api_base_url = consts.LOLAPI_BASE_URL
        self.api_key = os.getenv('RIOT_API_KEY')

    def get_last_patch_notes(self):

        response = requests.get(self.patch_notes_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img = soup.find('a', {'class': 'post-list__item__image'})

        return response.text

    async def get_champion_info(self, champion):
        """
        Retorna informações sobre um campeão do League of Legends

        Args:
            champion (string): nome do campeão a ser buscado

        Returns:
            json: json com as informações do campeão
        """

        url = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/data/pt_BR/champion/{champion.capitalize()}.json'
        response = requests.get(url)
        json_response = json.loads(response.text)
        
        return await json_response

    def get_summoner_info_by_name(self, summoner_name):
        """
        Retorna informações sobre um invocador do League of Legends

        Args:
            summoner_name (string): nome do invocador a ser buscado

        Returns:
            json: json com as informações do invocador
        """
        response = requests.head(f'{self.api_base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}', headers={'X-Riot-Token': self.api_key})
        json_response = json.loads(response.text)

        return json_response