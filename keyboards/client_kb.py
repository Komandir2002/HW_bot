from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

help_button = KeyboardButton('/help')
quiz_button = KeyboardButton('/quiz')
info_button = KeyboardButton('/info')
joke_button = KeyboardButton('/joke')
vetka_button = KeyboardButton('/vetka')
location_button = KeyboardButton('Share Location',request_location=True)
information_button = KeyboardButton('Share Info',request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
start_markup.row(help_button,quiz_button,location_button,information_button,info_button,joke_button,vetka_button)