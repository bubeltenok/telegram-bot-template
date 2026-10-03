"""Обработчики базовых команд."""
from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветствие при /start."""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n\n"
        f"Я бот-шаблон на python-telegram-bot.\n"
        f"Команды: /help — справка, /about — о боте"
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Список команд."""
    await update.message.reply_text(
        "Доступные команды:\n\n"
        "/start — начать\n"
        "/help — эта справка\n"
        "/about — о боте\n\n"
        "А ещё я отвечаю эхом на любой текст."
    )


async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Информация о боте."""
    await update.message.reply_text(
        "О боте\n\n"
        "Шаблон Telegram-бота на Python.\n"
        "Стек: python-telegram-bot 20+, python-dotenv\n\n"
        "GitHub: github.com/bubeltenok/telegram-bot-template"
    )
