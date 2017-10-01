import discord
import asyncio
import random
import botcheck
import json

client = discord.Client()
ishope = False


@client.event
async def on_ready():
	print('log in')
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_reaction_add(reaction, user):
	print(user.name)
	print(reaction)

@client.event
async def on_message(message):
	print(message.content)
	print(message.attachments)
	print(message.reactions)
	if(message.content == "Hello"):
		await client.send_message(message.channel,"World")
	if(message.content.startswith("i!color")):
		choose_color = message.content[len('i!color'):].strip()
		print(choose_color)

		if(not choose_color):
			print('You never choose color!!')
			return
		if(botcheck.check_is_error_color_mentions(message.server.roles,choose_color)):
			print('You choose error color!!')
			return


		role = discord.utils.get(message.server.roles, mention=choose_color)

		for arole in message.author.roles:
			name = arole.name
			print(name)
			if(botcheck.is_all_color_roles(name)):
				print(name)
				await client.remove_roles(message.author, arole)
		await client.add_roles(message.author, role)

		role_str = ''
		for role in message.server.roles:
			if(botcheck.is_all_color_roles(role.name)):
				role_str+=" "+ role.mention
		
		await client.send_message(message.channel,
			"You can choose "+role_str)

	# check after i!hope, anyone finished picture
	if(message.content.startswith('i!done')): 
		if not botcheck.is_hope_channel(message):
			await client.send_message(message.channel,
			"error channel!!!")
			return
		global ishope
		if ishope == False:
			await client.send_message(message.channel,
			"no hope!!!!!!")
			return
		done_pic = message.content[len('i!done'):].strip()
		# check attach pic and http pic
		if not message.attachments and !botcheck.check_contain_http_img(done_pic):
			print('empty pic!!')
			return
		
		if(not botcheck.check_contain_http_img(message.attachments[0]['url'])):
			print('upload error data!!')
			return

		print (message.attachments[0]['url'])

	if(message.content.startswith('i!hope')): 
		if not botcheck.is_hope_channel(message):
			await client.send_message(message.channel,
			"error channel!!!")
			return

		global ishope
		if ishope == True:
			await client.send_message(message.channel,
			"is done!!!!!!")
			return
		hope_topic = message.content[len('i!hope'):].strip()
		if(not hope_topic):
			print('You never choose topic!!')
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
			"{} 許願說要 ".format(message.author.mention)+new_member.mention+" 畫 "+hope_topic)
		
			
		


client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
