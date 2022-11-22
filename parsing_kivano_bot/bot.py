from telebot import types, TeleBot
from decouple import config

from parsing import main as parse
from utils import get_db, get_products_by_category, get_total_pages_by_category


token = config('TOKEN')
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Если хотите посмотреть каталог введите /catalog\nЕсли хотите спрасить заново, введите /parse')

@bot.message_handler(commands=['parse'])
def update_db(message):
    bot.send_message(message.chat.id, 'Начинаем парсинг')
    parse()

@bot.message_handler(commands=['catalog'])
def send_catalog(message):
    categories = list(get_db().keys())
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(0, len(categories)+1, 3):
        buttons = []
        for j in range(3):
            if i+j >= len(categories):
                break
            cat = categories[i+j]
            button = types.InlineKeyboardButton(cat, callback_data=f'category={cat}')
            buttons.append(button)
        keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Категории:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: True)
def check_button(call):
    params = parse_params(call.data)
    if 'id' in params:
        send_product_details(call, params)
    else:
        send_products(call, params) 

def parse_params(params):
    return dict(x.split('=') for x in params.split('&'))

def send_products(call, params):
    category = params['category']
    page = int(params.get('page', 1))
    last = get_total_pages_by_category(category)
    products = get_products_by_category(category, page)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for i in range(0, len(products)+1, 2):
        buttons = []
        for j in range(2):
            if i+j >= len(products):
                break
            product = products[i+j]
            button = types.InlineKeyboardButton(product['title'], callback_data=f'category={category}&page={page}&id={i+j}')
            buttons.append(button)
        keyboard.add(*buttons)
    buttons = []
    if page < last:
        button = types.InlineKeyboardButton('>>', callback_data=f'category={category}&page={page+1}')
        buttons.append(button)
    if page > 1:
        button = types.InlineKeyboardButton('<<', callback_data=f'category={category}&page={page-1}')
        buttons.append(button)
    keyboard.add(*buttons)

    bot.send_message(call.from_user.id, f'Страница: {page}\nПродукты:', reply_markup=keyboard)

def send_product_details(call, params):
    category = params['category'] 
    page = int(params.get('page', 1))
    id = int(params['id'])
    products = get_products_by_category(category, page)
    product = products[id]
    bot.send_photo(call.from_user.id, product['image'])
    bot.send_message(call.from_user.id, f'Title: {product["title"]}\nPrice: {product["price"]}')

bot.polling()