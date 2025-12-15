import telebot
from telebot import types

TOKEN = "8068497666:AAEl1Vj079Zf3RNu9ejB0qAPXqCExPCQ78U"
bot = telebot.TeleBot(TOKEN)

# Foydalanuvchilarni saqlash uchun set
users = set()

# /start komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    users.add(message.chat.id)  # foydalanuvchini ro‘yxatga qo‘shamiz

    # Inline menu yaratamiz
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🏖 Maskanlar ro‘yxati", callback_data="maskan")
    btn2 = types.InlineKeyboardButton("👨‍💼 Admin", callback_data="admin")
    btn3 = types.InlineKeyboardButton("👨‍💻 Yaratuvchi", callback_data="creator")
    btn4 = types.InlineKeyboardButton("📊 Foydalanuvchilar soni", callback_data="users_count")
    # Oddiy URL tugmasi
    btn5 = types.InlineKeyboardButton(
        "🌐 Bizning rasmiy web saytimiz",
        url="https://damolishmaskani.netlify.app/"   # bu yerda o‘z saytingizni yozing
    )

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)

    bot.send_message(
        message.chat.id,
        "🏖 Dam olish maskaniga xush kelibsiz!\nQuyidagi menyudan tanlang:",
        reply_markup=markup
    )

# Inline tugmalarni ishlovchi handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "maskan":
        bot.send_message(call.message.chat.id, "Dam olish maskanida basseyn, oshxona, honalar va tog'lar bag'rida joylashgan.")
    elif call.data == "admin":
        bot.send_message(call.message.chat.id, "Admin: Urokov Nurali, tel: +998 99 274 60 47")
        photo_url = "https://mehmonxona212.netlify.app/"  # haqiqiy rasm URL bo‘lishi kerak
        bot.send_photo(call.message.chat.id, photo_url, caption="Chorbog‘ dam olish maskani")
    elif call.data == "creator":
        bot.send_message(call.message.chat.id, "👨‍💻 Ushbu bot yaratuvchisi: Dasturchi\nTelegram: https://t.me/Python_212")
    elif call.data == "users_count":
        bot.send_message(call.message.chat.id, f"📊 Hozircha {len(users)} ta foydalanuvchi botdan foydalangan.")

# Default handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Komandalarni ishlatib ko‘ring: /start")

# Botni ishga tushirish
bot.polling(none_stop=True)
