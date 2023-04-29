import discord
from discord.ext import commands
from client	import DiscordClient
from dotenv import load_dotenv
import os
import sys
import requests
import json
import consts

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_SECRET")

sys.path.append("D:\dev\alpha-bot\img")

# configuração do bot
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.message_content = True

client = DiscordClient(intents).get_client()

@client.event
async def on_ready():
	print('bot online')

@client.command(name='ping')
async def hello(ctx):
  await ctx.send('Pong!')

@client.command(name='lol')
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


@client.command(name='familia')
async def familia(ctx):
  description = consts.TESTO_FAMILIA
  file = discord.File("D:/dev/alpha-bot/img/familia.png", filename="familia.png")
  embed = discord.Embed(description=description, title='OS HOMENS')
  embed.set_image(url='attachment://familia.png')
  await ctx.send(file=file, embed=embed)

@familia.error
async def familia_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send('erro ao enviar o comando')

client.run(DISCORD_TOKEN)