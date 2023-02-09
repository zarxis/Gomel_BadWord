import telebot, time, sql, logging, sys
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from pygismeteo import Gismeteo

api_token= "5811388544:AAGfs2JxfxB7SBHsRDjhWMmDAmqngEUIXi0"
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #key = types.KeyboardButton("/Stat")
    key1 = types.KeyboardButton("/Weather")
    key2 = types.KeyboardButton("/register")
    markup.add(key1, key2)
    bot.send_message(message.chat.id,
                     "Захотел узнать как часто ты использешь BADWORDS? Правильно, ты по адресу!",
                     reply_markup=markup)



#просто пихать будем тут функции, да я говно-кодер

#@bot.message_handler(commands=['.getME'])
#def getME(message):
#    n = bot.get_me()
#    bot.send_message(message.chat.id, n)


# Stat

#@bot.message_handler(commands=['Stat'])
#def stat(message):
#    
#    bot.send_message(message.chat.id, "самый большой матершинник это...")
#    time.sleep(1)
#    bot.send_message(message.chat.id, "ты")


# Погода ----------------------------
@bot.message_handler(commands=['Weather'])
def startW(message):
    bot.send_message(message.chat.id, "Введите название города.")
    bot.register_next_step_handler(message, GetWeather, message.chat.id)

def GetWeather(mesInfo, mesId):
    sityName = mesInfo.text
    gismeteo=Gismeteo()
    if isinstance(sityName, str): 
        search_results = gismeteo.search.by_query(sityName)
        #print(search_results)
        city_id = search_results[0].id
        #print('\n------------------------------', city_id)
        current = gismeteo.current.by_id(city_id)
        #print('\n -------------------------------', current)
        
        temp = current.temperature.air.c
        d_weather = current.description.full
        hum = current.humidity.percent
        cloud = current.cloudiness.percent
        bot.send_message(mesId, "Текущая температура🌍: " + f'{temp}'
                         +'\n'"Тип погоды🌍: " + f'{d_weather}'
                         + '\n'"Влажность🌍: " + f'{hum}'
                         + '\n'"Облачность🌍: " + f'{cloud}')
        

#обдащение в бд
@bot.message_handler(commands=['register'])
def get_text_message(message):
    #Запись в бдшку
    try:
        #привидение переменных для бд
        u_reg = message.from_user.id
        u_fname = message.from_user.username
        u_lname = message.from_user.last_name
        u_stat = 0
        sql.db_INSERT(user_id = u_reg, first_name = u_fname, last_name = u_lname, stat = u_stat)
        bot.send_message(message.from_user.id, 'Поздравляю, теперь ты зарегестрирован :)')
    except:
        bot.send_message(message.chat.id, 'Ты уже зарегистрирован')



while True:
    try:
      bot.polling(none_stop=True)
    except: 
      print('ERR')
      logging.error('error: {}'.format(sys.exc_info()[0]))
      time.sleep(5)