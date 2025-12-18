import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
import os

TOKEN = '784789060:AAH4_pDDS-7U1hA_LNZrXW0fv4w3L9GWiLs'  # توکنت

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

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

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "joke":
        bot.send_message(call.message.chat.id, "جوک باحال:\n\nاومدم به دوستم pm بدم، دیدم آفلاینه... گفتم afk بدم! 😂")
    elif call.data == "special":
        bot.send_message(call.message.chat.id, "😍 محتوای ویژه فقط برای اعضای vip!\nبه ادمین پیام بده 👆")
    elif call.data == "grok":
        bot.send_message(call.message.chat.id, "به زودی سوالتو به گروک واقعی می‌فرستم و جواب می‌گیرم 🤖")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def index():
    return 'ربات زنده است!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
