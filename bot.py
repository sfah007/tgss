import config
import logging
import imgkit
import uuid

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['screenshot'])
async def screenshot(message: types.Message):
    await message.answer('Отправьте сообщением URL к сайту чтобы бот сделал его скриншот')


@dp.message_handler()
async def echo(message: types.Message):
    path_to_img = f"{uuid.uuid4()}.jpg"
    imgkit.from_url(message.text, path_to_img)
    await message.answer(path_to_img)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
