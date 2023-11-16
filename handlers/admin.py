from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton
from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.kb_admin import get_startinline, get_new_admin, get_export
from database_admin import sql_admins_start, get_admins, update_admins, add_new_user, new_user_region, export_to_csv,export_to_json
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMadmin(StatesGroup):
    admin = State()

class FSMuser(StatesGroup):
    username = State()
    region = State()

async def admin_start(message: types.Message):
    admins = await get_admins()
    print(admins)
    if message.from_user.username in admins:
        text = 'Вы успешно вошли в админ-панель и имеете доступ ко всем функциям админа'
        await bot.send_message(message.chat.id, text=text,reply_markup=get_startinline())
    else:
        text='У вас нет доступа к админ-панели, для доступа к клиентской части нажмите /start'
        await bot.send_message(message.chat.id, text=text)

async def menu(callback: types.CallbackQuery):
    admins = await get_admins()
    print(admins)
    if callback.from_user.username in admins:
        text = 'Функции администратора:'
        await callback.message.edit_text(text=text,reply_markup=get_startinline())

async def add_admin(callback: types.CallbackQuery):
    admins = await get_admins()
    text = ''
    for i in admins:
        text += f'@{i}\n\n'
    await callback.message.edit_text(text='Список администраторов:\n\n'+text+'После нажатия на кнопку напишите Имя Пользователя нового администратора',
                                     reply_markup=get_new_admin())


async def fsm_admin(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Пожалуйста, напишите Имя Пользователя пользователя, которого желаете сделать администратором')
    await FSMadmin.admin.set()

async def admin_added(message: types.Message, state:FSMContext):
    """Получение региона и обновление записи в БД"""
    if message.content_type == 'text':
        async with state.proxy() as data:
            text = message.text[1:]
            data['new_admin'] = text
            await update_admins(text)
        await state.finish()
        await message.reply("Новый администратор добавлен",reply_markup=get_startinline())
    else:
        await bot.send_message(message.from_user.id, text='Пожалуйста, напишите текстом')


async def add_user(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Пожалуйста, напишите Имя Пользователя пользователя, которого вы хотите добавить')
    await FSMuser.username.set()

async def fsm_username(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        text = message.text[1:]
        data['username'] = text
        await add_new_user(text)
    await FSMuser.next()
    await message.reply('Теперь введи регион пользователя')

async def fsm_region(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
        await new_user_region(data['username'],data['region'])
        print(data)
    await state.finish()
    await message.reply('Редактирование трека и рода деятельности невозможно', reply_markup=get_startinline())

async def download_data(callback: types.CallbackQuery):
    await callback.message.edit_text(text='В каком формате выгрузить данные о пользователях?',reply_markup=get_export())

async def download_csv(callback: types.CallbackQuery):
    file = await export_to_csv()
    await callback.message.edit_text(text='Файл с данными пользователей в формате csv',reply_markup=get_startinline())
    await bot.send_document(callback.from_user.id, document=file)

async def download_json(callback: types.CallbackQuery):
    file = await export_to_json()
    await callback.message.edit_text(text='Файл с данными пользователей в формате json',reply_markup=get_startinline())
    await bot.send_document(callback.from_user.id, document=file)


async def service_info(callback: types.CallbackQuery):
    await callback.message.edit_text(text="В базе данных трэкам и родам деятельности присвоены условные обозначения"
                                          ", их расшифровка\n\n"
                                          "Расшифовки трэков:\n"
                                        "t1=Исследователи Путешествий\n"
                                        "t2=Хранители Троп\n"
                                        "t3=Проводники Смыслов\n"
                                        "t4=Открыватели Возможностей\n"
                                        "t5=Создатели Маршрутов\n"
                                        "t6=Наставники Регионов\n"
                                        "t7=Проект «Больше, чем работа»\n"
                                        "t8=Программа Студтуризм\n\n\n"
                                        "Расшифровки родов деятельности:\n"
                                            "a1=Представитель оргкомитетов образовательных организаций (ректор, проректор, сотрудник)\n"
                                            "a2=Руководитель или активисты студтурклуба\n"
                                            "a3=Амбассадор Программы Студтуризм\n"
                                            "a4=Представитель вуза, предприятия, региона\n"
                                            "a5=Cтудент, готовый развивать направления промышленного туризма в России\n"
                                            "a6=Инструктор по туризму\n"
                                            "a7=Проводник\n"
                                            "a8=Представитель туристических клубов\n"
                                            "a9=Представитель особо охраняемых природных территорий\n"
                                            "a10=Экскурсовод\n"
                                            "a11=Учитель\n"
                                            "a12=Представитель региональных органов исполнительной власти в сфере молодежной политики и туризма\n"
                                            "a13=Представитель федеральных органов исполнительной власти\n"
                                            "a14=Член Экспертного совета программы «Больше, чем путешествие»\n"
                                            "a16=Туроператор\n"
                                            "a17=Активный участник программы «Больше, чем путешествие»\n"
                                            "a18=Представитель программы в поездках\n"
                                            "a19=Молодой путешественник\n"
                                            "a20=Дирекция конкурсов"
                                          ,reply_markup=get_startinline())

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=['admin'])
    dp.register_callback_query_handler(add_admin, text='2admin')
    dp.register_callback_query_handler(fsm_admin,text='5admin')
    dp.register_message_handler(admin_added, content_types=['text'], state=FSMadmin)
    dp.register_callback_query_handler(menu,text='a_menu')
    dp.register_callback_query_handler(add_user, text='1admin')
    dp.register_message_handler(fsm_username,content_types=['text'], state=FSMuser.username)
    dp.register_message_handler(fsm_region,content_types=['text'], state=FSMuser.region)
    dp.register_callback_query_handler(download_data, text='3admin')
    dp.register_callback_query_handler(download_csv,text='csv')
    dp.register_callback_query_handler(download_json,text='json')
    dp.register_callback_query_handler(service_info, text='4admin')
