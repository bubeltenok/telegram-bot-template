# telegram-bot-template

Шаблон Telegram-бота, который я собрал когда разбирался с python-telegram-bot. 

Ничего сверхъестественного — просто структура, чтобы не писать всё с нуля каждый раз. Команды /start, /help, эхо-ответы, логирование. Можно брать и допиливать под себя.

## Как запустить

```bash
# 1. Зависимости
pip install -r requirements.txt

# 2. Создай .env и вставь токен от @BotFather
cp .env.example .env
# открой .env и замени your_bot_token_here на настоящий токен

# 3. Запуск
python bot.py
```

## Как получить токен

1. Пиши [@BotFather](https://t.me/BotFather) в Telegram
2. Отправь `/newbot`
3. Придумай имя и username для бота
4. БотFather выдаст токен вида `123456789:ABCdef...` — скопируй в `.env`

## Структура

```
telegram-bot-template/
├── bot.py              # точка входа, регистрирует обработчики
├── config.py           # читает токен из .env
├── handlers/           # обработчики команд
│   ├── start.py        # /start, /help, /about
│   └── echo.py         # ответ на любой текст
├── requirements.txt
└── .env.example        # шаблон для .env
```

Почему handlers в отдельной папке: удобно, когда бот растёт. Каждая команда — свой файл, не превращаем bot.py в помойку.

## Что умеет из коробки

- `/start` — приветствие
- `/help` — список команд
- `/about` — информация о боте
- Любой текст — эхо-ответ

## Как добавить свою команду

1. Создай файл в `handlers/`, например `weather.py`
2. Напиши функцию-обработчик:

```python
from telegram import Update
from telegram.ext import ContextTypes

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Погода сегодня отличная!")
```

3. Зарегистрируй в `bot.py`:

```python
from handlers.weather import weather_handler
application.add_handler(CommandHandler("weather", weather_handler))
```

4. Перезапусти бота

## Почему python-telegram-bot v20+

С версии 20 библиотека перешла на асинхронность (async/await). Это значит бот может обрабатывать несколько сообщений одновременно, не блокируясь. Для простого бота разницы не заметишь, но если планируешь что-то серьёзное — пригодится.

## Проблемы

- Бот не отвечает — проверь токен, возможно случайно опубликовал его в открытом репозитории и BotFather отозвал
- `ModuleNotFoundError` — `pip install -r requirements.txt` забыл

MIT, используй как хочешь.
