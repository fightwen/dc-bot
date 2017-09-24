import discord
import asyncio
import random

client = discord.Client()
ishope = False
role_names=["red","blue","green"]

@client.event
async def on_ready():
	print('log in')
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):
	if(message.content == "Hello"):
		await client.send_message(message.channel,"World")
	if(message.content.startswith("i!color")):
		choose_color = message.content[len('i!color'):].strip()
		print(choose_color)

		if(not choose_color):
			print('You never choose color!!')
			return
		if(check_is_error_color_mentions(message.server.roles,choose_color)):
			print('You choose error color!!')
			return


		role = discord.utils.get(message.server.roles, mention=choose_color)

		for arole in message.author.roles:
			name = arole.name
			print(name)
			if(is_all_color_roles(name)):
				print(name)
				await client.remove_roles(message.author, arole)
		await client.add_roles(message.author, role)

		role_str = ''
		for role in message.server.roles:
			if(is_all_color_roles(role.name)):
				role_str+=" "+ role.mention
		
		await client.send_message(message.channel,
			"You can choose "+role_str)
	if(message.content.startswith('i!hope')): 
		if not is_hope_channel(message):
			await client.send_message(message.channel,
			"error channel!!!")
			return
		global ishope
		if ishope == True:
			await client.send_message(message.channel,
			"is done!!!!!!")
			return

		member_names = []
		for member in client.get_all_members():
			print(member)
			print(member.bot)
			if(member.bot == False 
				and member.status == discord.Status.online 
				and message.author!=member):
				member_names.append(member)

		if(not member_names):
			await client.send_message(message.channel,
			"目前沒有人可以點圖 :sob:")
			return

		new_member = random.choice(member_names)
		print(new_member)
		print(new_member.status)
		ishope = True
		await client.send_message(message.channel,
			"{} 許願說要 ".format(message.author.mention)+new_member.mention+" 畫 xxxx")


def is_hope_channel(message):
	if message.channel.id == '357191670825091084':
		return True
	return False

def is_all_color_roles(role_name):
	if "*" in role_name:
		return True
	return False 

def check_is_error_color_mentions(roles,mention):
	is_error_mention = True
	for role in roles:
		if role.mention == mention:
			is_error_mention =  False

	return is_error_mention

client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
