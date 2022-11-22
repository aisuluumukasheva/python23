import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# создать клавиатуру
keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хэллоу хэллоу, выбери кнопку: ', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == "yes":
        bot.send_sticker(call.from_user.id, 'CAACAgEAAxkBAAEGOp1jW2mvlOEs4YrkXR0OPYsRdyOa0wACWgcAAr-MkAS28TuOYHM0EyoE')
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, 'CAACAgEAAxkBAAEGOspjW2oIwllfLxNha-BRTFiTiC-ewQACTgcAAr-MkAQJUa97EBGooCoE')
        

bot.polling()