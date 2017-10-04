def get_text_change_color_hint():
	text_change_color_hint = "{} 完成了點圖！獲得了更換暱稱顏色的獎勵！:rainbow: 請下指令 ``i!idcolor @顏色號碼``  \n請注意只能更改一次，不要打錯字了:yum:\n:arrow_up_small: 一分鐘後換色權利會過期 ，請趕快選擇"
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
	"```css\n[i!hope 點圖主題]   \n"\
	"{ex: i!hope 貓咪擬人}\n\n"\
	">  每一天只能一次使用 ，如果其他人使用了點圖，則需要隔一天才能再次點圖。\n"\
	"(請慎選你的點圖主題。選錯送出無法改)\n會隨機指定出目前在線上的用戶完成點圖，如果想被點到者，狀態必須是線上。\n"\
	"(非閒置、離線、勿擾狀態)\n\n[i!done 圖片網址或是圖片附件] \n"\
	"{ex: i!done https://images.xxxxxx.jpg}\n\n"\
	">  點圖畫好了使用的指令，圖附檔名必須是 ``jpg`` `` png`` `` gif``，如果你是被點到的對象，可獲得一次改暱稱顏色的機會，如果不是，使用此指令還是會隨機獲得一次改暱稱顏色的機會。\n"\
	"--------------------------------------------------------\n"\
	"任何作弊行為會被視為病毒永久隔離( ×ω× )\n如果有問題請洽詢 [@紅茶拿鐵(ac)#2450]\n"\
	"被點到者可以選擇不用畫\n沒有換暱稱顏色的需求，就不用特別下指令，直接把點圖畫作放 #daily-hope 即可\n"\
	"--------------------------------------------------------```"
	return text_rule