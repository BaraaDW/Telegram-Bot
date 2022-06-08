
import logging

from telegram.ext import (Updater, CommandHandler, PollAnswerHandler, PollHandler, MessageHandler, Filters)


logger = logging.getLogger('--TEST--')


def start(update, context):
    """Inform user about what this bot can do"""
    update.message.reply_text('Please select /quiz to get a Quiz.')


def poll(update, context):
    """Sends a predefined poll"""
    questions = ["Good", "Really good", "Fantastic", "Great"]
    message = context.bot.send_poll(update.effective_user.id, "How are you?", questions, is_anonymous=False, allows_multiple_answers=True)
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {message.poll.id: {"questions": questions}}
    context.bot_data.update(payload)
    print(f'payload is {payload}')


def receive_poll_answer(update, context):
    """Summarize a users poll vote"""
    answer = update.poll_answer
    poll_id = answer.poll_id
    questions = context.bot_data[poll_id]["questions"]

    selected_options = answer.option_ids
    answer_string = ""
    for question_id in selected_options:
        if question_id != selected_options[-1]:
            answer_string += questions[question_id] + " and "
        else:
            answer_string += questions[question_id]
    user_mention = update.effective_user.full_name
    state = f"{user_mention} choose : {answer_string}!"
    print(state)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5013210105:AAHnsnoEsm7OYENZw9WniG74Bfm5g2Ii58s", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('quiz', poll))
    dp.add_handler(PollAnswerHandler(receive_poll_answer))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()