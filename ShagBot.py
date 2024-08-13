from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '' # апи-ключ
bot = Bot(token=api) # сам бот
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')
    await message.answer('Urban message')

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Start message')
    await message.answer('Привет! Я бот, помогающий Вашему здоровью')

@dp.message_handler() # все общие хендлеры в конец специальных!
async def all_message(message):
    print('Мы получили сообщение')
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)























