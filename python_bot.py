import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog_flow import detect_intent_texts


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('АААААААААА ПОМОГИТЕЕ!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    response = detect_intent_texts(project_id, update.effective_chat.id, [update.message.text], "ru")
    update.message.reply_text(response.fulfillment_text)


def main() -> None:
    """Start the bot."""
    updater = Updater(tg_token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    """Enable logging"""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logger = logging.getLogger(__name__)

    """Get environment variables"""
    env = Env()
    env.read_env()
    tg_token = env("TG_TOKEN")
    project_id = env("PROJECT_ID")

    main()
