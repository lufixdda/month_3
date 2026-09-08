from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from src.keyboards import keybord_main, inline
from src.questions import QUESTIONS

router = Router()

class Quiz(StatesGroup):
    waiting_for_answer = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}",
        reply_markup=keybord_main
    )

    print(f"Написал пользователь {message.from_user.full_name} его ID, {message.from_user.id} его ник, {message.from_user.username}")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветсвие\n'
        '/help - список команд',
        reply_markup=inline
    )


@router.message(F.text.lower() == 'группа')
async def cmd_group(message: Message):
    await message.answer("Твоя группа это 69-1")


@router.message(F.text == 'Каталог')
async def cmd_catalog(message: Message):
    await message.answer("Наш каталог к сожалению пуст :(")


@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Начинаем игру!", show_alert=True)
    await state.update_data(index = 0, score = 0)
    await state.set_state(Quiz.waiting_for_answer)

    await callback.message.answer('Вопрос 1: ' + QUESTIONS[0]['q'])

@router.message(Quiz.waiting_for_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data.get('index')
    score = data.get('score')

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer('Правильно!, Бонжур! +1')
    else:
        await message.answer(f'Неправильно! Правильный ответ: {QUESTIONS[index]["a"]}')

    index += 1
    len_questions = len(QUESTIONS)
    if index == len_questions:
        await message.answer(f'Конец! счет:{score}/{len_questions}')
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f'Вопрос {index + 1}: ' + QUESTIONS[index]['q'])



@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот бот создан для обучения в рамках курса по Python"
    )


@router.message(F.text.lower() == 'пока')
async def cmd_bye(message: Message):
    await message.answer(f"Пока, {message.from_user.full_name}!")


@router.message(F.text.lower() == 'java')
async def cmd_java(message: Message):
    await message.answer('Java — это объектно-ориентированный язык программирования высокого уровня,\n'
                        'созданный компанией Sun Microsystems (ныне Oracle) в 1995 году\n'
                        'Основная идея Java — "Write Once, Run Anywhere"')

@router.message(F.text.lower() == 'python')
async def cmd_python(message: Message):
    await message.answer('Python — это высокоуровневый язык программирования общего назначения, \n'
                        'который был создан Гвидо ван Россумом и впервые выпущен в 1991 году.\n'
                        'Python известен своей простотой и читаемостью кода, что делает его популярным среди начинающих программистов и профессионалов.\n'
                        'Он поддерживает несколько парадигм программирования, включая объектно-ориентированное, процедурное и функциональное программирование.')

@router.message(F.text.lower() == 'javascript')
async def cmd_javascript(message: Message): 
    await message.answer('JavaScript — это высокоуровневый, интерпретируемый язык программирования, \n'
                        'который является одним из основных технологий веб-разработки наряду с HTML и CSS.\n'
                        'Он был создан Бренданом Айком в 1995 году и изначально назывался Mocha, затем LiveScript, а позже получил название JavaScript.\n'
                        'JavaScript позволяет создавать интерактивные элементы на веб-страницах, управлять поведением браузера и взаимодействовать с сервером.')


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
