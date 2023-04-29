import discord
from discord.ext import commands
import os

class DiscordClient:
    def __init__(self, intents):
        self.client = commands.Bot(command_prefix='!', intents=intents)

    def get_client(self):
        return self.client
