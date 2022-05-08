import telebot
import random
from gtts import gTTS
from telebot import types
TOKEN = '5309183513:AAHw9YbUY0sbiWM61dnfVvkCjV_58Adtja8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands =['start'])
def send_welcome(message):
    # myname = message.chat.username
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} من ربات حدس عدد هستم. جهت شروع بازی /game را بزن")
    
@bot.message_handler(commands =['game'])
def send_welcome(message):
    bot.reply_to(message,"بین صفر تا صد یک عدد انتخاب کردم، حدس بزن!")
    b = random.randint(0,100)
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        myname = message.from_user.first_name
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('a')
        a = int(message.text)
        if a==b:
            bot.reply_to(message,f"ایول {myname} تونستی درست حدس بزنی!")
        elif a<b:
            bot.reply_to(message,"برو بالا")
        elif a>b: 
            bot.reply_to(message,"بیا پایین")

@bot.message_handler(commands =['voice'])
def send_m(message):
    bot.reply_to(message,"متن خود را برای تبدیل به صدا وارد کنید (انگلیسی پشتیبانی می‌شود)")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        tt = gTTS(message.text)
        tt.save('file.mp3')
        voice = open('file.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands =['age'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} لطفا سال تولد خود را به شمسی وارد کنید:")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        a = int(message.text)
        b = 1401 - a
        bot.reply_to(message,f"{myname} تو الان {b} سالته!")
        


bot.infinity_polling()