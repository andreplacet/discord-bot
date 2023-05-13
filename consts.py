import os
from dotenv import load_dotenv

load_dotenv()
# API's KEYS AND TOKENS
DISCORD_TOKEN = os.getenv("DISCORD_SECRET")
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Paths, URLs and other stuff

TESTO_FAMILIA = f"Essa é a familia, e nunca deixara de ser"

LOLAPI_BASE_URL = 'https://br1.api.riotgames.com'
LOL_MATCH_AMERICA_BASE_URL = 'https://americas.api.riotgames.com'
PATCH_NOTES_URL = 'https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/'
LAST_PATCH_NOTE = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/div[1]/div/ol/li[0]/a'


RANK_ICON = {
    'IRON': r'img\ranked-emblem\emblem-bronze.png',
    'BRONZE': r'img\ranked-emblem\emblem-bronze.png',
    'SILVER': r'img\ranked-emblem\emblem-silver.png',
    'GOLD': r'img\ranked-emblem\emblem-gold.png',
    'PLATINUM': r'img\ranked-emblem\emblem-platinum.png',
    'DIAMOND': r'img/ranked-emblem/emblem-diamond.png',
    'MASTER': r'img\ranked-emblem\emblem-master.png',
    'GRANDMASTER': r'img\ranked-emblem\emblem-grandmaster.png',
    'CHALLENGER': r'img\ranked-emblem\emblem-challenger.png',   
}

RANK_ICON_URL = {
    'IRON' : 'https://static.wikia.nocookie.net/leagueoflegends/images/f/fe/Season_2022_-_Iron.png/revision/latest?cb=20220105213520',
    'BRONZE' : 'https://static.wikia.nocookie.net/leagueoflegends/images/e/e9/Season_2022_-_Bronze.png/revision/latest?cb=20220105214224',
    'SILVER' : 'https://static.wikia.nocookie.net/leagueoflegends/images/4/44/Season_2022_-_Silver.png/revision/latest?cb=20220105214225',
    'GOLD' : 'https://static.wikia.nocookie.net/leagueoflegends/images/8/8d/Season_2022_-_Gold.png/revision/latest?cb=20220105214225',
    'PLATINUM' : 'https://static.wikia.nocookie.net/leagueoflegends/images/3/3b/Season_2022_-_Platinum.png/revision/latest?cb=20220105214225',
    'DIAMOND' : 'https://static.wikia.nocookie.net/leagueoflegends/images/e/ee/Season_2022_-_Diamond.png/revision/latest?cb=20220105214226',
    'MASTER' : 'https://static.wikia.nocookie.net/leagueoflegends/images/e/eb/Season_2022_-_Master.png/revision/latest?cb=20220105214311',
    'GRANDMASTER' : 'https://static.wikia.nocookie.net/leagueoflegends/images/f/fc/Season_2022_-_Grandmaster.png/revision/latest?cb=20220105214312',
    'CHALLENGER' : 'https://static.wikia.nocookie.net/leagueoflegends/images/0/02/Season_2022_-_Challenger.png/revision/latest?cb=20220105214312',
}

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# FFMPEG

FFMPEG_OPTIONS = {
    'options': '-vn -b:a 128k',  # Set audio bitrate to 128kbps
    'executable': r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin',  # Path to the FFmpeg binary
    'before_options': '-vol 100',  # Set audio volume to 500%
}