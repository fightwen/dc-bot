import requests
import json
import discord
import bottext
import random

motion_key = ['whatever','confused','crazy','table','love','angry','hurt','happy','excited','surprised',
'shy','worried','evil','friends','sad','scarred','hugging','sleeping','thinking','cat','monkey']

async def request_jp_emotion(client,message):
	endpoint = "https://raw.githubusercontent.com/venam/emoji/master/emoji.json"

	response = requests.get(endpoint)
	print(response.text)
	
	emotion_text = response.json()

	global motion_key
	one_motion_key = random.choice(motion_key)
	print(one_motion_key)

	one_motion = random.choice(emotion_text[one_motion_key])
	print(one_motion)

	embed = discord.Embed(title=':pencil2: 顏文字 '+one_motion_key, description=one_motion)

	await client.send_message(message.channel,bottext.get_text_kaomoji().format(message.author.mention))
	await client.send_message(message.channel,embed=embed)

async def request_gh_emotion(client,message):
	endpoint = "https://api.github.com/emojis"

	response = requests.get(endpoint)
	
	emotion_text = response.json()
	one_motion_key_index = random.randint(0,len(emotion_text.keys()) - 1)

	one_motion_key = list(emotion_text.keys())[one_motion_key_index]
	one_motion_link = emotion_text[one_motion_key]

	embed = discord.Embed(title=':pencil2: emoji ', description=one_motion_key)
	embed.set_image(url = one_motion_link)

	await client.send_message(message.channel,bottext.get_text_emoji().format(message.author.mention))
	await client.send_message(message.channel,embed=embed)




