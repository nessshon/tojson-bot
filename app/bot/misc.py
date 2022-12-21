from contextlib import suppress

from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.utils.exceptions import (MessageCantBeEdited, MessageToEditNotFound,
                                      MessageCantBeDeleted, MessageToDeleteNotFound)


async def edit_message(message: Message, text: str,
                       reply_markup: InlineKeyboardMarkup | None = None,
                       disable_web_page_preview: bool = False) -> Message:
    with suppress(MessageCantBeEdited, MessageToEditNotFound):
        return await message.edit_text(
            text, reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview
        )


async def delete_message(message: Message) -> None:
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


def rate_limit(limit: float, key=None):
    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)

        return func

    return decorator
