
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from loader import dp, db
@dp.message_handler(text='Корзинка 🛒')
async def korzina(message: types.Message):
    products1 = db.get_products(tg_id=message.from_user.id)
    if len(products1) != 0:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Заказать 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Ваши заказы\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} $\n"
        msg += f"\nОбщая сумма: {total} $"
        markup.row("Назад", "Очистить 🗑")
        await message.answer(msg, reply_markup=markup)
    else:
        await message.answer("Ваша корзинка еще пуста! Может быть это исправим?", reply_markup=tel)
        await Phone.category.set()


@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Name=product.strip())
    await message.answer(f"{product.strip()} Ваша корзинка удалена!", reply_markup=menuAll)


@dp.message_handler(text="Очистить 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Ваша корзинка очищена!", reply_markup=menuAll)


@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("Вы нажали назад", reply_markup=menuAll)


@dp.message_handler(text="Заказать 🚚")
async def send(message: types.Message):
    products = db.get_products(tg_id=message.from_user.id)
    total = 0
    msg = "Ваши заказы\n\n"
    for product in products:
        price = get_price(product[1], product[2])
        total += price
        msg += f"{product[1]} x {product[2]} = {price} $\n"
    msg += f"\nОбщая сумма: {total} $"
    yes_no = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no.add("Да!")
    yes_no.add("Нет!")
    await message.answer(msg)
    await message.answer("Все верно?", reply_markup=yes_no)
