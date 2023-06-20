import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from aiogram.utils import markdown
from aiogram.types import (Message, BotCommand,
                           BotCommandScopeAllPrivateChats)

from .texts import Text
from .handlers import to_json
from ..bot.filters import IsPrivate
from ..bot.misc import rate_limit, delete_message, edit_message


@rate_limit(2)
async def command_start(message: Message):
    emoji = await message.answer("👋")
    await delete_message(message)
    await asyncio.sleep(2)

    user_link = markdown.hlink(
        title=message.from_user.first_name,
        url=message.from_user.url
    )
    text = Text(message.from_user.language_code).get("start")
    await edit_message(emoji, text.format(user_link))
    await message.answer(to_json(dict(message)))

@rate_limit(2)
async def command_source(message: Message):
    emoji = await message.answer("👨‍💻")
    await delete_message(message)
    await asyncio.sleep(2)

    text = Text(message.from_user.language_code).get("source")
    await edit_message(emoji, text)


async def setup(bot: Bot):
    commands = {
        "en": [
            BotCommand("start", "Restart"),
            BotCommand("source", "Source code"),
        ],
        "ru": [
            BotCommand("start", "Перезапустить"),
            BotCommand("source", "Исходный код"),
        ]
    }

    await bot.set_my_commands(
        commands=commands["ru"],
        scope=BotCommandScopeAllPrivateChats(),
        language_code="ru"
    )
    await bot.set_my_commands(
        commands=commands["en"],
        scope=BotCommandScopeAllPrivateChats(),
    )


def register(dp: Dispatcher):
    dp.register_message_handler(
        command_start, CommandStart(), IsPrivate()
    )
    dp.register_message_handler(
        command_source, IsPrivate(), commands="source"
    )
