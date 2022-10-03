from functools import partial
import logging

from environs import Env
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialog_flow import detect_intent_texts

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def reply_message(project_id, update: Update, context: CallbackContext) -> None:
    """Reply user message"""
    answer = detect_intent_texts(project_id, update.effective_chat.id, update.message.text, "ru")
    update.message.reply_text(answer.fulfillment_text)


def main() -> None:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    """Get environment variables"""
    env = Env()
    env.read_env()
    tg_token = env("TG_TOKEN")
    project_id = env("PROJECT_ID")

    """Start the bot."""
    updater = Updater(tg_token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, partial(reply_message, project_id)))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
