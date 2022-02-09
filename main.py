#qweqwewqe
import telebot
from telebot import types

token = "5111267655:AAGGoDx1-rZUY--ZHZr3S1zby3vSbwlNT94"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("хочу", "/photo", "/site")
    bot.send_message(message.chat.id, 'Бот имеет следующие команды:', reply_markup=keyboard)

@bot.message_handler(commands=['photo'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://irecommend.ru/sites/default/files/imagecache/copyright1/user-images/427908/MA615nl64JFNSquHevbULA.jpg')

@bot.message_handler(commands=['site'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда используй команду /site')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Тогда тебе не сюда')
    elif message.text.lower() == "не знаю":
        bot.send_message(message.chat.id, 'Посети сайт МТУСИ и узнай с помощю команды /site')

bot.polling(none_stop=True, interval=0)
