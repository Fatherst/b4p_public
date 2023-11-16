from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.kb_client import get_startinline, get_info, get_activity_region,get_activity_putesh,get_activity_stud,get_activity_trop,get_activity_bigger,get_activity_creator,get_activity_opener,get_activity_smisl,get_tracks, get_menu,get_man, get_many, get_back
from database import check_bd_user_region, sql_start, add_user_by_region, check_user, get_user, add_track, get_user_by_track_three,get_user_by_track, get_user_by_region, add_activity, get_user_by_activity, get_user_by_region_three,get_user_by_activ_three, update_user_region
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


tracks_dict = {
    't1': 'Исследователи Путешествий',
    't2': 'Хранители Троп',
    't3': 'Проводники Смыслов',
    't4': 'Открыватели Возможностей',
    't5': 'Создатели Маршрутов',
    't6': 'Наставники Регионов',
    't7': 'Проект «Больше, чем работа»',
    't8': 'Программа Студтуризм',
}

activities_dict = {
    'a1': 'Представитель оргкомитетов образовательных организаций (ректор, проректор, сотрудник)',
    'a2': 'Руководитель или активисты студтурклуба',
    'a3': 'Амбассадор Программы Студтуризм',
    'a4': 'Представитель вуза, предприятия, региона',
    'a5': 'Cтудент, готовый развивать направления промышленного туризма в России',
    'a6': 'Инструктор по туризму',
    'a7': 'Проводник',
    'a8': 'Представитель туристических клубов',
    'a9': 'Представитель особо охраняемых природных территорий',
    'a10': 'Экскурсовод',
    'a11': 'Учитель',
    'a12': 'Представитель региональных органов исполнительной власти в сфере молодежной политики и туризма',
    'a13': 'Представитель федеральных органов исполнительной власти',
    'a14': 'Член Экспертного совета программы «Больше, чем путешествие»',
    'a16': 'Туроператор',
    'a17': 'Активный участник программы «Больше, чем путешествие»',
    'a18': 'Представитель программы в поездках',
    'a19': 'Молодой путешественник',
    'a20': 'Дирекция конкурсов',

}

class FSMall(StatesGroup):
    region = State()

class FSMupdate(StatesGroup):
    update = State()

class FSMactivity(StatesGroup):
    activity = State()

class FSMtrack(StatesGroup):
    track = State()

async def start_command(message: types.Message):
    """Проверка, зарегистрирован ли юзер уже и есть ли у него юзернейм"""
    if message.from_user.username:
        if not await check_user(message.from_user.username):
            await bot.send_photo(message.chat.id,
                                 photo="AgACAgIAAxkBAAEnkNRlT4xDCm-EwXjPVidrGEdU2MNdpgACItYxG-_hgUp1BSI-iNDt5AEAAwIAA3kAAzME",
                                 caption='Приветствую! Ты попал в бот форума «Больше, чем путешествие»! Нажми на кнопку ниже, чтобы начать общаться с другими участниками форума!\n\nНа форуме тебя ожидает:\n– образовательная программа;\n – полезная программа;\n– экскурсионная программа;\n– культурная программа.\n\n'
                                         'ВАЖНО!\nПеред использованием бота убедись, что у тебя в настройках установлено Имя Пользователя. Если не установлено, то перейди в Настройки -> Имя Пользователя',
                                 reply_markup=get_startinline())
        else:
            rows = await get_user(message.from_user.username)
            rows_for_string = []
            for i in rows:
                if i is None:
                    i = 'Не указано'
                    rows_for_string.append(i)
                else:
                    rows_for_string.append(i)
            await bot.send_message(message.chat.id, text=f'*Ваш профиль:*\n_Имя Пользователя:_* @{rows_for_string[0]}*\n'
                                    f'_Регион:_* {rows_for_string[1].title()}*\n'
                                    f'_Род деятельности:_* {activities_dict[rows_for_string[2]]}*\n'
                                    f'_Трек:_* {tracks_dict[rows_for_string[3]]}*\n',reply_markup=get_menu(),parse_mode="Markdown")
    else:
        await bot.send_message(message.chat.id, text='К сожалению, у вас не установлено Имя Пользователя Telegram и вы не можете '
                                                     'продолжать использование бота. Пожалуйста, перейдите в настройки Telegram и установите'
                                                     'желаемое имя пользователя, после чего снова нажмите на /start')

async def info(callback: types.CallbackQuery):
    await callback.message.delete()
    await bot.send_message(callback.from_user.id,
                         text='Этот бот предоставляет участникам форума уникальную возможность найти собеседника по интересам!Тут также можно найти группу из 3-ёх человек и общаться группой\nНажми на кнопку, чтобы начать ввод своих данных и получить возможность общаться с другими людьми с форума!',
                         reply_markup=get_info())

