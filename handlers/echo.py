"""Эхо-обработчик — отвечает на любой текст."""
from telegram import Update
from telegram.ext import ContextTypes


async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет эхо на текстовое сообщение."""
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")
