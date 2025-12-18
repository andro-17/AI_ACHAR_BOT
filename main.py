import os
from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '784789060:AAH4_pDDS-7U1hA_LNZrXW0fv4w3L9GWiLs'  # توکنت

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# دستور /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("😂 جوک جدید", callback_data="joke"),
        InlineKeyboardButton("😍 محتوای ویژه", callback_data="special"),
        InlineKeyboardButton("📞 تماس با ادمین", url="https://t.me/ANDRO_17"),
        InlineKeyboardButton("🤖 سوال از گروک", callback_data="grok")
    )
    bot.reply_to(message, "🎉 سلام! به ربات خنده‌بازار خوش اومدی 😏\nیکی از دکمه‌ها رو بزن!", reply_markup=markup)

# دکمه‌ها
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "joke":
        bot.send_message(call.message.chat.id, "جوک باحال:\n\nیکی گفت به خدا سوگند!\nخدا گفت قبول نیست، شاهد نداری 😂")
    elif call.data == "special":
        bot.send_message(call.message.chat.id, "😍 محتوای ویژه فقط برای اعضای vip!\nبه ادمین پیام بده 👆")
    elif call.data == "grok":
        bot.send_message(call.message.chat.id, "به زودی سوالتو به گروک واقعی می‌فرستم و جواب می‌گیرم 🤖")

# webhook برای دریافت آپدیت‌ها
@app.route('/' + TOKEN, methods=['POST'])
def get_update():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        return 'bad request', 403

# صفحه اصلی (برای تست زنده بودن)
@app.route('/')
def index():
    return "ربات زنده است! 😎"

# اجرای سرور
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
