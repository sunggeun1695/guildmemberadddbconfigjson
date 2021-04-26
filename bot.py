"""
by 로쏠호 (대충 이거 있으면은 안켜지니까 " 안에있는거 다 지우세요 " 까지)
"""

from sqlite3.dbapi2 import Cursor
import discord
import json
import os
import sqlite3
from discord.ext import commands

bot = discord.Client(Intents=discord.Intents.all())

with open("config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    access_token = configData["live_token"]

@bot.event
async def on_ready():
    print(f'[ ! ] {bot.user.id}로 로그인 했습니다.')
    
db = sqlite3.connect('expData.db')
db.cursor()

@bot.event
async def on_guildMemberAdd(member):
    channels = member.guild.systemChannel
    channels.send(f'{member}님, {member.guild.name}에 오신것을 환영해요!')
    
async def on_guildMemberRemove(member):
    channels = member.guild.systemChannel
    channels.send(f'{member}님! {member.guild.name}서버가 싫어서 나가셨나요?\n아니면은 학원, 여행 등등의 일로 나가셨나요?\n다시 돌아오세요 ㅜㅠ')

bot.run(access_token)
    