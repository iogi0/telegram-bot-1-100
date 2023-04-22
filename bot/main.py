import logging
import aiogram
import random
from aiogram import Bot,Dispatcher,types,executor

TOKEN = '6133107533:AAHElHmcdx7jFK2wmNg4amsLpF6Ev0rr6zY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

number = random.randint(1, 100) 

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привіт! я пропоную тобі вгадати число,яке я загадав (від 1 до 100).що б розпочати гру нажми на /game') #, reply_markup=start_button

# @dp.callback_query_handler()
# async def get_info(callback_query: types.CallbackQuery):
#     if callback_query.data == 'start':
#         await message.ansver('123')

@dp.message_handler(commands='game')
async def game(message: types.Message):
    await message.answer('гру розпочато! напиши число від 1 до 100')

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def guess_number(message: types.Message):
# перевіряємо,чи ввів користувач число, у противному випадку застосовуєм except
    try: 
        guess = int(message.text)
#перевірка введеного числа з загаданим 
        if guess < number:
            await message.reply('я загадав більше число')
        elif guess > number:
            await message.reply('я загадав менше число')
# якщо користувач вгадує число,гра закінчується
        else:
            await message.reply('ви вгадали! що б почати нову гру введіть команду /game ')
    except:
        await message.reply('я сказав число від 1 до 100.')

# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# start_button = InlineKeyboardMarkup(
#     inline_keyboard=[
#         InlineKeyboardButton(text='почати гру',callback_data='game')
#     ]
# )
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)