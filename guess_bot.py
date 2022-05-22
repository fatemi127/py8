import telebot
import random
import qrcode
from gtts import gTTS

TOKEN = '5309183513:AAGDv-3VLnrQwl6jgFrAzvEcA74jshczL_k'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands =['start'])
def send_welcome(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} من ربات حدس عدد هستم. جهت شروع بازی /game را بزن")

@bot.message_handler(commands=['game'])
def start_message(message):
    a = random.randint(0,100)
    message_for_game = bot.send_message(message.chat.id,"به بازی حدس عدد خوش اومدی، بین اعداد 0 تا 100 عدد وارد کن")
  
    @bot.message_handler(func= lambda m: True)
    def guess(message):
        b = int(message.text)
        if a==b:
            bot.reply_to(message,f"ایول  تونستی درست حدس بزنی!")
        elif a<b:
            bot.reply_to(message,"برو بالا")
        elif a>b:
            bot.reply_to(message,"بیا پایین")
            
        


@bot.message_handler(commands =['voice'])
def voice_s(message):
    matn = bot.send_message(message.chat.id,"متن خود را برای تبدیل به صدا وارد کنید (انگلیسی پشتیبانی می‌شود)")
    bot.register_next_step_handler(matn, seda)
def seda(message):
    myobj = gTTS(text = message.text, slow=False)
    myobj.save('file.mp3')
    voice = open('file.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands =['age'])
def send_age(message):
    myname = message.from_user.first_name
    pasokh = bot.send_message(message.chat.id,f"سلام {myname} لطفا سال تولد خود را به شمسی وارد کنید:")
    bot.register_next_step_handler(pasokh, sen)
def sen(message):
    myname = message.from_user.first_name
    sal = int(message.text)
    alan = 1401 - sal
    bot.send_message(message.chat.id,f"{myname} تو الان {alan} سالته!")

@bot.message_handler(commands =['qr'])
def send_a(message):
    #myname = message.from_user.first_name
    bot.send_message(message.chat.id,"لطفا کلمه مورد نظر را برای تبدیل به qr وارد کنید")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        e = message.text
        img = qrcode.make(e)
        img.save("some_file.png")
        photo = open('some_file.png', 'rb')
        bot.send_photo(message.chat.id, photo)

bot.infinity_polling()
