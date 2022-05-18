from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db

prod = db.View_cat()
cat = db.View_prod()

category = InlineKeyboardMarkup(row_width=2)
for i in prod:
    category.insert(InlineKeyboardButton(text=f'{i[1]}', callback_data=i[0]))
category.insert(InlineKeyboardButton(text='Назад', callback_data='back'))


cate = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Меню',callback_data='menu',url='https://telegra.ph/Menyu-04-01-3')],
        [InlineKeyboardButton(text='Заказать',callback_data='zakaz')],
        [InlineKeyboardButton(text='Корзинка',callback_data='korzina')],
    ]
)

key = InlineKeyboardMarkup(row_width=1)
key.insert(InlineKeyboardButton(text='В корзинку', callback_data='count'))
key.insert(InlineKeyboardButton(text='Назад', callback_data=f'back2'))
key.insert(InlineKeyboardButton(text='Главное меню', callback_data='main'))

user = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить",callback_data="send_to_admin")],
        [InlineKeyboardButton(text="Отмена",callback_data="cancel")]
    ]
)

count2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='+1',callback_data='1'),InlineKeyboardButton(text='+2',callback_data='2'),InlineKeyboardButton(text='+3',callback_data='3')],
        [InlineKeyboardButton(text='+4',callback_data='4'),InlineKeyboardButton(text='+5',callback_data='5'),InlineKeyboardButton(text='+6',callback_data='6')],
        [InlineKeyboardButton(text='+7',callback_data='7'),InlineKeyboardButton(text='+8',callback_data='8'),InlineKeyboardButton(text='+9',callback_data='9')],
        [InlineKeyboardButton(text='Отмена',callback_data='otmena')]
    ]
)
