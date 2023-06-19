import json

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hcode

from .filters import IsPrivate, IsGroup
from .misc import rate_limit


def to_json(value: dict) -> str:
    return json.dumps(
        value,
        indent=2,
        sort_keys=True,
        ensure_ascii=False
    )


@rate_limit(1)
async def message_to_json(message: Message):
    message_dict = dict(message)
    message_json = to_json(message_dict)

    if len(message_json) <= 4096:
        await message.reply(hcode(message_json))
    else:
        await message.reply_document(
            document=message_json.encode('utf8')
        )


def register(dp: Dispatcher):
    dp.register_message_handler(
        message_to_json, IsPrivate() | IsGroup(),
        content_types="any"
    )
