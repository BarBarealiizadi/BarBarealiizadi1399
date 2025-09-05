import telebot
import os

# اینجا باید توکن رباتت رو بذاری
TOKEN = os.getenv("BOT_TOKEN")  # بعدا تو Render اضافه می‌کنیم
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "سلام":
        bot.reply_to(message, "سلام! حالت چطوره؟")
    else:
        bot.reply_to(message, "پیام‌تو گرفتم 👌")

bot.polling()
