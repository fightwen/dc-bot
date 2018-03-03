import requests
import json
import discord
import bottext

async def request_color(client,message):
	embed = request_color_embed(client,message)

	await client.send_message(message.channel,bottext.get_text_color().format(message.author.mention))
	await client.send_message(message.channel,embed=embed)

def request_color_embed(client,message):
	endpoint = "http://www.colourlovers.com/api/colors/random?format=json"

	response = requests.get(endpoint)
	print(response.text)

	color_text = response.json()
	print(color_text[0]['imageUrl'])
	embed = discord.Embed(title=':dividers: 顏色卡', description='色碼：'+color_text[0]['hex'], color=int(color_text[0]['hex'],16))
	embed.set_image(url = color_text[0]['imageUrl'])
	return embed

async def request_palettes(client,message):
	embed = request_palettes_embed(client,message)

	await client.send_message(message.channel,bottext.get_text_palettes().format(message.author.mention))
	await client.send_message(message.channel,embed=embed)

def request_palettes_embed(client,message):
	endpoint = "http://www.colourlovers.com/api/palettes/random?format=json"

	response = requests.get(endpoint)
	print(response.text)

	color_text = response.json()
	print(color_text[0]['imageUrl'])

	palettes_hex=''
	index = 0
	for color in color_text[0]['colors']:

		if index+1 is len(color_text[0]['colors']):
			palettes_hex += color
		else:
			palettes_hex += color + ', '
		index+=1


	 
	embed = discord.Embed(title=':confetti_ball: 色票卡', description='色碼：'+palettes_hex, color=int(color_text[0]['colors'][0],16))
	embed.set_image(url = color_text[0]['imageUrl'])

	return embed


async def request_patterns(client,message):
	
	embed = request_patterns_embed(client,message)

	await client.send_message(message.channel,bottext.get_text_patterns().format(message.author.mention))
	await client.send_message(message.channel,embed=embed)

def request_patterns_embed(client,message):
	endpoint = "http://www.colourlovers.com/api/patterns/random?format=json"

	response = requests.get(endpoint)
	print(response.text)

	color_text = response.json()
	print(color_text[0]['imageUrl'])

	palettes_hex=''
	index = 0
	for color in color_text[0]['colors']:

		if index+1 is len(color_text[0]['colors']):
			palettes_hex += color
		else:
			palettes_hex += color + ', '
		index+=1


	 
	embed = discord.Embed(title=':ribbon: 樣式卡', description='色碼：'+palettes_hex, color=int(color_text[0]['colors'][0],16))
	embed.set_image(url = color_text[0]['imageUrl'])
	embed.add_field(name="作者", value='['+color_text[0]['userName']+']('+color_text[0]['url']+')')
	return embed

	