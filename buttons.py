import telebot
from telebot import types

bot = telebot.TeleBot('6001296458:AAFTixxxXUIxJxLO1xgpjwyw7q64-L95hSs')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '.')

@bot.message_handler(commands=['button'])
def but(message):
    markup_but = types.ReplyKeyboardMarkup(resize_keyboard = True)

    but = types.KeyboardButton('вова путін хто?')

    markup_but.add(but)

    bot.send_message(message.chat.id, 'buttons are fixed!', reply_markup = markup_but)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'вова путін хто?':
        bot.send_message(message.chat.id, 'хуйло!')


bot.polling(none_stop=True)