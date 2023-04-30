import discord
from discord.ext import commands
from client	import DiscordClient
import os
import sys
import requests
import json
import consts


##### configuração do bot #####
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.message_content = True
client = DiscordClient(intents).get_client()

###### serviços do bot #####
@client.event
async def on_ready():
	print('bot online')

@client.command(name='ping')
async def hello(ctx):
  await ctx.send('Pong!')

##### league of legends #####
@client.command(name='patch', help='Retorna o link do último patch notes')
async def patch_notes(ctx):
  response = requests.get(consts.PATCH_NOTES_URL)
  img = response
  await ctx.send(img['href'])


@client.command(name='summoner', help='Retorna informações sobre um invocador do League of Legends')
async def summoner(ctx, *arg):
  comprehension = '%20'.join(arg)
  response = requests.get(f'{consts.LOLAPI_BASE_URL}/lol/summoner/v4/summoners/by-name/{comprehension}', headers={'X-Riot-Token': consts.RIOT_API_KEY})
  if response.status_code == 200:
    json_response = json.loads(response.text)
    embed = discord.Embed(description=f'Level: {json_response["summonerLevel"]}', title=json_response["name"])
    embed.set_thumbnail(url=f'http://ddragon.leagueoflegends.com/cdn/13.8.1/img/profileicon/{json_response["profileIconId"]}.png')
  else:
    embed = discord.Embed(description=f'Invocador não encontrado', title=':/')
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

client.run(consts.DISCORD_TOKEN)