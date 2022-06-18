from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
from main import chat_anwser

logging.basicConfig(level=logging.INFO)

TOKEN = "5578817522:AAEx2Ag3nE3hvsHDCPBuzTxt0JZ03U-4qak"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Ayam Goreng", callback_data="ayam_goreng")
button2 = InlineKeyboardButton(text="Bebek Goreng", callback_data="bebek_goreng")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

@dp.message_handler(commands="start")
async def hello(message: types.Message):
    await message.answer("Halo kawan AITers!")\

@dp.message_handler(commands="menu")
async def logo(message: types.Message):
    await message.answer_photo('https://assets-pergikuliner.com/ISj6nCpB4NpFEvg6GCCVt6AVWZs=/945x0/smart/filters:watermark(https://assets-pergikuliner.com/assets/pegimakan-logo-3e147c56e232f471596371920946ae65.png,-0,-3,10):no_upscale()/https://assets-pergikuliner.com/uploads/image/picture/1575025/picture-1567758425.JPG')


@dp.message_handler(commands="pesan")
async def pesan(message: types.Message):
    await message.answer("Hai! Mau pesan apa?", reply_markup=keyboard_inline)\

@dp.callback_query_handler(text=["ayam_goreng", "bebek_goreng"])
async def pesanan(call: types.CallbackQuery):
    if call.data == "ayam_goreng":
        await call.message.answer("Oke kamu memesan Ayam Goreng")
    if call.data == "bebek_goreng":
        await call.message.answer("Oke kamu memesan Bebek Goreng")
    await call.answer()

@dp.message_handler()
async def hello(message: types.Message):
    answer = chat_anwser(message.text)
    print(answer)
    await message.answer(answer)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)

