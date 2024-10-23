from aiogram import Bot, Dispatcher, executor, types

TOKEN_BOT = 'ТВОЙ_ТОКЕН_БОТА'

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)

