import telebot
import random
import qrcode
from gtts import gTTS
from telebot import types
TOKEN = '<anytoken!>'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands =['start'])
def send_welcome(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname} من ربات حدس عدد هستم. جهت شروع بازی /game را بزن")
    
@bot.message_handler(commands =['game'])
def send_welcome(message):
    a_num =  bot.send_message(message,"بین صفر تا صد یک عدد انتخاب کردم، حدس بزن!")
    bot.register_next_step_handler(a_num, game_new)
def game_new(message):
    b = random.randint(0,100)
    myname = message.from_user.first_name
    a = int(message.text)
    if a==b:
        bot.reply_to(message,f"ایول {myname} تونستی درست حدس بزنی!")
    elif a<b:
        bot.reply_to(message,"برو بالا")
    elif a>b: 
        bot.reply_to(message,"بیا پایین")      
  
    

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
    myname = message.from_user.first_name
    bot.reply_to(message,f"لطفا کلمه مورد نظر را برای تبدیل به qr وارد کنید")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        e = message.text
        img = qrcode.make(e)
        img.save("some_file.png")
        photo = open('some_file.png', 'rb')
        bot.send_photo(message.chat.id, photo)
@bot.message_handler(commands =['list'])
def list(message):
    myname = message.from_user.first_name
    list_num = []
    bot.reply_to(message,f"تعدادی عدد را به ترتیب وارد کنید تا بزرگترین آن را بگویم!")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        if message.text != "/done":
            num_lst =int(message.text)
            list_num.append(num_lst)
            max_lst = max (list_num)
        if message.text != "/done":      
            bot.reply_to(message,f"عدد مورد نظر به لیست وارد شد. اگر اعدادت تمام شد روی /start کلیک کنید")
        
        bot.reply_to(message,f"فهرست اعدادی که وارد کردی {list_num} :هست و بزرگترین عدد آن \n {max_lst} است")
            
bot.infinity_polling()
