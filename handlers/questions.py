from telegram import Update
from telegram.ext import ContextTypes

# Память пользователей (ID: количество вопросов)
user_questions = {}

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    count = user_questions.get(user_id, 0)

    if count >= 3:
        await update.message.reply_text(
            "🔒 Ты использовал все 3 бесплатных вопроса.\n"
            "Чтобы получить неограниченные ответы, оформи подписку."
        )
    else:
        user_questions[user_id] = count + 1
        await update.message.reply_text(
            "🔮 Я чувствую твой запрос... Мудрость грядет к тебе.\n"
            "Пожалуйста, используй команды:\n"
            "/tarot — расклад\n"
            "/horoscope — гороскоп\n"
            "/advice — совет"
        )
