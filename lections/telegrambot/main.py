import telebot

from decouple import config

token = config('TOKEN')
print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','hello'])
def start_message(message):
    bot.send_message(message.chat.id,'Хэллоу хэллоу')
    # отправить текстовое сообщение
    bot.send_sticker(message.chat.id,'CAACAgEAAxkBAAEGOaFjW12-0DJWyQetSaKzLI1mQmlR1gACSgcAAr-MkASOUccq84-8GioE')
    # отправить стикер
    bot.send_photo(message.chat.id,'https://www.dallaspetland.com/wp-content/uploads/2022/02/Bull-Terrier-1-300x300.png')
    # отправить фото
bot.polling()
# команда, которая запускает бота
