from aiogram.dispatcher.filters.state import StatesGroup, State


class Reklama(StatesGroup):
    reklama = State()

class Call(StatesGroup):
    upload = State()
    download = State()

class Cart(StatesGroup):
    add = State()
    confirm = State()

class Zakaz(StatesGroup):
    start = State()
    name = State()
    Adress = State()
    tel = State()
    tel2 = State()
    confirmP =State()
