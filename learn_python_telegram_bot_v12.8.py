from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from googletrans import Translator
from PIL import Image
import random


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"✨ Hello, {update.message.chat.first_name} !"
                              f"\nwelcome To My Bot💙."
                              f"\nwrite /basic to see what Bot do."
                              f"\nwrite /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Available commands :\n1) /facebook - To get the facebook URL.'
                              '\n2) /StartConversation - To talk with bot.'
                              '\n3) /StartGoogleTranslator - To translate text.'
                              '\n4) /info - To show your data.'
                              '\n5) /img - Bot will send photo.')


def basic_bot(update: Update, context: CallbackContext):
    update.message.reply_text('1) if send text : go to google translator.'
                              '\n2) if send photo : Bot will save it.'
                              '\n3) if send voice : Bot will save it.')


def facebook_url(update: Update, context: CallbackContext):
    face_url = 'https://www.facebook.com/'
    update.message.reply_text(f"facebook link is {face_url}")


def start_conversation(update: Update, context: CallbackContext):
    update.message.reply_text(f"Welcome to conversation with me.")


def conversation(update: Update, context: CallbackContext):
    user_line = update.message.text
    if user_line == "hi":
        update.message.reply_text('hi sir.')
    elif user_line == "how are you?":
        update.message.reply_text('good, and you sir?')
    elif user_line == "what is your name?":
        update.message.reply_text('Napom sir.')
    else:
        pass


def start_google_translator(update: Update, context: CallbackContext):
    update.message.reply_text(f"Welcome to Google Translator\nEnter your text.")


def google_translator(update: Update, context: CallbackContext):
    # init the Google API translator
    translator = Translator()

    # translate a spanish text to arabic for instance
    translation = translator.translate(update.message.text, dest="ar")
    result = translation.text
    update.message.reply_text(result)


def user_information(update: Update, context: CallbackContext):
    update.message.reply_text(f"Wlcome your information is:")
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text=f'chat_id : {chat_id}')
    context.bot.send_message(chat_id=chat_id, text=f'chat_type : {update.message.chat.type}')
    context.bot.send_message(chat_id=chat_id, text=f'chat.username : {update.message.chat.username}')
    context.bot.send_message(chat_id=chat_id, text=f'chat.first_name : {update.message.chat.first_name}')
    context.bot.send_message(chat_id=chat_id, text=f'text : {update.message.text}')
    context.bot.send_message(chat_id=chat_id, text=f'message_id : {update.message.message_id}')
    context.bot.send_message(chat_id=chat_id, text=f'date : {update.message.date}')
    context.bot.send_message(chat_id=chat_id, text=f'photo : {update.message.photo}')


def send_image(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot
    images_name = ['img1.jfif', 'img2.jfif', 'img3.jfif', 'img4.jfif', 'img5.jfif',
                   'img6.jfif', 'img7.jfif', 'img8.jfif', 'img9.jfif', 'img10.jfif',]
    random_img = random.choice(images_name)
    bot.send_photo(chat_id=chat_id, photo=open(f'C:\\Users\\baraa.56\\Desktop\\TelegramBot\\Bot_imgs\\{random_img}', 'rb'))
    update.message.reply_text("😎😎😎😎😎")


def get_and_download_image(update: Update, context: CallbackContext):
    """ some images have (3) levels of quality, some images have (2) levels """
    lvl = 'normal'
    if lvl == 'tiny':
        quality = 0
    if lvl == 'small':
        quality = 1
    if lvl == 'normal':
        quality = 2
    else:  # big
        quality = 3
    quality = -1  # high quality

    message_id = update.message.message_id
    file_id = update.message.photo[quality].file_id
    bot = context.bot
    file = bot.getFile(file_id)
    print("file_id: " + str(file_id))
    img_path = f'C:\\Users\\baraa.56\\Desktop\\TelegramBot\\user_photos\\img_message{message_id}.jpg'
    file.download(img_path)

    update.message.reply_text(f"Download photo Successfully👍")
    update.message.reply_text(f"Save in Local Server :\n({img_path})")


def image_to_pdf(update: Update, context: CallbackContext):
    message_id = update.message.message_id

    # download image
    quality = -1  # high quality
    file_id = update.message.photo[quality].file_id
    bot = context.bot
    file = bot.getFile(file_id)
    img_path = f'C:\\Users\\baraa.56\\Desktop\\TelegramBot\\user_photos\\img{message_id}.jpg'
    file.download(img_path)

    # convert image to pdf
    img_open = Image.open(f'{img_path}')
    img_rgb = img_open.convert('RGB')
    img_rgb.save(f'C:\\Users\\baraa.56\\Desktop\\TelegramBot\\user_photos\\file{message_id}.pdf')


def get_and_download_voice(update: Update, context: CallbackContext):
    message_id = update.message.message_id

    file_id = update.message.voice.file_id
    bot = context.bot
    file = bot.getFile(file_id)
    voice_path = f'C:\\Users\\baraa.56\\Desktop\\TelegramBot\\user_photos\\voice{message_id}.mp3'
    file.download(voice_path)

    update.message.reply_text(f"Download voice Successfully👍")
    update.message.reply_text(f"Save in Local Server :\n({voice_path})")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry I can't recognize your #text '{update.message.text}'")


def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry '{update.message.text}' is not a valid #command.\nwrite /help to see the commands available.")


def main():
    """Start the bot."""
    print('__here__')
    # Create the Updater and pass it your bot's token.
    updater = Updater("5013210105:AAHnsnoEsm7OYENZw9WniG74Bfm5g2Ii58s", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('basic', basic_bot))

    # __________________________________________________________________________________________________________________

    # ___(1)___
    # dp.add_handler(CommandHandler('facebook', facebook_url))

    # ___(2)___
    # dp.add_handler(CommandHandler('StartGoogleTranslator', start_google_translator))
    # dp.add_handler(MessageHandler(Filters.text, google_translator))

    # ___(3)___
    # dp.add_handler(CommandHandler('StartConversation', start_conversation))
    # dp.add_handler(MessageHandler(Filters.text, conversation))

    # ___(4)___
    # dp.add_handler(CommandHandler('info', user_information))

    # ___(5)___
    dp.add_handler(CommandHandler('img', send_image))

    # __________________________________________________________________________________________________________________

    # ___(END)___
    dp.add_handler(MessageHandler(Filters.command, unknown_command))
    # dp.add_handler(MessageHandler(Filters.text, unknown_text))

    dp.add_handler(MessageHandler(Filters.text, google_translator))

    # ___(6)___
    dp.add_handler(MessageHandler(Filters.photo, get_and_download_image))

    # # ___(7)___
    # dp.add_handler(MessageHandler(Filters.photo, image_to_pdf))

    # ___(8)___
    dp.add_handler(MessageHandler(Filters.voice, get_and_download_voice))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
