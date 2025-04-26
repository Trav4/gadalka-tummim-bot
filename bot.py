from telegram.ext import Application, CommandHandler
from handlers.start import start
from handlers.tarot import tarot_reading
from handlers.horoscope import horoscope_today
from handlers.advice import daily_advice
import os

# Загружаем токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    # Создаем приложение Telegram
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем команды
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('tarot', tarot_reading))
    application.add_handler(CommandHandler('horoscope', horoscope_today))
    application.add_handler(CommandHandler('advice', daily_advice))

    # Запускаем бота
    print("✅ Gadalka TUMMIM is alive and listening for prophecies...")
    application.run_polling()

if __name__ == "__main__":
    main()
# Основной бот-код
