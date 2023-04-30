from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import consts
from aiohttp_client import HttpClient

load_dotenv()

class LeagueLegends:
    def __init__(self):
        self.patch_notes_url = 'https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/'
        self.api_base_url = consts.LOLAPI_BASE_URL
        self.api_key = os.getenv('RIOT_API_KEY')
        self.http_client = HttpClient()

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
        json_response = await self.http_client.get(url)
        return json_response

        
        return await json_response

    def get_summoner_info_by_name(self, summoner_name):
        """
        Retorna informações sobre um invocador do League of Legends

        Args:
            summoner_name (string): nome do invocador a ser buscado

        Returns:
            json: json com as informações do invocador
        """
        url = f'{self.api_base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})
        return json_response

    async def get_champion_mastery(self, summoner_id):
        url = f'{self.api_base_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})

        return json_response

    async def get_summoner_profile(self, summoner_name):
        summoner_info = await self.get_summoner_info_by_name(summoner_name)
        champion_mastery = await self.get_champion_mastery(summoner_info['id'])

        profile = {
            'summoner_name': summoner_info['name'],
            'level': summoner_info['summonerLevel'],
            'profile_icon_id': summoner_info['profileIconId'],
            'champions': []
        }

        for champion in champion_mastery[:3]:
            champion_info = await self.get_champion_info(champion['championId'])
            champion_data = {
                'name': champion_info['name'],
                'level': champion['championLevel'],
                'points': champion['championPoints'],
                'kda': int((champion['kills'] + champion['assists']) / champion['deaths'])
            }
            profile['champions'].append(champion_data)

        return profile