async def region(callback: types.CallbackQuery):
    await callback.message.edit_text(
                         text='Пожалуйста напишите свой город или область одним сообщением в следующем формате:\n\n*Москва*\n\nИли в формате:\n*Ленинградская область*',parse_mode="Markdown")
    await FSMall.region.set()

async def reg_yes(message: types.Message, state:FSMContext):
    """Получение региона и создание записи в БД"""
    if message.content_type == 'text':
        async with state.proxy() as data:
            data['username'] = message.from_user.username
            text = message.text
            text= text.lower()
            data['region'] = text
            await add_user_by_region(text, message.from_user.username)
        await state.finish()
        await message.reply("Отлично, теперь выбери, в каком треке ты участвуешь",reply_markup=get_tracks())
    else:
        await bot.send_message(message.from_user.id, text='Пожалуйста, напишите текстом')


async def activity(callback: types.CallbackQuery):
    """Получение текста кнопки
    Получение записи из БД и добавление колонны о деятельности"""
    track = callback.data
    await add_track(callback.from_user.username, track)
    if track == 't1':
        markup = get_activity_putesh()
    elif track == 't2':
        markup = get_activity_trop()
    elif track == 't3':
        markup = get_activity_smisl()
    elif track == 't4':
        markup = get_activity_opener()
    elif track == 't5':
        markup = get_activity_creator()
    elif track == 't6':
        markup = get_activity_region()
    elif track == 't7':
        markup = get_activity_bigger()
    elif track == 't8':
        markup = get_activity_stud()
    await callback.message.edit_text(
                         text='Молодец!\nТеперь давай определим, какой у тебя род деятельности',
                         reply_markup=markup)

async def menu(callback: types.CallbackQuery):
    """Получение колонн из БД, дальше создается другой список для приведения списка к более презентабельному виду"""
    await add_activity(callback.from_user.username, callback.data)
    rows = await get_user(callback.from_user.username)
    rows_for_string = []
    for i in rows:
        if i is None:
            i = 'Не указано'
            rows_for_string.append(i)
        else:
            rows_for_string.append(i)
    await callback.message.edit_text(
                           text=f'*Ваш профиль:*\n_Имя Пользователя:_* @{rows_for_string[0]}*\n'
                                f'_Регион:_* {rows_for_string[1].title()}*\n'
                                f'_Род деятельности:_* {activities_dict[rows_for_string[2]]}*\n'
                                f'_Трек:_* {tracks_dict[rows_for_string[3]]}*\n'
                                '\n\n'
                                'Поздравляем! Теперь ты имеешь доступ ко всем функциям бота, можешь находить собеседника по региону/треку/роду деятельности.\n'
                                'Также ты можешь прочитать инструкцию по использованию функций бота и создать группу по интересам из 3-ёх человек',
                           reply_markup=get_menu(),parse_mode="Markdown")


async def find_man(callback: types.CallbackQuery):
    await callback.message.edit_text(text='По какой информации ты хочешь найти собеседника?',reply_markup=get_man())


async def find_by_region(callback: types.CallbackQuery):
    user = await get_user(callback.from_user.username)
    region = user[1]
    username = callback.from_user.username
    print(username+'fddfhdf')
    random_user = await get_user_by_region(region,username)
    rows_for_string = []
    print(random_user)
    if not random_user:
        await callback.message.edit_text(text='Не получилось найти собеседника из вашего региона :(',reply_markup=get_back())
    else:
        for i in random_user:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        await callback.message.edit_text(text=f'Ваш случайный собеседник:\n\nИмя Пользователя: @{rows_for_string[0]}\n'
                                              f'Регион: {rows_for_string[1].title()}\n'
                                              f'Род деятельности: {activities_dict[rows_for_string[2]]}\n'
                                              f'Трек: {tracks_dict[rows_for_string[3]]}\n')


async def find_by_activity(callback: types.CallbackQuery):
    user = await get_user(callback.from_user.username)
    activ = user[2]
    username = callback.from_user.username
    print(username+'fddfhdf')
    random_user = await get_user_by_activity(activ,username)
    rows_for_string = []
    print(random_user)
    if not random_user:
        await callback.message.edit_text(text='Не получилось найти собеседника с таким же родом деятельности :(',reply_markup=get_back())
    else:
        for i in random_user:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        await callback.message.edit_text(text=f'Ваш случайный собеседник:\n\nИмя Пользователя: @{rows_for_string[0]}\n'
                                              f'Регион: {rows_for_string[1].title()}\n'
                                              f'Род деятельности: {activities_dict[rows_for_string[2]]}\n'
                                                f'Трек: {tracks_dict[rows_for_string[3]]}\n')

