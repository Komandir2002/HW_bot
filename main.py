from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from config import bot, dp


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Команды:\n/start\n/quiz\n/help")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Кто создал pyhton?"
    answers = [
        "Гвидо ван Россум",
        "Микилянжело",
        "Стив Жобс",
        "Ворен Бафет",
        "Чин Кан",
        "Нет правильного ответа",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Это был Гвидо ван Россум",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Каком году был основан Python?"
    answers = [
        "1900г",
        "2000г",
        "в начале 1980",
        "конце 1980г",
        "1844",
        "1945",
        "Нет правильного ответа",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Это было в начале 1980",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "Объясните разницу между списком и кортежем"
    answers = [
        "Список изменяемый,a кортеж - нет",
        "Нету разницы",
        "Спискок не изменяемый, а кортеж изменяемый",
        "не знаю",
        "Нет правильного ответа",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Это было в начале 1980",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_3(call: types.CallbackQuery):
    question = "Какая функция возврашает 3 пункт задачи"
    answers = [
        "print(list += list)",
        "def sum_slt(lst):\nsum = lst + lst\nprint(sum)",
        "lamda(x+x)",
        "Нет правильного ответа",
    ]
    photo = open("media/mwe.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)