from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Вопросы')
b2 = KeyboardButton('/Расположение')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)

kb_user.add(b1).add(b2)