from aiogram.utils import executor
from handlers import client, admin
from create_bot import dp
from database import sql_start
from database_admin import sql_admins_start




async def on_startup(_):
    await sql_start()
    await sql_admins_start()
    print('Бот в онлайне')


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
