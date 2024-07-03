# Импорт библиотек
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, Message
from aiogram.filters import Command, CommandStart
from aiogram import Bot, Dispatcher
from config import TOKEN
import logging
import asyncio 

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание кнопки для запуска Mini App
def webapp_builder():
    builder = InlineKeyboardBuilder()
    builder.button(
        text = "Пони Таун!!!", web_app=WebAppInfo(
            url="https://pony.town/"
        )
    )
    return builder.as_markup()

# Команда /start
@dp.message(CommandStart)
async def send_welcome(message: Message):
    # Подключение кнопки для запуска Mini App к сообщению и вывод пользователю
    await message.answer(f"Привет,{message.chat.first_name}! Этот тестовый бот, иди поиграй в поняшек!", reply_markup=webapp_builder())


# Сообщение будет отправлено, если пользователь написал обычное сообщение, а не команду
@dp.message()
async def diff(message: Message):
    await message.answer("Команда нераспознана, повторите попытку")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Начало работы бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    # Хз, чек видео в ютубе
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')