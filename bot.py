
import psycopg2

import asyncio
from datetime import datetime
from typing import Optional

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup    
from aiogram.dispatcher.filters import Text
import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.middlewares.logging import LoggingMiddleware



API_TOKEN = '6073371023:AAG1YMot-OVMTSLqALmMNjZMVhb5m73psbA'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the callback function for the message handler
def dad_joke_handler(update, context):
    message = update.message.text
    if message.startswith("I'm") or message.startswith("i'm"):
        name = message[3:]
        response = f"Hi {name}, I'm Dad!"
        update.message.reply_text(response)

# Define the main function to run the bot
def main():
    # Set up the bot and the dispatcher
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add the message handler to the dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, dad_joke_handler))

    # Start the bot
    updater.start_polling()
    logger.info("Dad joke bot started.")
    updater.idle()

if __name__ == '__main__':
    main()
  

    
     
	     		
