import random
from telegram import Update
from telegram.ext import ContextTypes

daily_advices = [
    "Помни: после темной ночи всегда восходит солнце.",
    "Слушай свою интуицию — она твой верный советник.",
    "Будь благодарен за то, что имеешь — и получишь больше.",
    "Не бойся перемен, они несут новые возможности.",
    "Сегодня важно проявить терпение и мудрость."
]

async def daily_advice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    advice = random.choice(daily_advices)
    await update.message.reply_text(f"🧿 Совет дня:\n\n{advice}")
# advice handler
