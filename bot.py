import config
import logging
import imgkit

from aiogram import Bot, Dispatcher, executor, types


path_wkthmltoimage = config.PATH_TO_WKHTMLTOPDF
img_config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['screenshot'])
async def screenshot(message: types.Message):
    await message.answer('Отправьте сообщением URL к сайту чтобы бот сделал его скриншот')


@dp.message_handler()
async def echo(message: types.Message):
    options = {
        'format': 'png',
        'width': 1920,
        'height': 1080,
        'disable-smart-width': '',
        'encoding': "UTF-8",
        'javascript-delay': 10,
        'custom-header': [
            ('User-Agent',
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
        ],
    }

    await message.answer('подождите пожалуйста')

    try:
        img = imgkit.from_url(message.text, False, options=options, config=img_config)
        await bot.send_photo(
            message['from']['id'],
            img,
            caption=message.text
        )
    except:
        await message.answer('Укажите правильный адрес к сайту! Сайт не отвечает либо указан не верно')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
