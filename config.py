"""Конфигурация бота.

Токен храним в .env, чтобы не светить его в коде.
Если запушишь токен на GitHub — BotFather отзовёт его автоматически
(да, я узнал это на собственном опыте).
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Создай файл .env и добавь туда токен от @BotFather.")
