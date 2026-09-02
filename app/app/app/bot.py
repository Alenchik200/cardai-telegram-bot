import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from ai import generate_text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n"
        "Я AI-бот для создания карточек товаров.\n\n"
        "Отправь мне описание товара."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        result = generate_text(text)
        await update.message.reply_text(result)
    except Exception as e:
    import traceback
    traceback.print_exc()
    await update.message.reply_text(
        "Произошла ошибка при обращении к AI. Попробуйте ещё раз."
    )


def main():
    raw_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    token = "".join(c for c in raw_token if c.isascii() and c.isprintable())

    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN не установлен")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
