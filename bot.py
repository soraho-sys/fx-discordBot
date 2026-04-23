import discord
import requests
import os

TOKEN = os.environ["TOKEN"]
API_URL = "https://your-antigravity-api.com/chat"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot起動")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        res = requests.post(API_URL, json={
            "message": message.content
        })
        data = res.json()
        reply = data.get("reply", "エラー")
    except:
        reply = "現在システム応答なし"

    await message.channel.send(reply)

client.run(TOKEN)
