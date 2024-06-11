import random, re, requests
from datetime import datetime, timedelta
import telebot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak


token = "7372310968:AAFLr_nK2rU5AaeJHDH6-aNSC9z_k-wXSSc"
bot = telebot.TeleBot(token)

old = None

@bot.callback_query_handler(func=lambda call: call.data == 'ok')
def rand(call):

    min_date = datetime(1995,6,16)
    now = datetime.now()
    max_date = now - timedelta(hours=6)
    date = min_date + timedelta(seconds=random.randint(0, int((max_date - min_date).total_seconds())))

    year = date.strftime("%y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    
    url = f"https://apod.nasa.gov/apod/ap{year}{month}{day}.html"
    req = requests.get(url).text
    img = re.findall('<IMG SRC="(.*?)"', req)[0]
    link = "https://apod.nasa.gov/apod/" + img

    new = bot.send_photo(call.message.chat.id, link,reply_markup=Mak().add(Btn('صورة ثانية',callback_data='ok')))
    
    old = new

@bot.message_handler(commands=["start"])
def Welcome(msg):
    bot.reply_to(msg,'''مرحبا بك {} في بوت صور الفضاء
يمكنك ضغط بلإسفل لعرض الصوره بأعلى دقه ᶠᵘˡˡ ʰᵈ
 by : @exxxix  👨🏼‍🚀 '''.format(msg.from_user.first_name), reply_markup=Mak().add(Btn('صورة من الفضاء ', callback_data='ok')))
bot.infinity_polling()
