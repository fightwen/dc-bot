import discord
import asyncio
import random
import botcheck
import time

client = discord.Client()
test_mode = False
ishope = False
hope_user=[]
hope_time = 1.0
text_change_color_hint = "{} 完成了點圖！獲得了更換暱稱顏色的獎勵！:rainbow: 請下指令 ``i!idcolor @顏色``  \n請注意只能更改一次，不要打錯字了:yum:\n:arrow_up_small: 一分鐘後換色權利會過期 ，請趕快選擇"
text_all_server_colors_hint = ":tada: 可以選的顏色："
text_not_member_can_draw = "目前沒有人可以點圖 :sob:"
text_error_hope_channel = "錯誤的頻道！請到點圖頻道 :stuck_out_tongue_closed_eyes:"
text_nobody_hope = "現在根本沒人點圖 :flushed: ，但還是感謝 {0} 貢獻畫作！ :two_hearts: 感恩 {1}！ 讚嘆 {2}！"
text_next_hope = ":bangbang: 點圖進行中，下次可點圖時間為  {} :alarm_clock:"

text_who = "__**姓名**__：下午茶秘書\n"+"__**誕生日**__：2017/10/03\n"+"__**身高**__：不明\n"+"__**喜歡**__：滿滿的大自介\n"+"__**討厭**__：等你寫自介\n"+"__**造型**__：ahmin\n https://cdn.discordapp.com/avatars/364005116434579456/e4ede0ff346a6d435ec829000c7b9841.jpg"
text_help = "您好！我是下午茶秘書\n"+"任何活動，任何需求，看心情決定是否為您實現 :closed_book:\n" +":small_orange_diamond: ``i!help`` = 秘書處理的所有業務資料\n"+":small_blue_diamond: ``i!who``  = 秘書身家調查\n"+":small_orange_diamond: ``i!rule``  = 可獲取一份 #daily-hope 點圖許願池說明書"
text_rule ="點圖許願池說明書 :ok_hand: 祝您玩得愉快。\n```css\n[i!hope 點圖主題]   \n{ex: i!hope 貓咪擬人}\n\n>  每一天只能一次使用 ，如果其他人使用了點圖，則需要隔一天才能再次點圖。\n(請慎選你的點圖主題。選錯送出無法改)\n會隨機指定出目前在線上的用戶完成點圖，如果想被點到者，狀態必須是線上。\n(非閒置、離線、勿擾狀態)\n\n[i!done 圖片網址或是圖片附件] \n{ex: i!done https://images.xxxxxx.jpg}\n\n>  點圖畫好了使用的指令，如果你是被點到的對象，可獲得一次改暱稱顏色的機會，如果不是，使用此指令還是會隨機獲得一次改暱稱顏色的機會。\n--------------------------------------------------------\n任何作弊行為會被視為病毒永久隔離( ×ω× )\n如果有問題請洽詢 [@紅茶拿鐵(ac)#2450]\n被點到者可以選擇不用畫\n沒有換暱稱顏色的需求，就不用特別下指令，直接把點圖畫作放 #daily-hope 即可\n--------------------------------------------------------```"

@client.event
async def on_ready():
	print('log in')
	print(client.user.name)
	print(client.user.id)
	await client.change_presence(game = discord.Game(name="i!help"))

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
	if(message.content == "Hello"):
		handle_hello(client, message)
	if message.content == "i!who":
		global text_who
		await client.send_message(message.channel,text_who)
	if message.content == "i!help":
		global text_help
		await client.send_message(message.channel,text_help)
	if message.content == "i!rule":
		global text_rule
		await client.send_message(message.author,text_rule)
	if(message.content.startswith("i!color")):
		if not test_mode:
			return
		await handle_color(client, message,'i!color')
		await print_all_choose_id(client, message)

	# check after i!hope, anyone finished picture
	if(message.content.startswith('i!done')): 
		if test_mode:
			hope_channel_id = '357191670825091084'
		else:
			hope_channel_id = '364395456379486218'
		if not botcheck.is_hope_channel(message,hope_channel_id):
			await error_channel_msg(client, message)
			return
	
		if ishope == False:
			global text_nobody_hope
			await client.send_message(message.channel,
			text_nobody_hope.format(message.author.mention,message.author.mention,message.author.mention))
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
			msg_answer = await client.wait_for_message(timeout=60,author = message.author,check = check)

			if not msg_answer:
				print('time out!!')
				return
			await handle_color(client,msg_answer,'i!idcolor')

	if(message.content.startswith('i!hope')): 
		await client.delete_message(message)
		if not botcheck.is_hope_channel(message):
			await error_channel_msg(client, message)
			return
		if time.time() - hope_time >= 60*60*24:
			ishope = False 

		if ishope == True:
			global text_next_hope
			next_hope_time = hope_time + 60*60*24
			next_hope_time_str = time.asctime(time.localtime(next_hope_time))
			await client.send_message(message.channel,text_next_hope.format(next_hope_time_str))
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

		hope_time = time.time()
		await client.send_message(message.channel,
			"{} 許願說要 ".format(message.author.mention) +new_member.mention+" 畫 :star2: ``"+hope_topic+"``  :star2:")
		
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

async def error_channel_msg(client,message):
	global text_error_hope_channel
	await client.send_message(message.channel,text_error_hope_channel)


if test_mode:
	client.run("MzUxMjUzOTEwMDU4Njk2NzA0.DIP61Q.DVeU9oIP6a37n7xgdZO7zgJzW-k")
else:
	client.run("MzY0MDA1MTE2NDM0NTc5NDU2.DLXirQ.BxTq4iQKodHq9Whxlsih1YPS9Ho")