async def find_by_track(callback: types.CallbackQuery):
    user = await get_user(callback.from_user.username)
    track = user[3]
    random_user = await get_user_by_track(track, callback.from_user.username)
    print(random_user)
    rows_for_string = []
    if not random_user:
        await callback.message.edit_text(text='Не получилось найти собеседника по такому же треку :(',
                                         reply_markup=get_back())
    else:
        for i in random_user:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        await callback.message.edit_text(text=f'Ваш случайный собеседник:\n\nИмя Пользователя: @{rows_for_string[0]}\n'
                                                         f'Регион: {rows_for_string[1].title()}\n'
                                                         f'Род деятельности: {activities_dict[rows_for_string[2]]}\n'
                                                         f'Трек: {tracks_dict[rows_for_string[3]]}\n')


async def find_many(callback: types.CallbackQuery):
    await callback.message.edit_text(text='По какой информации ты хочешь найти случайных собеседников?',
                                     reply_markup=get_many())

async def many_by_track(callback:types.CallbackQuery):
    """Проверка на то, есть ли вообще юзеры(это надо сделать во всех поисках, иначе будет возвращать None и будет ошибка)"""
    user = await get_user(callback.from_user.username)
    track = user[3]
    results = await get_user_by_track_three(track, callback.from_user.username)
    rows_for_string = []
    if results:
        for i in results:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        if len(results)!=12:
            text = 'Извините, по вашему треку не удалось найти достаточно собеседников :('
        else:
            text = (f'Первый собеседник\nИмя пользователя: @{rows_for_string[0]}\nРегион: {rows_for_string[1]}\nДеятельность: {activities_dict[rows_for_string[2]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[3]]}\n\n'
                    f'Второй собеседник\nИмя пользователя: @{rows_for_string[4]}\nРегион: {rows_for_string[5]}\nДеятельность: {activities_dict[rows_for_string[6]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[7]]}\n\n'
                    f'Третий собеседник\nИмя пользователя: @{rows_for_string[8]}\nРегион: {rows_for_string[9]}\nДеятельность: {activities_dict[rows_for_string[10]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[11]]}\n\n'
                    )
        await callback.message.edit_text(text=text,reply_markup=get_back())
    else:
        await callback.message.edit_text(text='Извините, по вашему треку не удалось найти достаточно собеседников :(',
                                         reply_markup=get_back())


async def many_by_region(callback:types.CallbackQuery):
    """Проверка на то, есть ли вообще юзеры(это надо сделать во всех поисках, иначе будет возвращать None и будет ошибка)"""
    user = await get_user(callback.from_user.username)
    region = user[1]
    results = await get_user_by_region_three(region, callback.from_user.username)
    rows_for_string = []
    if results:
        for i in results:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        if len(results)!=12:
            text = 'Извините, не удалось найти достаточно собеседников из вашего региона:('
        else:
            text = (f'Первый собеседник\nИмя пользователя: @{rows_for_string[0]}\nРегион: {rows_for_string[1]}\nДеятельность: {activities_dict[rows_for_string[2]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[3]]}\n\n'
                    f'Второй собеседник\nИмя пользователя: @{rows_for_string[4]}\nРегион: {rows_for_string[5]}\nДеятельность: {activities_dict[rows_for_string[6]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[7]]}\n\n'
                    f'Третий собеседник\nИмя пользователя: @{rows_for_string[8]}\nРегион: {rows_for_string[9]}\nДеятельность: {activities_dict[rows_for_string[10]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[11]]}\n\n'
                    )
        await callback.message.edit_text(text=text,reply_markup=get_back())
    else:
        await callback.message.edit_text(text='Извините, не удалось найти достаточно собеседников из вашего региона:(',reply_markup=get_back())


async def many_by_activ(callback:types.CallbackQuery):
    """Проверка на то, есть ли вообще юзеры(это надо сделать во всех поисках, иначе будет возвращать None и будет ошибка)"""
    user = await get_user(callback.from_user.username)
    activ = user[2]
    results = await get_user_by_activ_three(activ, callback.from_user.username)
    rows_for_string = []
    if results:
        for i in results:
            if i is None:
                i = 'Не указано'
                rows_for_string.append(i)
            else:
                rows_for_string.append(i)
        if len(results)!=12:
            text = 'Извините, не удалось найти достаточно собеседников с таким же родом деятельности:('
        else:
            text = (f'Первый собеседник\nИмя пользователя: @{rows_for_string[0]}\nРегион: {rows_for_string[1]}\nДеятельность: {activities_dict[rows_for_string[2]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[3]]}\n\n'
                    f'Второй собеседник\nИмя пользователя: @{rows_for_string[4]}\nРегион: {rows_for_string[5]}\nДеятельность: {activities_dict[rows_for_string[6]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[7]]}\n\n'
                    f'Третий собеседник\nИмя пользователя: @{rows_for_string[8]}\nРегион: {rows_for_string[9]}\nДеятельность: {activities_dict[rows_for_string[10]]}\n'
                    f'Трэк: {tracks_dict[rows_for_string[11]]}\n\n'
                    )
        await callback.message.edit_text(text=text,reply_markup=get_back())
    else:
        await callback.message.edit_text(text='Извините, не удалось найти достаточно собеседников с таким же родом деятельности:(',reply_markup=get_back())

