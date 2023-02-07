import telebot, time, sql
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from pygismeteo import Gismeteo

api_token= "5811388544:AAGfs2JxfxB7SBHsRDjhWMmDAmqngEUIXi0"
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key2 = types.KeyboardButton("/Stat")
    key1 = types.KeyboardButton("/Weather")
    markup.add(key1, key2, key3)
    bot.send_message(message.chat.id, "Захотел узнать как часто ты использешь BAD WORDS? Правильно, ты по адресу!", reply_markup=markup)



#просто пихать будем тут функции, да я говно-кодер

#@bot.message_handler(commands=['.getME'])
#def getME(message):
#    n = bot.get_me()
#    bot.send_message(message.chat.id, n)


# Stat
@bot.message_handler(commands=['Stat'])
def stat(message):
    bot.send_message(message.chat.id, "самый большой матершинник это...")
    time.sleep(1)
    bot.send_message(message.chat.id, "ты")

# Погода ----------------------------
@bot.message_handler(commands=['Weather'])

def stat(message):
    bot.send_message(message.chat.id, "Введите название города.")
    bot.register_next_step_handler(message, GetWeather, message.chat.id)

def GetWeather(mesInfo, mesId):
    sityName = mesInfo.text
    gismeteo=Gismeteo()
    if isinstance(sityName, str): 
        search_results = gismeteo.search.by_query(sityName)
        city_id = search_results[0].id

        current = gismeteo.current.by_id(city_id)
        
        temp = current.temperature.air.c
        d_weather = current.description.full
        hum = current.humidity.percent
        cloud = current.cloudiness.percent
        bot.send_message(mesId, "Текущая температура🌍: " + f'{temp}'
                         +'\n'"Тип погоды🌍: " + f'{d_weather}'
                         + '\n'"Влажность🌍: " + f'{hum}'
                         + '\n'"Облачность🌍: " + f'{cloud}')
        print(search_results)
        
         
        """        
        A = str(current.temperature.air.c) + ", " + current.description.full
        A = A + ", " + str(current.humidity.percent) + ", " + str(current.cloudiness.percent)
        bot.send_message(mesId, sityName)
        bot.send_message(mesId, A)
        """
    else:
        bot.send_message(mesId, "ERROR")
    


# будущая регистрация в боте.
@bot.message_handler(commands=['ShowId'])
def get_text_message(message):
    bot.send_message(message.from_user.id, 'Теперь ты в системе')
    
    u_reg = message.from_user.id
    u_fname = message.from_user.username
    u_lname = message.from_user.last_name
        
    sql.db_table_val(user_id = u_reg, first_name = u_fname, last_name = u_lname)

bot.polling(none_stop=True)