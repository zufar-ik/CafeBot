from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

from keyboards.default.startp import contactnum, yes_no, send_loc
from keyboards.inline.inn import category, cate, key, user, count2
from loader import db
from loader import dp
from states.state import Call, Cart, Zakaz
import re

prod = db.View_prod()
cats = db.View_cat()


@dp.callback_query_handler(text='zakaz', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите категорию!', reply_markup=category)
    await Call.upload.set()


@dp.callback_query_handler(text='menu', state='*')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Выберите категорию!', reply_markup=category)


@dp.callback_query_handler(text='back', state='*')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(text='Может что нибудь закажем?', reply_markup=cate)


for i in cats:
    @dp.callback_query_handler(text=f'{i[0]}', state='*')
    async def get_data(call: types.CallbackQuery, state: FSMContext):
        call1 = call.data
        hp = db.where_cat(id=call1)
        await state.update_data(
            {'call2': call1}
        )
        data_call = InlineKeyboardMarkup(row_width=1)
        idq = db.where_prod(clas_id=call1)
        for cat in idq:
            data_call.insert(InlineKeyboardButton(text=f'{cat[3]}', callback_data=f'{cat[6]}'))
        data_call.insert(InlineKeyboardButton(text='Назад', callback_data='back1'))
        data_call.insert(InlineKeyboardButton(text='Главное меню', callback_data='main'))
        if idq:
            await call.message.edit_text(f"{hp[0][2]}",
                                         reply_markup=data_call)
        elif not idq:
            await call.answer('Скоро добавим')
        # await call.message.edit_text('Скоро добавим!',reply_markup=data_call)
        await Call.download.set()


@dp.callback_query_handler(text='back1', state='*')
async def back1(call: types.CallbackQuery):
    await call.message.edit_text("Выберите категорию ниже!", reply_markup=category)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


for i in prod:
    @dp.callback_query_handler(text=f'{i[6]}', state='*')
    async def get_more(call: types.CallbackQuery, state: FSMContext):
        call2 = call.data
        await state.update_data(
            {'name': call2}
        )
        idq = db.where_prod(slug=call2)
        for product in idq:
            await call.message.answer_photo(photo=(open(f"DJANGO/{product[4]}", "rb")),
                                            caption=f'<b>{product[3]}</b>\n\n'
                                                    f'{product[5]} сум\n\n'
                                                    f'{product[2]}', reply_markup=key)
        await call.message.delete()
        await Call.upload.set()


@dp.callback_query_handler(text='count', state='*')
async def add(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=count2)
    await Cart.add.set()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.callback_query_handler(state=Cart.add)
async def add(call: types.CallbackQuery, state: FSMContext):
    n = call.data
    data = await state.get_data()
    CALL = data.get('name')
    NAME = db.where_prod(slug=CALL)
    if is_number(n) == True and 0 < int(n):
        idname = call.from_user.id
        for i in NAME:
            product = db.check_product(tg_id=call.from_user.id, name=i[3])
            print(product)
            if product:
                db.update_product(tg_id=idname, name=i[3], quantity=int(product[2]) + int(n), price=i[5])
            else:
                db.add_product(tg_id=idname, name=i[3], quantity=int(n), price=i[5])
            await call.answer('Ваш заказ добавлен в корзинку!', show_alert=True)
            await call.message.delete()
            await call.message.answer('Выберите категорию', reply_markup=cate)

    elif n == 'otmena':
        await call.message.delete()
        await call.message.answer('Выберите категорию', reply_markup=cate)
    else:
        await call.message.answer(text='Ой! Походу вы ввели некорректный символ.', reply_markup=count2)
    await state.finish()


for i in cats:
    @dp.callback_query_handler(text='back2', state='*')
    async def get_data(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        call1 = data.get('call2')
        hp = db.where_cat(id=call1)
        data_call = InlineKeyboardMarkup(row_width=1)
        idq = db.where_prod(clas_id=call1)
        for cat in idq:
            data_call.insert(InlineKeyboardButton(text=f'{cat[3]}', callback_data=f'{cat[6]}'))
        data_call.insert(InlineKeyboardButton(text='Назад', callback_data='back1'))
        data_call.insert(InlineKeyboardButton(text='Главное меню', callback_data='main'))
        await call.message.delete()
        await call.message.answer(f"{hp[0][2]}",
                                  reply_markup=data_call)
        await Call.upload.set()


@dp.callback_query_handler(text='main', state='*')
async def main(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите категорию', reply_markup=cate)


@dp.callback_query_handler(text='korzina', state='*')
async def korzina(call: types.CallbackQuery):
    products1 = db.get_products(tg_id=call.from_user.id)
    if len(products1) != 0:
        markup = InlineKeyboardMarkup(row_width=2)
        products = db.get_products(tg_id=call.from_user.id)
        for i in products:
            markup.insert(InlineKeyboardButton(text=i[1], callback_data='none'))
        total = 0
        msg = "Ваши заказы\n\n"
        for product in products:
            narx = (int(product[4]) * int(product[2]))
            total += narx
            msg += f"<a>{product[1]}</a>\n\n{product[4]} x {product[2]} = {narx} сум\n\n -------------------------------------\n"
        msg += f"\nОбщая сумма: {total} сум"
        markup.insert(InlineKeyboardButton("Заказать 🚚", callback_data='jj'))
        markup.insert(InlineKeyboardButton(text='Очистить 🗑', callback_data='clear'))
        markup.insert(InlineKeyboardButton(text='Назад', callback_data='back'))
        await call.message.answer(msg, reply_markup=markup)
    else:
        await call.message.edit_text("Ваша корзинка еще пуста! Может быть это исправим?")
        await call.message.answer("Выберите категорию", reply_markup=category)


@dp.callback_query_handler(text='none')
async def none(call: types.CallbackQuery):
    await call.answer('Да, давай закажем это аппетитное блюдо!!!!', show_alert=False)


@dp.callback_query_handler(text='clear')
async def clear(call: types.CallbackQuery):
    id = call.from_user.id
    db.clear_cart(tg_id=id)
    await call.message.edit_text('Ваша корзинка очищена!', reply_markup=cate)


@dp.callback_query_handler(text="jj", state='*')
async def send(call: types.CallbackQuery):
    products = db.get_products(tg_id=call.from_user.id)
    total = 0
    msg = "Ваши заказы\n\n"
    for product in products:
        narx = (int(product[4]) * int(product[2]))
        total += narx
        msg += f"{product[1]}\n\n{product[4]} x {product[2]} = {narx} сум\n\n-------------------------------------\n"
    msg += f"\nОбщая сумма: {total} сум"
    await call.message.delete()
    await call.message.answer(msg)
    await call.message.answer('Все верно?', reply_markup=yes_no)
    await Zakaz.start.set()


@dp.message_handler(text="Да, все верно!", state=Zakaz.start)
async def ye(message: types.Message):
    await message.answer("Заполните нужные пункты пожалуйста")
    await message.answer("Как вас зовут?")
    await Zakaz.name.set()


@dp.message_handler(state=Zakaz.name)
async def name(message: types.Message, state: FSMContext):
    id1 = message.from_user.id
    await state.update_data(
        {"id": id1}
    )
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Введите адрес доставки", reply_markup=send_loc)
    await Zakaz.next()


@dp.message_handler(content_types=['location'], state=Zakaz.Adress)
async def adress(message: types.Message, state: FSMContext):
    adress1 = message.location
    await state.update_data(
        {"adress": adress1}
    )
    await message.answer("Введите основной номер!", reply_markup=contactnum)
    await Zakaz.next()


@dp.message_handler(content_types=['contact'], state=Zakaz.tel)
async def get_img(message: types.Message, state: FSMContext):
    phone = message.contact['phone_number']
    num = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    if re.match(num, phone):
        await state.update_data(
            {'phone': phone}
        )
        await message.answer("Введите второстепенный номер!\n"
                             "(если его нет отправьте любой знак)", reply_markup=ReplyKeyboardRemove())
        await Zakaz.next()
    else:
        await message.answer("Вы ввели некорректный номер\n"
                             "Введите еще раз!")
        await Zakaz.tel


@dp.message_handler(state=Zakaz.tel2)
async def get_img(message: types.Message, state: FSMContext):
    tel2 = message.text
    await state.update_data(
        {'tel2': tel2}
    )
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    Username = message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    idq = message.from_user.id
    lat = (adress1['latitude'])
    long = (adress1['longitude'])
    await message.bot.send_location(chat_id=idq, latitude=lat, longitude=long)
    await message.answer(
        text=f"Имя и фамилия: {name}\n"
             f"Основной номер: +{telnum1}\n"
             f"Username: @{Username}\n"
             f"Второстепенный: +{telnum2}", reply_markup=user
    )
    await Zakaz.next()


@dp.callback_query_handler(text="cancel", state=Zakaz.confirmP)
async def back(call: types.CallbackQuery):
    await call.message.answer("Вы отменили заказ!", reply_markup=cate)
    await call.message.delete()


@dp.callback_query_handler(text="send_to_admin", state=Zakaz.confirmP)
async def sendadmin(call: types.CallbackQuery, state: FSMContext):
    data1 = await state.get_data()
    name = data1.get("name")
    adress1 = data1.get("adress")
    telnum1 = data1.get("phone")
    telnum2 = data1.get("tel2")
    id1 = data1.get("id")
    Username = call.message.from_user.username
    await state.update_data(
        {"username": Username}
    )
    username = data1.get("username")
    products = db.get_products(tg_id=id1)
    total = 0
    msg = "Его заказы\n\n"
    for product in products:
        narx = (int(product[4]) * int(product[2]))
        total += narx
        msg += f"{product[1]}\n\n{product[4]} x {product[2]} = {narx} сум\n\n-------------------------------------\n"
    msg += f"\nОбщая сумма: {total} сум"
    idq = 1297546327
    lat = (adress1['latitude'])
    long = (adress1['longitude'])
    await call.bot.send_location(chat_id=idq, latitude=lat, longitude=long)
    await call.bot.send_message(chat_id=1297546327,
                                text=f"{msg}\n"
                                     f"Имя и фамилия: {name}\n"
                                     f"Основной номер: +{telnum1}\n"
                                     f"Username: @{username}\n"
                                     f"Второстепенный: +{telnum2}"
                                )
    await call.message.answer("Ваш заказ не будет отправлен!\n"
                              "Этот раздел только для демонстрации наших сил😊", reply_markup=cate)
    await call.message.delete()

    db.clear_cart(tg_id=id1)

    await state.finish()
