import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the dad joke function
def dad_joke(update, context):
    text = update.message.text.lower()
    if text.startswith(("i'm", "im")):
        name = text[3:].strip()
        joke = f"Hi {name}, I'm Dad!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=joke)

# Define the start command function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am a dad joke bot. Send me a message starting with 'im' or 'I'm' and I'll tell you a dad joke!")

def main():
    # Get the Telegram bot token from the environment variable
    token = os.getenv('TELEGRAM_TOKEN')

    # Create the Updater and pass in the token
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add the handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, dad_joke))

    # Start the bot
    updater.start_polling()
    logger.info('Dad joke bot started.')
    updater.idle()

if __name__ == '__main__':
    main()
