import asyncio
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('пiщов нахуй')


async def main() -> None:
    application = ApplicationBuilder().token('7804030886:AAFmqYAPW08gRlS6N6ASwqp5GXNPyifcS64').build()

    application.add_handler(CommandHandler('spam', spam))

    await application.initialize()
    await application.start()
    await application.updater.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
