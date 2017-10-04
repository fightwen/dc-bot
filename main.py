import discord
import asyncio
import random
import botcheck
import time
import bottext

client = discord.Client()
test_mode = False
ishope = False
hope_user=[]
hope_time = 1.0
current_hope = ""

@client.event
async def on_ready():
	print('log in')
	print(client.user.name)
	print(client.user.id)
	await client.change_presence(game = discord.Game(name=bottext.get_bot_cmd(test_mode)+"!help"))

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
	global hope_time
	global test_mode
	global current_hope
	bot_cmd = bottext.get_bot_cmd(test_mode)
	if(message.content == "Hello"):
		handle_hello(client, message)
	if message.content == bot_cmd+"!who":
		await client.send_message(message.channel,bottext.get_text_who())
	if message.content == bot_cmd+"!help":
		await client.send_message(message.channel,bottext.get_text_help())
	if message.content == bot_cmd+"!rule":
		await client.send_message(message.author,bottext.get_text_rule())
		await client.delete_message(message)
	if(message.content.startswith(bot_cmd+"!color")):
		if not test_mode:
			return
		await handle_color(client, message,bot_cmd+'!color')
		await print_all_choose_id(client, message)
	if(message.content.startswith(bot_cmd+"!idcolor x")):
		await del_all_colors(client,message)

	# check after i!hope, anyone finished picture
	if(message.content.startswith(bot_cmd+'!done')): 
		hope_channel_id = get_hope_channel_id(test_mode)
		if not botcheck.is_hope_channel(message,hope_channel_id):
			await error_channel_msg(client, message)
			return

		done_pic = message.content[len(bot_cmd+'!done'):].strip()
		# check attach pic and http pic
		if not message.attachments and not botcheck.check_contain_http_img(done_pic):
			print('empty pic!!')
			await client.delete_message(message)
			return
	
		if ishope == False:
			await client.send_message(message.channel,bottext.get_text_nobody_hope().format(message.author.mention,message.author.mention,message.author.mention))
			return
		
		
		if(not botcheck.check_contain_http_img(done_pic) 
			and not botcheck.check_contain_http_img(message.attachments[0]['url'])):
			print('upload error data!!')
			return
		done_bonus = check_user_has_hope_bonus(message, hope_user)
		
		if done_bonus:
			hope_user.clear()
			await print_all_choose_id(client,message)
			await client.send_message(message.channel,bottext.get_text_change_color_hint().format(message.author.mention))
			
			def check(message):
				return message.content.startswith(bot_cmd+'!idcolor') and message.author.id!=client.user.id
			msg_answer = await client.wait_for_message(timeout=60,author = message.author,check = check)

			if not msg_answer:
				print('time out!!')
				return
			await handle_color(client,msg_answer,bot_cmd+'!idcolor')

	if(message.content.startswith(bot_cmd+'!hope')): 
		await client.delete_message(message)
		hope_channel_id = get_hope_channel_id(test_mode)
		if not botcheck.is_hope_channel(message,hope_channel_id):
			await error_channel_msg(client, message)
			return

		if time.time() - hope_time >= 60*60*24:
			ishope = False 

		if ishope == True:
			
			next_hope_time = hope_time + 60*60*24
			next_hope_time_str = time.asctime(time.localtime(next_hope_time))

			await client.send_message(message.channel,bottext.get_text_next_hope().format(next_hope_time_str))
			
			# remind user hope info again
			if not current_hope:
				return
			await client.send_message(message.channel,current_hope)
			return
		hope_topic = message.content[len(bot_cmd+'!hope'):].strip()
		if(not hope_topic):
			print('You never choose topic!!')
			return

		# user need to lv1 to hope
		has_permission = botcheck.check_lv1_permission(message)
		if not has_permission:
			await client.send_message(message.channel,bottext.get_text_hope_no_permission().format(message.author.mention))
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
			await client.send_message(message.channel,bottext.get_text_not_member_can_draw())
			return

		new_member = random.choice(member_names)
		print(new_member)
		print(new_member.status)
		ishope = True
		hope_user.append(new_member)

		hope_time = time.time()

		hope_info = "{} 許願說要 ".format(message.author.mention) +new_member.mention+" 畫 :star2: ``"+hope_topic+"``  :star2:"
		await client.send_message(message.channel,hope_info)

		hope_channel_url = bottext.get_server_hope_url()
		await client.send_message(new_member,hope_info+"\n"+bottext.get_text_hope_dm().format(new_member.mention,message.server.name,message.channel.name,hope_channel_url))

		current_hope = hope_info
		
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

	await del_all_colors(client,message)

	print('add_roles')
	await client.add_roles(message.author, role)
		
async def print_all_choose_id(client,message):
	role_str = ''
	for role in message.server.roles:
		if(botcheck.is_all_color_roles(role.name)):
			role_str+=" "+ role.mention

	await client.send_message(message.channel,bottext.get_text_all_server_colors_hint()+role_str)

async def error_channel_msg(client,message):
	await client.send_message(message.channel,bottext.get_text_error_hope_channel())

def get_hope_channel_id(test_mode):
	if test_mode:
		return '357191670825091084'
	else:
		return '364395456379486218'

async def del_all_colors(client,message):
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

def check_user_has_hope_bonus(message,hope_user):
	if not hope_user:
		print('no hope_user')

	done_bonus = False
	print(hope_user)

	# other users have random chance
	if not hope_user or message.author.mention != hope_user[0].mention:
		bonus_chance_num = random.randint(1,10)
		print('bonus color chance {}'.format(bonus_chance_num))
		if bonus_chance_num == 5:
			done_bonus = True

	# user who finished pic has id color changed permission
	if hope_user and message.author.mention == hope_user[0].mention:
		done_bonus = True

	return done_bonus
	
		


if test_mode:
	client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
else:
	client.run("MzY0MDA1MTE2NDM0NTc5NDU2.DLXirQ.BxTq4iQKodHq9Whxlsih1YPS9Ho")