
import telebot
from telebot import types

token = "5111267655:AAGGoDx1-rZUY--ZHZr3S1zby3vSbwlNT94"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Нужна помощь? Нажми /help.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/timetable", "/photo", "/info")
    bot.send_message(message.chat.id, 'Бот имеет следующие команды:', reply_markup=keyboard)

@bot.message_handler(commands=['photo'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("ИСТОРИЯ МТУСИ", "ФАКУЛЬТЕТЫ", "АБИТУРИЕНТУ", "/help")
    bot.send_message(message.chat.id, 'https://irecommend.ru/sites/default/files/imagecache/copyright1/user-images/427908/MA615nl64JFNSquHevbULA.jpg'
                                      ' Также вы можете узнать о МТУСИ больше написав боту ИСТОРИЯ МТУСИ, ФАКУЛЬТЕТЫ или АБИТУРИЕНТУ.', reply_markup=keyboard)

@bot.message_handler(commands=['info'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("ИСТОРИЯ МТУСИ", "ФАКУЛЬТЕТЫ", "АБИТУРИЕНТУ", "/help")
    bot.send_message(message.chat.id, 'Сайт МТУСИ – https://mtuci.ru/ '
                     'Также вы можете узнать о МТУСИ больше написав боту ИСТОРИЯ МТУСИ, ФАКУЛЬТЕТЫ или АБИТУРИЕНТУ.', reply_markup=keyboard)

@bot.message_handler(commands=['timetable'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("ИСТОРИЯ МТУСИ", "ФАКУЛЬТЕТЫ", "АБИТУРИЕНТУ", "/help")
    bot.send_message(message.chat.id, 'https://mtuci.ru/time-table/ '
                     'Также вы можете узнать о МТУСИ больше написав боту ИСТОРИЯ МТУСИ, ФАКУЛЬТЕТЫ или АБИТУРИЕНТУ.', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "история мтуси":
        bot.send_message(message.chat.id, 'Хотите  узнать историу МТУСИ? Переходите ссылке: https://mtuci.ru/about_the_university/history/')
    elif message.text.lower() == "факультеты":
        bot.send_message(message.chat.id, 'Хотите узнать больше про факультеты МТУСИ? Тогда переходите по ссылке: https://mtuci.ru/dep/')
    elif message.text.lower() == "абитуриенту":
        bot.send_message(message.chat.id, 'Хотите подать документы на поступление? Тогда переходите по ссылке: https://abitur.mtuci.ru/')

bot.polling(none_stop=True, interval=0)
