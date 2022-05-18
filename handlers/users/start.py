import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.inline.inn import cate
from loader import db, bot
from loader import dp


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Добавляем пользователей в базу
    try:
        db.add_user(tg_id=message.from_user.id,
                    username= message.from_user.username,
                    id= message.from_user.id,
                    lname=name)
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет ....\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>")
        await message.answer("Выберите категорию",reply_markup=cate)
        # Оповещаем админа
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу пользователей.\nВ базе есть {count} людей."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} в базе имелся раньше")
        await message.answer(f"Добро пожаловать! {name}\n\n"
                             f"🤖 Я бот который поможет ....\n\n"
                             f"🤝 Заказать похожего или совсем иного бота? Свяжитесь с разработчиком <a href='https://t.me/zufar_ik'>Zufar</a>")
        await message.answer("Выберите категорию",reply_markup=cate)
