from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


def get_startinline():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Добавление пользователя', callback_data='1admin')
    b2 = InlineKeyboardButton('Обновление списка администраторов', callback_data='2admin')
    b3 = InlineKeyboardButton('Скачать список пользователей', callback_data='3admin')
    b4 = InlineKeyboardButton('Служебные обозначения', callback_data='4admin')
    start_inline.row(b1).add(b2).add(b3).add(b4)
    return start_inline

def get_new_admin():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Добавить администратора', callback_data='5admin')
    b2 = InlineKeyboardButton('Возврат в меню', callback_data='a_menu')
    start_inline.row(b1).add(b2)
    return start_inline

def get_export():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('CSV', callback_data='csv')
    b2 = InlineKeyboardButton('JSON', callback_data='json')
    start_inline.row(b1).add(b2)
    return start_inline