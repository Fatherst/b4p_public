from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
API_TOKEN = 'TOKEN'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)