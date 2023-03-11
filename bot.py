


import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters


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
    updater = Updater("6073371023:AAG1YMot-OVMTSLqALmMNjZMVhb5m73psbA", use_context=True)
    dp = updater.dispatcher

    # Add the message handler to the dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, dad_joke_handler))

    # Start the bot
    updater.start_polling()
    logger.info("Dad joke bot started.")
    updater.idle()

if __name__ == '__main__':
    main()

    
     
	     		
