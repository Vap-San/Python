from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import logging


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)  


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler("my_log.log", encoding='utf-8', mode='w')],
        level=logging.INFO,
)

