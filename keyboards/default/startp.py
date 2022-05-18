from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

count1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"),
         KeyboardButton(text="3")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"),
         KeyboardButton(text="6")],
        [KeyboardButton(text="7"), KeyboardButton(text="8"),
         KeyboardButton(text="9")],
        [KeyboardButton(text="Отмена")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


contactnum = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделиться номером", request_contact=True)
        ]
    ],
    resize_keyboard=True,
)

send_loc = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Поделиться геопозицией', request_location=True)]
    ],
    resize_keyboard=True,
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Да, все верно!'),KeyboardButton(text='Нет, не верно!')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
