import os
from dotenv import load_dotenv

load_dotenv()
# API's KEYS AND TOKENS
DISCORD_TOKEN = os.getenv("DISCORD_SECRET")
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# Paths, URLs and other stuff

TESTO_FAMILIA = f"Essa é a familia, e nunca deixara de ser"

LOLAPI_BASE_URL = 'https://br1.api.riotgames.com'
PATCH_NOTES_URL = 'https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/'
LAST_PATCH_NOTE = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[0]/a'