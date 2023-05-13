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
        self.api_match_base_url = consts.LOL_MATCH_AMERICA_BASE_URL
        self.api_key = os.getenv('RIOT_API_KEY')
        self.http_client = HttpClient()

    def get_last_patch_notes(self):

        pass

        return response.text

    async def get_champion_info(self, champion):
        """
        Retorna informações sobre um campeão do League of Legends

        Args:
            champion (string): nome do campeão a ser buscado

        Returns:
            json: json com as informações do campeão
        """
        url = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/data/pt_BR/champion/{champion}.json'
        json_response = await self.http_client.get(url)
        return json_response

        
        return await json_response

    async def get_summoner_info_by_name(self, summoner_name):
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

    async def get_summoner_rank_by_id(self, summoner_id):
        """
        Retorna informações sobre o rank de um invocador do League of Legends

        Args:
            summoner_id (string): id do invocador a ser buscado

        Returns:
            json: json com as informações do rank do invocador
        """
        url = f'{self.api_base_url}/lol/league/v4/entries/by-summoner/{summoner_id}'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})
        return json_response


    async def get_last_match_info_by_name(self, summoner_name):
        """
        Retorna informações sobre a última partida de um invocador do League of Legends

        Args:
            summoner_name (string): nome do invocador a ser buscado

        Returns:
            json: json com as informações da última partida do invocador
        """

        summoner_info = await self.get_summoner_info_by_name(summoner_name)
        summoner_info["rank"] = await self.get_summoner_rank_by_id(summoner_info["id"])

        url = f'{self.api_match_base_url}/lol/match/v5/matches/by-puuid/{summoner_info["puuid"]}/ids?start=0&count=20'
        match_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})

        url = f'{self.api_match_base_url}/lol/match/v5/matches/{match_response[0]}'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})

        game_info = {
            'summoner_info': summoner_info,
            'game_mode': json_response['info']['gameMode'],
            'game_id': json_response['metadata']['matchId'],
            'participants': [],
            'summoner_stats': []
        }

        [game_info['participants'].append({'name': participant['summonerName'], 'champion': participant['championName']}) for participant in json_response['info']['participants']]

        [game_info['summoner_stats'].append({'kills': participant['kills'], 'deaths': participant['deaths'], 'assists': participant['assists'], 'champion': participant['championName'], 'kda': participant['challenges']['kda']}) for participant in json_response['info']['participants'] if participant['summonerName'] == summoner_info['name']]

        return game_info

    async def get_champion_mastery(self, summoner_id):
        url = f'{self.api_base_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})

        return json_response


    async def get_last_twenty_games_by_puuid(self, account_id):
        url = f'{self.api_base_url}/lol/match/v5/matches/by-puuid/{account_id}/ids?start=0&count=20'
        json_response = await self.http_client.get_with_headers(url=url, headers={'X-Riot-Token': self.api_key})

        return json_response

    async def get_summoner_profile(self, summoner_name):
        """Retorna o perfil de um invocador do League of Legends
        com as informações do invocador e dos 3 campeões com maior maestria

        Args:
            summoner_name (string): nome do invocador a ser buscado

        Returns:
            json: json com as informações do invocador e dos 3 campeões com maior maestria
        """
        #champion_mastery = await self.get_champion_mastery(summoner_info['id'])

        summoner_last_match_info = await self.get_last_match_info_by_name(summoner_name)

        profile = {
            'summoner_name': summoner_last_match_info['summoner_info']['name'],
            'level': summoner_last_match_info['summoner_info']['summonerLevel'],
            'profile_icon_id': summoner_last_match_info['summoner_info']['profileIconId'],
            'last_match': summoner_last_match_info
        }

        for champion in champion_mastery[:3]:

            all_champions = await self.http_client.get(url='https://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json')
            all_champions = all_champions['data']
            champion_name = [item for item in all_champions if str(champion['championId']) == str(all_champions[item]['key'])][0]
            champion_info = await self.get_champion_info(champion_name)

            champion_last_games = await self.get_last_twenty_games_by_puuid(summoner_info['puuid'])

            champion_status_data = []

            for match in champion_last_games:

                match_info = await self.http_client.get(url=f'{self.api_base_url}/lol/match/v5/matches/{match}')

                for participant in match_info['info']['participants']:

                    if participant['puuid'] == summoner_info['puuid'] and participant['championName'] == champion_name:

                        champion_status_data ={

                        }
                        champion['kills'] = participant['kills']
                        champion['deaths'] = participant['deaths']
                        champion['assists'] = participant['assists']
                        champion_data.append(participant)

                        break

            champion_data = {
                'name': champion_info['data'][f'{champion_name}']['name'],
                'level': champion['championLevel'],
                'points': champion['championPoints'],
                'status' : champion_status_data
            }
            profile['champions'].append(champion_data)

        return profile