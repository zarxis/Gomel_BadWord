import telebot
from telebot import types
import time
import DB_CON

api_token= "api"
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("/Stat")
    key2 = types.KeyboardButton("/ShowId")
    markup.add(key1, key2)
    bot.send_message(message.chat.id, "Захотел узнать как часто ты использешь BAD WORDS? Правильно, ты по адресу!", reply_markup=markup)


#просто пихать будем тут функции, да я говно-кодер

#
@bot.message_handler(commands=['Stat'])
def stat(message):
    bot.send_message(message.chat.id, "самый большой матершинник это...")
    time.sleep(1)
    bot.send_message(message.chat.id, "ты")

#
@bot.message_handler(commands=['ShowId'])
def my_id(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, user_id)


bot.infinity_polling()