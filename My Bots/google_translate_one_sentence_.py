import logging
from googletrans import Translator
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LANGUAGE, ENGLISH, ARABIC = range(3)


def start(update, context):
    reply_keyboard = [['EN', 'AR']]
    user_name = update.message.chat.first_name
    update.message.reply_text(
        f'Hi {user_name}!\nMy name is Meta Bot. I will translate any sentence.'
        '\nSend /cancel to stop talking to me.')
    update.message.reply_text('choose the language :',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, reply_keyboard=False, resize_keyboard=True))

    return LANGUAGE


def translate_english(update, context):

    update.message.reply_text('Lets Start Translate To Arabic.\nInput English sentence:', reply_markup=ReplyKeyboardRemove())

    return ENGLISH


def translate_arabic(update, context):

    update.message.reply_text('Lets Start Translate To English.\nInput Arabic sentence:', reply_markup=ReplyKeyboardRemove())

    return ARABIC


def english_to_arabic(update, context):
    # init the Google API translator
    translator = Translator()

    # translate a spanish text to arabic for instance
    translation = translator.translate(update.message.text, dest="ar")
    result = translation.text
    update.message.reply_text(result)

    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def arabic_to_english(update, context):
    # init the Google API translator
    translator = Translator()

    # translate a spanish text to arabic for instance
    translation = translator.translate(update.message.text, dest="en")
    result = translation.text
    update.message.reply_text(result)

    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5013210105:AAHnsnoEsm7OYENZw9WniG74Bfm5g2Ii58s", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            LANGUAGE: [MessageHandler(Filters.text('EN'), translate_english), MessageHandler(Filters.text('AR'), translate_arabic)],
            ENGLISH: [MessageHandler(Filters.text, english_to_arabic)],
            ARABIC: [MessageHandler(Filters.text, arabic_to_english)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()