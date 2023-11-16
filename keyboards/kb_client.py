from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton


def get_startinline():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Информация про бот', callback_data='1')
    start_inline.row(b1)
    return start_inline

def get_back():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Возврат в меню', callback_data='back')
    start_inline.row(b1)
    return start_inline

def get_info():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Начать вводить данные', callback_data='2')
    start_inline.row(b1)
    return start_inline

"""
Расшифровки callback data в activities
a1=Представитель оргкомитетов образовательных организаций (ректор, проректор, сотрудник)
a2=Руководитель или активисты студтурклуба
a3=Амбассадор Программы Студтуризм
a4=Представитель вуза, предприятия, региона
a5=Cтудент, готовый развивать направления промышленного туризма в России
a6=Инструктор по туризму
a7=Проводник
a8=Представитель туристических клубов
a9=Представитель особо охраняемых природных территорий
a10=Экскурсовод
a11=Учитель
a12=Представитель региональных органов исполнительной власти в сфере молодежной политики и туризма
a13=Представитель федеральных органов исполнительной власти
a14=Член Экспертного совета программы «Больше, чем путешествие»
a16=Туроператор
a17=Активный участник программы «Больше, чем путешествие»
a18=Представитель программы в поездках
a19=Молодой путешественник
a20=Дирекция конкурсов
"""


def get_activity_stud():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Представитель оргкомитетов образовательных организаций (ректор, проректор, сотрудник)', callback_data='a1')
    b2 = InlineKeyboardButton('Руководитель или активисты студтурклуба', callback_data='a2')
    b3 = InlineKeyboardButton('Амбассадор Программы Студтуризм', callback_data='a3')
    start_inline.row(b1).add(b2).add(b3)
    return start_inline

def get_activity_bigger():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Представитель вуза, предприятия, региона',
                              callback_data='a4')
    b2 = InlineKeyboardButton('Cтудент, готовый развивать направления промышленного туризма в России', callback_data='a5')
    start_inline.row(b1).add(b2)
    return start_inline

def get_activity_trop():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Инструктор по туризму',
                              callback_data='a6')
    b2 = InlineKeyboardButton('Проводник', callback_data='a7')
    b3 = InlineKeyboardButton('Представитель туристических клубов', callback_data='a8')
    b4 = InlineKeyboardButton('Представитель особо охраняемых природных территорий', callback_data='a9')
    start_inline.row(b1).add(b2).add(b4).add(b3)
    return start_inline

def get_activity_smisl():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Экскурсовод',
                              callback_data='a10')
    b2 = InlineKeyboardButton('Учитель', callback_data='a11')
    start_inline.row(b1).add(b2)
    return start_inline

def get_activity_region():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Представитель региональных органов исполнительной власти в сфере молодежной политики и туризма', callback_data='a12')
    b2 = InlineKeyboardButton('Представитель федеральных органов исполнительной власти', callback_data='a13')
    b3 = InlineKeyboardButton('Член Экспертного совета программы «Больше, чем путешествие»', callback_data='a14')
    start_inline.row(b1).add(b2).add(b3)
    return start_inline

def get_activity_creator():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Туроператор', callback_data='a16')
    start_inline.row(b1)
    return start_inline

def get_activity_putesh():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Активный участник программы «Больше, чем путешествие»', callback_data='a17')
    b2 = InlineKeyboardButton('Представитель программы в поездках', callback_data='a18')
    b3 = InlineKeyboardButton('Молодой путешественник', callback_data='a19')
    start_inline.row(b1).add(b2).add(b3)
    return start_inline

def get_activity_opener():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Дирекция конкурсов', callback_data='a20')
    start_inline.row(b1)
    return start_inline


"""Расшифовки callback в tracks
t1=Исследователи Путешествий
t2=Хранители Троп
t3=Проводники Смыслов
t4=Открыватели Возможностей
t5=Создатели Маршрутов
t6=Наставники Регионов
t7=Проект «Больше, чем работа»
t8=Программа Студтуризм
"""
def get_tracks():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Исследователи Путешествий', callback_data='t1')
    b2 = InlineKeyboardButton('Хранители Троп', callback_data='t2')
    b3 = InlineKeyboardButton('Проводники Смыслов', callback_data='t3')
    b4 = InlineKeyboardButton('Открыватели Возможностей', callback_data='t4')
    b5 = InlineKeyboardButton('Создатели Маршрутов', callback_data='t5')
    b6 = InlineKeyboardButton('Наставники Регионов', callback_data='t6')
    b7 = InlineKeyboardButton('Проект «Больше, чем работа»', callback_data='t7')
    b8 = InlineKeyboardButton('Программа Студтуризм', callback_data='t8')
    start_inline.row(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8)
    return start_inline

def get_menu():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Найти человека по информации', callback_data='5')
    b2 = InlineKeyboardButton('Создать группу из 3-ёх человек', callback_data='6')
    b3 = InlineKeyboardButton('Инструкция по использованию бота', callback_data='7')
    b4 = InlineKeyboardButton('Обновить данные', callback_data='8')
    start_inline.row(b1).add(b2).add(b3).add(b4)
    return start_inline

def get_man():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('По региону', callback_data='9')
    b2 = InlineKeyboardButton('По треку', callback_data='10')
    b3 = InlineKeyboardButton('По деятельности', callback_data='11')
    start_inline.row(b1).add(b2).add(b3)
    return start_inline

def get_many():
    start_inline = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('По региону', callback_data='12')
    b2 = InlineKeyboardButton('По треку', callback_data='13')
    b3 = InlineKeyboardButton('По деятельности', callback_data='14')
    start_inline.row(b1).add(b2).add(b3)
    return start_inline


