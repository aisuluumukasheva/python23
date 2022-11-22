import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да') 
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хэй хэй, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAEGOp1jW2mvlOEs4YrkXR0OPYsRdyOa0wACWgcAAr-MkAS28TuOYHM0EyoE')
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAEGOspjW2oIwllfLxNha-BRTFiTiC-ewQACTgcAAr-MkAQJUa97EBGooCoE')
    else:
        bot.send_message(message.chat.id, 'Нажми на кнопку, ё моё!')   
        bot.register_next_step_handler(message, reply_to_button) 


bot.polling()
