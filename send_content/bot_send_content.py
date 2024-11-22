from aiogram import Bot, Dispatcher, executor, types

TOKEN_BOT = 'ТОКЕН ТВОЕГО БОТА'

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    with open('frog.jpg', mode='rb') as file:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=file,
                             caption='Когда научился отправлять фото!')


@dp.message_handler(commands=['install_photo'])
async def send_doc_photo(message: types.Message):
    with open('frog.jpg', mode='rb') as file:
        await bot.send_document(chat_id=message.from_user.id,
                                document=file,
                                caption='Теперь можешь скачать фотку!')


@dp.message_handler(commands=['send_doc'])
async def send_doc(message: types.Message):
    with open('my_file.txt', mode='rb') as file:
        await bot.send_document(chat_id=message.from_user.id,
                                document=file,
                                caption='Забери свой файл!')


@dp.message_handler(commands=['video'])
async def send_video(message: types.Message):
    with open('video.mp4', mode='rb') as file:
        await bot.send_video(chat_id=message.from_user.id,
                             video=file,
                             caption='Держи видео!')


@dp.message_handler(commands=['audio'])
async def send_audio(message: types.Message):
    with open('audio.mp3', mode='rb') as file:
        await bot.send_audio(chat_id=message.from_user.id,
                             audio=file,
                             caption='Для релаксации')
        await bot.send

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
