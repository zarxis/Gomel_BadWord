import telebot
from telebot import  types
import time

api_token= "api"
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Start")
    bot.send_message(message.chat.id, "ОТВАЛИ, Я НЕ РАБОТАЮ!")

#@bot.message_handler(commands=['Stat'])
#def stat(message):
#    bot.send_message(message.chat.id, "самый большой матершинник это...")
#    n = time.sleep(5)
#    while n < 6:
#        bot.send_message(message.chat.id, "узнаем через n")
#    bot.send_message(message.chat.id, "ты")

bot.infinity_polling()
