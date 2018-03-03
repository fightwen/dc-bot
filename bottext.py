import discord

def get_text_change_color_hint():
	text_change_color_hint = "{} 完成了點圖！獲得了更換暱稱顏色的獎勵！:rainbow: 請下指令 ``i!idcolor @顏色號碼*``  \n請注意只能更改一次，不要打錯字了:yum:\n:arrow_up_small: 一分鐘後換色權利會過期 ，請趕快選擇"
	return text_change_color_hint

def get_text_all_server_colors_hint():
	text_all_server_colors_hint = ":tada: 可以選的顏色："
	return text_all_server_colors_hint

def get_text_not_member_can_draw():
	text_not_member_can_draw = "目前沒有人可以點圖 :sob:"
	return text_not_member_can_draw

def get_text_error_hope_channel():
	text_error_hope_channel = "錯誤的頻道！請到點圖頻道 :stuck_out_tongue_closed_eyes:"
	return text_error_hope_channel

def get_text_nobody_hope():
	text_nobody_hope = "現在根本沒人點圖 :flushed: ，但還是感謝 {0} 貢獻畫作！ :two_hearts: 感恩 {1}！ 讚嘆 {2}！"
	return text_nobody_hope

def get_text_no_bonus():
	text_nobody_hope = "{0} 完成了點圖！ 可惜沒抽中暱稱換色的機會，請再多畫幾張使用``i!done``試試看吧，感謝 {1} 貢獻畫作！ :two_hearts: 感恩 {2}！ 讚嘆 {3}！"
	return text_nobody_hope

def get_text_next_hope():
	text_next_hope = ":bangbang: 點圖進行中，下次可點圖時間為  {} :alarm_clock:"
	return text_next_hope

def get_text_who():
	text_who = "__**姓名**__：下午茶秘書\n"\
	"__**誕生日**__：2017/10/03\n"\
	"__**身高**__：不明\n"\
	"__**喜歡**__：滿滿的大自介\n"\
	"__**討厭**__：等你寫自介\n"\
	"__**造型**__：ahmin\n https://cdn.discordapp.com/avatars/364005116434579456/e4ede0ff346a6d435ec829000c7b9841.jpg"
	return text_who


def get_text_help():
	text_help = "您好！我是下午茶秘書\n"+"任何活動，任何需求，看心情決定是否為您實現 :closed_book:\n" \
	":small_orange_diamond: ``i!help`` = 秘書處理的所有業務資料\n"\
	":small_blue_diamond: ``i!who``  = 秘書身家調查\n"\
	":small_orange_diamond: ``i!rule``  = 可獲取一份 #daily-hope 點圖許願池說明書\n"\
	":small_blue_diamond: ``i!idcolor x``  = 取消暱稱顏色的設定"
	return text_help

def get_text_rule():
	text_rule ="點圖許願池說明書 :ok_hand: 祝您玩得愉快。\n"\
	"```css"\
	"\n[i!hope 點圖主題]   \n"\
	"{ex: i!hope 貓咪擬人}\n\n"\
	">  每兩小時只能一次使用 ，如果其他人使用了點圖，則需要隔兩小時才能再次點圖。\n"\
	"(請慎選你的點圖主題。選錯送出無法改)\n會隨機指定出目前在線上的用戶完成點圖，如果想被點到者，狀態必須是線上。\n"\
	"(非閒置、離線、勿擾狀態)\n\n"\
	"[i!hope 類型 點圖主題]   \n"\
	"{ex: i!hope 色票 貓咪擬人}\n\n"\
	">  i!hope進階版，會依據類型隨機顯示類型的卡片，例如色票就隨機產生色票卡。\n"\
	">  可以用的類型：色票、顏色、樣式\n\n"\
	"[i!done 圖片網址或是圖片附件] \n"\
	"{ex: i!done https://images.xxxxxx.jpg}\n\n"\
	">  點圖畫好了使用的指令，圖附檔名必須是 ``jpg`` `` png`` `` gif``，如果你是被點到的對象，可獲得一次改暱稱顏色的機會，如果不是，使用此指令還是會隨機獲得一次改暱稱顏色的機會。\n\n"\
	"--------------------------------------------------------\n"\
	"任何作弊行為會被視為病毒永久隔離( ×ω× ) ex.發與點圖無關的圖、重複洗頻、發偷懶圖(!?)...等等 \n如果有問題請洽詢 [@紅茶拿鐵(ac)#2450]\n"\
	"被點到者可以選擇不用畫\n沒有換暱稱顏色的需求，就不用特別下指令，直接把點圖畫作放 #2hours-hope 即可\n"\
	"--------------------------------------------------------```"
	return text_rule
def get_text_hope_dm():
	text_hope_dm = ":mega: {0}  您接收到點圖任務了！ 請前往伺服器 **{1}** #{2} 點圖頻道完成任務吧！:sparkles:\n "\
	"~~(當然如果你不想....就算惹QQ)~~ \n\n點選伺服器連結，可快速前往點圖頻道\n {3}"
	return text_hope_dm

def get_server_hope_url():
	return "https://discord.gg/5GqTNXy"

def get_text_hope_no_permission():
	text_hope_no_permission = "{} 等級不夠，請升級Lv1，沒有指定別人點圖的權限，但是可以接受其他人的點圖任務 :thumbsup:"
	return text_hope_no_permission
def get_text_color():
	text_color = "這是 {} 抽到的顏色卡，畫圖的主題色就是這個囉 :kissing_heart:"
	return text_color

def get_text_palettes():
	text_palettes = "這是 {} 抽到的色票卡，快用這些色票揮灑你的圖吧  :innocent: :heart:"
	return text_palettes

def get_text_patterns():
	text_patterns = "這是 {} 抽到的樣式卡，照著這個樣式風格來發想你的創作吧  :relaxed: :heartpulse:"
	return text_patterns

def get_text_kaomoji():
	text_patterns = "這是 {} 抽到的顏文字，嘗試用此表情展現你的角色吧 :rofl:"
	return text_patterns

def get_text_emoji():
	text_emoji = "這是 {} 抽到的 emoji，嘗試用此圖展現你的角色吧 :rofl:"
	return text_emoji

def get_text_hope_topic_msg():
	text_hope_topic_mg = ":loudspeaker: 進行中的點圖主題： {}"
	return text_hope_topic_mg

def get_text_hope_topic_main_msg(message,new_member,hope_topic):
	text_hope_topic_main_msg = "{} 許願說要 ".format(message.author.mention) +new_member.mention+" 畫 :star2: "+hope_topic+"  :star2:"
	return text_hope_topic_main_msg

def get_text_change_msg(is_success):
	text_change_msg = ""
	if(is_success):
		text_change_msg = "暱稱換顏色成功囉！還不快讚嘆我 :kissing_heart:"
	else:
		text_change_msg = "唉呀~打錯指令囉！掰掰，下次再畫一張圖並輸入 ``i!done`` 試試看 :stuck_out_tongue_winking_eye:"
	return text_change_msg

def get_text_hope_type_msg():
	text_hope_type_msg = "阿！還有**限定要用此 {} **完成圖 :point_down:"
	return text_hope_type_msg

def get_text_hope_finishtip():
	text_hope_finishtip = "別忘了畫完的圖要附上 ``i!done`` 指令才能有換取暱稱顏色的機會唷 :kissing_closed_eyes:"
	return text_hope_finishtip

def get_bot_cmd(test_mode):
	if test_mode:
		return "g"
	else:
		return "i"