import os
from flask import Flask, request, abort
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7847389060:AAH4_pDDS-7U1hA_LNZrXW0fv4w3L9GWiLs'

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
    bot.reply_to(message, "🎉 سلام به ربات خنده‌بازار!\n\nدکمه بزن 😏", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "joke":
        bot.send_message(call.message.chat.id, "جوک باحال:\n\nیه روز یکی رفت دکتر گفت: دکتر من فکر می‌کنم نامرئی‌ام!\nدکتر گفت: بعدی! 😂")
    elif call.data == "special":
        bot.send_message(call.message.chat.id, "😍 محتوای ویژه فقط برای vip!\nبه ادمین پیام بده 👆")
    elif call.data == "grok":
        bot.send_message(call.message.chat.id, "به زودی گروک جواب می‌ده 🤖")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        try:
            update = telebot.types.Update.de_json(request.get_json())
            bot.process_new_updates([update])
            print("Update processed successfully:", update.update_id)  # Log موفقیت
            return 'ok', 200
        except Exception as e:
            print("Error:", str(e))  # Log ارور
            return 'error', 400
    abort(403)

@app.route('/')
def index():
    return "ربات زنده است! 😎"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
