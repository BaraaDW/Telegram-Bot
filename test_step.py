
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir😍\nwelcome To My Bot💙.\nwrite /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Available commands :\n/test - To testing.')


def testing(update: Update, context: CallbackContext):
    update.message.reply_text('hi hi hi hi')


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry I can't recognize you , you said '{update.message.text}'")


def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry '{update.message.text}' is not a valid command")


def main():
    """Start the bot."""
    updater = Updater("5013210105:AAHnsnoEsm7OYENZw9WniG74Bfm5g2Ii58s", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('test', testing))

    # ___(END)___
    dp.add_handler(MessageHandler(Filters.command, unknown_command))
    dp.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()
    # updater.idle()


if __name__ == '__main__':
    main()
