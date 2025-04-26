import random
from telegram import Update, InputFile
from telegram.ext import ContextTypes
import os

# Упрощенные трактовки карт
tarot_meanings = {
    "0_the_fool": "Шут — новые начинания, свобода, приключение.",
    "1_the_magician": "Маг — сила воли, мастерство, воплощение мечт.",
    "2_the_high_priestess": "Верховная Жрица — тайны, интуиция, мудрость.",
    "3_the_empress": "Императрица — плодородие, изобилие, забота.",
    "4_the_emperor": "Император — власть, структура, защита.",
    # ... дополним позже полный список трактовок
}

async def tarot_reading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card_code = random.choice(list(tarot_meanings.keys()))
    card_text = tarot_meanings[card_code]
    card_image_path = f"tarot_cards/images/{card_code}.jpg"

    if os.path.exists(card_image_path):
        with open(card_image_path, "rb") as img:
            await update.message.reply_photo(photo=InputFile(img))
    else:
        await update.message.reply_text("🃏 Карта найдена, но изображение отсутствует.")

    await update.message.reply_text(f"🔮 Значение карты:\n\n{card_text}")
# tarot handler
