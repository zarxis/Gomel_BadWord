import telebot

api_token= "..."
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "ОТВАЛИ, Я НЕ РАБОТАЮ!")
bot.infinity_polling()
