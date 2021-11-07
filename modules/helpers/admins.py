from typing import List
from pyrogram.types import Chat, User
from modules.cache.admins import get as gett
from modules.cache.admins import set


async def get_administrators(chat: Chat) -> List[User]:
    get = gett(chat.id)

    if get:
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [administrator.user.id for administrator in administrators]

    set(chat.id, to_set)
    return await get_administrators(chat)
