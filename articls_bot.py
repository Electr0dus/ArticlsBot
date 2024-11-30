from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


TOKEN_BOT = 'ТВОЙ ТОКЕН'

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

k1 = KeyboardButton('Первая')
k2 = KeyboardButton('Вторая')
k3 = KeyboardButton('Третья')

kb.add(k1).add(k2).insert(k3)


@dp.message_handler(text='Первая')
async def kb1(message: types.Message):
    await message.answer(text='Нажал на кнопку 1')

@dp.message_handler(text='Вторая')
async def kb2(message: types.Message):
    await message.answer(text='Нажал на кнопку 2')

@dp.message_handler(text='Третья')
async def kb3(message: types.Message):
    await message.answer(text='Нажал на кнопку 3')


@dp.message_handler(commands=['keyboard'])
async def echo_message(message: types.Message):
    await message.answer(text='Твоя клавиатура', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)