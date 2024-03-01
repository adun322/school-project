from aiogram import Dispatcher, Bot, executor, types

TOKEN = '' # put your token

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text='Привет')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
