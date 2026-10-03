#!/usr/bin/env python3
"""
Точка входа бота.

Регистрируем обработчики команд и запускаем polling.
Polling — это когда бот постоянно спрашивает Telegram: 
"есть ли для меня сообщения?". Для маленьких ботов это нормально,
для больших лучше webhook (но это сложнее).
"""
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from handlers import start_handler, help_handler, about_handler, echo_handler

# Логирование — чтобы видеть ошибки и что происходит
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Стартую бота...")
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Команды
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("about", about_handler))
    
    # Эхо на текст (все сообщения кроме команд)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    
    logger.info("Бот запущен. Ctrl+C для остановки.")
    application.run_polling()


if __name__ == "__main__":
    main()
