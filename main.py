import discord
from discord import Permissions
from discord.ext import commands
from client	import DiscordClient
import requests
import json
import consts
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from league_of_legends import LeagueLegends


##### configuração do bot #####
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.message_content = True
permissions = Permissions(permissions=3145728)
client = DiscordClient(intents=intents, permissions=permissions).get_client()
sp = Spotify(auth_manager=SpotifyClientCredentials(client_id=consts.SPOTIFY_CLIENT_ID, client_secret=consts.SPOTIFY_CLIENT_SECRET))

##### instanciamento de classes #####
lol = LeagueLegends()

###### serviços do bot #####
@client.event
async def on_ready():
	print('bot online')

@client.command(name='ping')
async def hello(ctx):
  await ctx.send('Pong!')

                
@client.command(name='play', help='Toca uma música do Spotify')
async def play(ctx, *track_name):
    voice_client = None
    track_name = ' '.join(track_name)
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        try:
            voice_client = await voice_channel.connect()
        except discord.errors.ClientException:
            voice_client = ctx.author.voice.client
            channel = voice_client.channel

        if voice_client.is_playing():
            voice_client.stop()

        try:
            results = sp.search(q=track_name, limit=1, type='track')
            track_uri = results['tracks']['items'][0]['uri']
            source = await discord.FFmpegOpusAudio.from_probe(track_uri)
            voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f'Now playing: {url}')
        except Exception as e:
            await ctx.send(f'Error: {str(e)}')

@client.command(name='stop', help='Stops and disconnects the bot from voice')
async def stop(ctx):
    # Stop playback and disconnect from the voice channel
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    await voice_client.disconnect()


##### league of legends #####
@client.command(name='patch', help='Retorna o link do último patch notes')
async def patch_notes(ctx):
  response = requests.get(consts.PATCH_NOTES_URL)
  img = response
  await ctx.send(img['href'])


@client.command(name='summoner', help='Retorna informações sobre um invocador do League of Legends')
async def summoner(ctx, *arg):
  comprehension = '%20'.join(arg)
  json_response = await lol.get_summoner_profile(comprehension)
  embed = discord.Embed(description=f'Level: {json_response["level"]}', title=json_response["summoner_name"])
  
  embed.set_thumbnail(url=f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/profileicon/{json_response["profile_icon_id"]}.png')
  embed = discord.Embed(description=f'Invocador não encontrado', title=':/')
  await ctx.send(embed=embed)

@client.command(name='champion', help='Retorna informações sobre um campeão do League of Legends')
async def champion(ctx, arg):
  info = await lol.get_champion_info(arg)
  if not info:
    embed = discord.Embed(description=f'Campeão não encontrado', title=':/')
  else:
    embed = discord.Embed(description=f'{info["data"][arg.capitalize()]["lore"]}', title=arg.capitalize())
    embed.set_thumbnail(url=f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/champion/{info["data"][arg.capitalize()]["image"]["full"]}')

  await ctx.send(embed=embed)


@client.command(name='lol', help='Retorna informações sobre um campeão do League of Legends')
async def league_of_legends(ctx, arg1):
  url = f'http://ddragon.leagueoflegends.com/cdn/13.8.1/data/pt_BR/champion/{arg1.capitalize()}.json'
  response = requests.get(url)
  json_response = json.loads(response.text)
  embed = discord.Embed(description=f'{json_response["data"][arg1.capitalize()]["lore"]}', title=arg1.capitalize())
  embed.set_thumbnail(url=f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/champion/{json_response["data"][arg1.capitalize()]["image"]["full"]}')
  await ctx.send(embed=embed)

@league_of_legends.error
async def league_of_legends_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Campeão não encontrado. Tente novamente.')

##### fim league of legends #####
@client.command(name='familia')
async def familia(ctx):
  description = consts.TESTO_FAMILIA
  file = discord.File("D:/dev/alpha-bot/img/familia.png", filename="familia.png")
  embed = discord.Embed(description=description, title='OS HOMENS')
  embed.set_image(url='attachment://familia.png' )
  await ctx.send(file=file, embed=embed)

@familia.error
async def familia_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send('erro ao enviar o comando')

@client.command(name='fabio')
async def fabio(ctx):
  file = discord.File("D:/dev/alpha-bot/img/fabinho-legal.jpg", filename="fabinho-legal.jpg")
  embed = discord.Embed(description='Fábio é um cara muito legal', title='Fábio')
  embed.set_image(url='attachment://fabinho-legal.jpg')
  await ctx.send(embed=embed, file=file)

@client.command(name='nadamais')
async def nadamais(ctx):
  file = discord.File("D:/dev/alpha-bot/img/fabinho.jpg", filename="fabinho.jpg")
  embed = discord.Embed(description='QUE UM TILTE', title='Nada mais, nada menos...')
  embed.set_image(url='attachment://fabinho-legal.jpg')
  await ctx.send(embed=embed, file=file)

client.run(consts.DISCORD_TOKEN)