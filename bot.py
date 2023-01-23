import telebot, time, DB_CON, Fweather
from telebot import types
from pygismeteo import Gismeteo

api_token= "api"
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("/Stat")
    key2 = types.KeyboardButton("/ShowId")
    key3 = types.KeyboardButton("/Weather")
    markup.add(key1, key2, key3)
    bot.send_message(message.chat.id, "Захотел узнать как часто ты использешь BAD WORDS? Правильно, ты по адресу!", reply_markup=markup)


#просто пихать будем тут функции, да я говно-кодер

#@bot.message_handler(commands=['.getME'])
#def getME(message):
#    n = bot.get_me()
#    bot.send_message(message.chat.id, n)

#
@bot.message_handler(commands=['Weather'])
def stat(message):
    bot.send_message(message.chat.id, "Введите название города.")
    bot.register_next_step_handler(message, GetWeather, message.chat.id)

@bot.message_handler(content_types='text')
def GetWeather(mesInfo, mesId):
    sityName = mesInfo.text
    gismeteo=Gismeteo()
    if isinstance(sityName, str): 
        search_results = gismeteo.search.by_query(sityName)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        
        
        """ Вот эту часть чекни пжлст
        temp = current.temperature.air.c
        d_weather = current.description.full
        hum = current.humidity.percent
        cloud = current.cloudiness.percent
        bot.send_message(message.chat_id, "Текущая температура: " + f'{temp}' +'\n'"Влажность: " + f'{d_weather}' + '\n'"Влажность: " + f'{hum}' + '\n'"Облачность: " + f'{cloud}')
        """
        
        
        A = str(current.temperature.air.c) + ", " + current.description.full
        A = A + ", " + str(current.humidity.percent) + ", " + str(current.cloudiness.percent)
        bot.send_message(mesId, sityName)
        bot.send_message(mesId, A)
    else:
        bot.send_message(mesId, "ERROR")
    
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

bot.polling(none_stop=True, interval=0)