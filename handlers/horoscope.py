import random
from telegram import Update
from telegram.ext import ContextTypes

daily_energies = [
    "Сегодня благоприятный день для новых начинаний.",
    "Слушай своё сердце — оно подскажет верный путь.",
    "Остерегайся поспешных решений.",
    "Ожидай приятные сюрпризы от судьбы.",
    "Энергия дня благоволит любви и гармонии."
]

async def horoscope_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(daily_energies)
    await update.message.reply_text(f"🌟 Ваш гороскоп на сегодня:\n\n{message}")
# horoscope handler
