from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
import emoji

from random import randint
from config import TOKEN
import processor as p

from loader import logging

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Глобальные переменные - список игрового поля, словарь имен игроков, флаги
gamefield, cia = [' '] * 16, True
players = {True: 'Крестики', False: 'Нолики'}
bloced_gamefield = False



def get_keys(win_flag=False):
    # Генератор клавиатуры - на основе глобальной переменной со списком игрового поля
    global gamefield, bloced_gamefield
    buttons = []
    for i in range(len(gamefield)):
        buttons.append(types.InlineKeyboardButton(text=gamefield[i], callback_data=i+1))
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    if win_flag:
        bloced_gamefield = True
        keyboard.add(types.InlineKeyboardButton(text='Запустить игру заново', callback_data='reset'))
    return keyboard


@dp.message_handler(commands=["help", "start", "stop"])
async def cmd_numbers(message: types.Message):
    global gamefield, players, cia
    match message.text[1:]:
        case 'help':
            logging.info('Запущена команда /help')
            await message.reply(f'Привет, {message.from_user.first_name}!\n' +
                                '/help - вывод списка команд\n' +
                                '/start - запуск игры\n' +
                                '/stop - завершить игру', reply=False)
        case 'start':
            logging.info('Запущена команда /start')
            await new_game(message)
        case 'stop':
            logging.info('Запущена команда /stop')
            user_name = message.from_user.first_name
            await message.reply(f"До встречи, {user_name}")
            logging.info('Бот остановлен!')
            dp.stop_polling()
            


@dp.message_handler()  # реакция на любой текст, кроме перечисленных выше команд
async def cmd_numbers(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, введи /help для отображения списка команд', reply=False)


async def update_fld(message: types.Message, new_value: int):
    global players, cia, bloced_gamefield
    # Общая функция для обновления текста с отправкой клавиатуры
    if p.check_4_win(gamefield):
        win_str = 10*'*'+f'{players[not cia].upper()} ПОБЕДИЛИ!!!!'+ 10*'*'
        logging.info(f'Конец игры! {players[not cia]} победили!!!')
        bloced_gamefield = True
        await message.edit_text(f"{win_str}", reply_markup=get_keys(True))
    elif not p.isfull(gamefield):
        await message.edit_text(f"{new_value}", reply_markup=get_keys())
    else:
        win_str = 5*'\U0001F4A5'+' НИЧЬЯ! ' + 5*'\U0001F4A5'
        logging.info(f'Дружеская ничья!!!')
        await message.edit_text(f"{win_str}", reply_markup=get_keys(True))


async def new_game(message: types.Message):
    global gamefield, cia
    gamefield, cia = [' '] * 16, bool(randint(0, 1)) 
    try:
        await message.edit_text(f"Ходят {players[cia].lower()}:", reply_markup=get_keys())
    except exceptions.MessageCantBeEdited:
        await message.answer(f"Ходят {players[cia].lower()}:", reply_markup=get_keys())


@dp.callback_query_handler()
async def callbacks_num(call: types.CallbackQuery):
    global cia, gamefield, players, bloced_gamefield  
    action = call.data
    # обработка нажатия кнопок
    if bloced_gamefield == False:
        if action.isdecimal():
            if gamefield[int(action)-1] == ' ':
                gamefield[int(action)-1] = '\U0000274C' if cia else '\U00002B55'
                # p.write_log(p.t(), f'Состояние поля: {gamefield}')
                cia = not cia
                out_val = f'Ходят {players[cia].lower()}:'
                await update_fld(call.message, out_val)
            else:   
                await call.answer()
                return
    else:
        if action == 'reset':  # новая игра - сброс инициальных параметров
            bloced_gamefield = False
            await new_game(call.message)
            return
    await call.answer()


if __name__ == '__main__':
    try:
        logging.info('Старт сервера - начало работы бота')
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
       logging.info('Остановка сервера - завершение работы бота')


