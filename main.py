import discord
import asyncio
import random
import botcheck
import time

client = discord.Client()
ishope = False
hope_user=[]
text_change_color_hint = "{} 完成了點圖！獲得了更換暱稱顏色的獎勵！:rainbow: 請下指令 ``i!idcolor @顏色``"
text_all_server_colors_hint = ":tada: 可以選的顏色："
text_not_member_can_draw = "目前沒有人可以點圖 :sob:"

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
	global ishope
	if(message.content == "Hello"):
		handle_hello(client, message)
	if(message.content.startswith("i!color")):
		await handle_color(client, message,'i!color')
		await print_all_choose_id(client, message)

	# check after i!hope, anyone finished picture
	if(message.content.startswith('i!done')): 
		if not botcheck.is_hope_channel(message):
			await client.send_message(message.channel,
			"error channel!!!")
			return
	
		if ishope == False:
			await client.send_message(message.channel,
			"no hope!!!!!!")
			return
		done_pic = message.content[len('i!done'):].strip()
		# check attach pic and http pic
		if not message.attachments and not botcheck.check_contain_http_img(done_pic):
			print('empty pic!!')
			return
		
		if(not botcheck.check_contain_http_img(done_pic) 
			and not botcheck.check_contain_http_img(message.attachments[0]['url'])):
			print('upload error data!!')
			return
		if not hope_user:
			print('no user')
			return

		done_bonus = False
		print(hope_user)
		# user who finished pic has id color changed permission
		if message.author.mention == hope_user[0].mention:
			done_bonus = True
			
		# other users have random chance
		if message.author.mention != hope_user[0].mention:
			bonus_chance_num = random.randint(1,10)
			print('bonus color chance {}'.format(bonus_chance_num))
			if bonus_chance_num == 5:
				done_bonus = True
		
		if done_bonus:
			hope_user.clear()
			await print_all_choose_id(client,message)
			global text_change_color_hint
			await client.send_message(message.channel,text_change_color_hint.format(message.author.mention))
			
			def check(message):
				return message.content.startswith('i!idcolor') and message.author.id!=client.user.id
			msg_answer = await client.wait_for_message(author = message.author,check = check)
			await handle_color(client,msg_answer,'i!idcolor')

	if(message.content.startswith('i!hope')): 
		if not botcheck.is_hope_channel(message):
			await client.send_message(message.channel,
			"error channel!!!")
			return

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
			global text_not_member_can_draw
			await client.send_message(message.channel,text_not_member_can_draw)
			return

		new_member = random.choice(member_names)
		print(new_member)
		print(new_member.status)
		ishope = True
		hope_user.append(new_member)
		await client.send_message(message.channel,
			"{} 許願說要 ".format(message.author.mention)+new_member.mention+" 畫 "+hope_topic)
		
async def handle_hello(client,message):
	await client.send_message(message.channel,"World")

async def handle_color(client,message,bot_command):
	choose_color = message.content[len(bot_command):].strip()
	print(choose_color)

	if(not choose_color):
		print('You never choose color!!')
		return
	if(botcheck.check_is_error_color_mentions(message.server.roles,choose_color)):
		print('You choose error color!!')
		return

	role = discord.utils.get(message.server.roles, mention=choose_color)

	while(botcheck.check_all_color_roles_list(message.author.roles)):
		for arole in message.author.roles:
			name = arole.name
			print(name)
			if(botcheck.is_all_color_roles(name)):
				print(name)
				await client.remove_roles(message.author, arole)
		print('sleep')
		time.sleep(1)
		pass

	print('add_roles')
	await client.add_roles(message.author, role)
		
async def print_all_choose_id(client,message):
	role_str = ''
	for role in message.server.roles:
		if(botcheck.is_all_color_roles(role.name)):
			role_str+=" "+ role.mention

	global text_all_server_colors_hint
	await client.send_message(message.channel,text_all_server_colors_hint+role_str)

client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
