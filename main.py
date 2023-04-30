import discord
from discord.ext import commands
from client	import DiscordClient
import os
import sys
import requests
import json
import consts
from league_of_legends import LeagueLegends


##### configuração do bot #####
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.message_content = True
client = DiscordClient(intents).get_client()

##### instanciamento de classes #####
lol = LeagueLegends()

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