import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('log in')
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):
	if(message.content == "Hello"):
		await client.send_message(message.channel,"World")

client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
