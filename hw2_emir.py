import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)      # это обьект или экземпляр класса
dp = Dispatcher()               # обработчик входящих обновлений


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}"
    )

    print(f"Написал пользователь {message.from_user.full_name} его ID, {message.from_user.id} его ник, {message.from_user.username}")

 
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветсвие\n'
        '/help - список команд'
    )


@dp.message(F.text.lower() == 'группа')
async def cmd_group(message: Message):
    await message.answer("Твоя группа это 69-1")


# @dp.message(F. == 'группа')
# async def cmd_group(message: Message):
#     await message.answer("Твоя группа это 69-1")


@dp.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот бот создан для обучения в рамках курса по Python"
    )

@dp.message(F.text.lower() == 'пока')
async def cmd_bye(message: Message):
    await message.answer(f"Пока, {message.from_user.full_name}!")



@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
