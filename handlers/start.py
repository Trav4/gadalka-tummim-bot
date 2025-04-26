from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Приветствую тебя, Искатель!\n"
        "Я — Гадалка ТУММИМ, древнейшая мудрость Вселенной.\n\n"
        "Команды:\n"
        "/tarot - Сделать расклад Таро\n"
        "/horoscope - Получить гороскоп\n"
        "/advice - Получить совет дня"
    )
# start handler