async def back(callback: types.CallbackQuery):
    rows = await get_user(callback.from_user.username)
    rows_for_string = []
    for i in rows:
        if i is None:
            i = 'Не указано'
            rows_for_string.append(i)
        else:
            rows_for_string.append(i)
    await callback.message.edit_text(
        text=f'*Ваш профиль:*\n_Имя Пользователя:_* @{rows_for_string[0]}*\n'
             f'_Регион:_* {rows_for_string[1].title()}*\n'
             f'_Род деятельности:_* {activities_dict[rows_for_string[2]]}*\n'
             f'_Трек:_* {tracks_dict[rows_for_string[3]]}*\n'
             '\n\n'
             'Ты вернулся в главное меню.\n'
             'Также ты можешь прочитать инструкцию по использованию функций бота и создать группу по интересам из 3-ёх человек',
        reply_markup=get_menu(),parse_mode="Markdown")


async def manual(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Этот бот создан для взаимодействия участников форума «Больше, чем путешествие»\nПосле нажатия кнопки «Найти человека по информации»'
             'ты можешь выбрать, по какой информации будет найден собеседник. Выбрав это, ты получишь контакты случайного собеседника с таким же треком/регионом/родом деятельности(зависит от того, на какую кнопку ты нажал), как у тебя\n'
             '\nНажимая кнопку «Создать группу из 3-ёх человек» ты получаешь сразу трёх собеседников, каждому из которых ты можешь написать, нажав на Имя Пользователя собеседника.\n\n'
             'Кнопка «Обновить Данные»: если ты ошибся при вводе данных, ты можешь нажать на эту кнопку и переписать их заново.\n\n'
             '*ВАЖНО!*\nПеред работой с ботой убедись, что у тебя установлено Имя Пользователя Telegram\nТакже, убедись, что корректно вводишь свой регион, чтобы другие пользователи смогли тебя найти!',
        reply_markup=get_back(),parse_mode="Markdown")

async def update_user(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text='Пожалуйста напишите свой город или область одним сообщением в следующем формате:\nМосква\nЛенинградская область')
    await FSMupdate.update.set()

async def update_reg(message: types.Message, state:FSMContext):
    """Получение региона и обновление записи в БД"""
    if message.content_type == 'text':
        async with state.proxy() as data:
            data['username'] = message.from_user.username
            text = message.text
            text= text.lower()
            data['region'] = text
            await update_user_region(text, message.from_user.username)
        await state.finish()
        await message.reply("Отлично, теперь выбери, в каком треке ты участвуешь",reply_markup=get_tracks())
    else:
        await bot.send_message(message.from_user.id, text='Пожалуйста, напишите текстом')

#activity_list = ['Представитель оргкомитетов образовательных организаций (ректор, проректор, сотрудник)','Руководитель или активисты студтурклуба','Амбассадор Программы Студтуризм','Представитель вуза, предприятия, региона','Cтудент, готовый развивать направления промышленного туризма в России','Инструктор по туризму','Проводник','Представитель туристических клубов','Представитель особо охраняемых природных территорий','Экскурсовод','Учитель','Представитель региональных органов исполнительной власти в сфере молодежной политики и туризма','Представитель федеральных органов исполнительной власти','Член Экспертного совета программы «Больше, чем путешествие»','Туроператор','Активный участник программы «Больше, чем путешествие»','Представитель программы в поездках','Молодой путешественник','Дирекция конкурсов']

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(info, text='1')
    dp.register_callback_query_handler(region, text='2')
    dp.register_message_handler(reg_yes, content_types=['text'], state=FSMall)
    dp.register_callback_query_handler(activity, text=tracks_dict)
    dp.register_callback_query_handler(menu, text=activities_dict)
    dp.register_callback_query_handler(find_man, text='5')
    dp.register_callback_query_handler(find_many, text='6')
    dp.register_callback_query_handler(many_by_track, text='13')
    dp.register_callback_query_handler(back,text='back')
    dp.register_callback_query_handler(find_by_track, text='10')
    dp.register_callback_query_handler(find_by_region, text='9')
    dp.register_callback_query_handler(find_by_activity, text='11')
    dp.register_callback_query_handler(many_by_region, text='12')
    dp.register_callback_query_handler(many_by_activ, text='14')
    dp.register_callback_query_handler(manual, text='7')
    dp.register_callback_query_handler(update_user, text='8')
    dp.register_message_handler(update_reg, content_types=['text'], state=FSMupdate)
