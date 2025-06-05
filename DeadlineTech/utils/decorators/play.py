# Powered by DeadlineTech

import asyncio
import logging
import traceback

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DeadlineTech import YouTube, app
from DeadlineTech.misc import SUDOERS
from DeadlineTech.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from DeadlineTech.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

links = {}

def PlayWrapper(command):
    async def wrapper(client, message):
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if message.sender_chat:
                upl = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="AnonymousAdmin")]]
                )
                return await message.reply_text(_["general_3"], reply_markup=upl)

            if await is_maintenance() is False and message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a>.",
                    disable_web_page_preview=True,
                )

            try:
                await message.delete()
            except Exception as e:
                logger.warning(f"Failed to delete message: {e}")

            audio_telegram = (
                (message.reply_to_message.audio or message.reply_to_message.voice)
                if message.reply_to_message else None
            )
            video_telegram = (
                (message.reply_to_message.video or message.reply_to_message.document)
                if message.reply_to_message else None
            )
            url = await YouTube.url(message)

            if not audio_telegram and not video_telegram and not url:
                if len(message.command) < 2:
                    if "stream" in message.command:
                        return await message.reply_text(_["str_1"])
                    return await message.reply_photo(
                        photo=PLAYLIST_IMG_URL,
                        caption=_["play_18"],
                        reply_markup=InlineKeyboardMarkup(botplaylist_markup(_)),
                    )

            if message.command[0][0] == "c":
                chat_id = await get_cmode(message.chat.id)
                if not chat_id:
                    return await message.reply_text(_["setting_7"])
                try:
                    chat = await app.get_chat(chat_id)
                    channel = chat.title
                except Exception as e:
                    logger.error(f"get_chat failed: {e}")
                    return await message.reply_text(_["cplay_4"])
            else:
                chat_id = message.chat.id
                channel = None

            playmode = await get_playmode(message.chat.id)
            playty = await get_playtype(message.chat.id)
            if playty != "Everyone" and message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_13"])
                if message.from_user.id not in admins:
                    return await message.reply_text(_["play_4"])

            video = (
                True if message.command[0][0] == "v" or "-v" in message.text
                else (True if message.command[0][1] == "v" else None)
            )
            fplay = True if message.command[0][-1] == "e" else None

            if not await is_active_chat(chat_id):
                userbot = await get_assistant(chat_id)
                try:
                    get = await app.get_chat_member(chat_id, userbot.id)
                    if get.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
                        return await message.reply_text(
                            _["call_2"].format(app.mention, userbot.id, userbot.name, userbot.username)
                        )
                except UserNotParticipant:
                    logger.info("Assistant not in chat, generating invite...")
                    invitelink = links.get(chat_id)
                    if not invitelink:
                        if message.chat.username:
                            invitelink = message.chat.username
                            try:
                                await userbot.resolve_peer(invitelink)
                            except Exception as e:
                                logger.warning(f"resolve_peer failed: {e}")
                        else:
                            try:
                                invitelink = await app.export_chat_invite_link(chat_id)
                            except ChatAdminRequired:
                                return await message.reply_text(_["call_1"])
                            except Exception as e:
                                logger.error(f"export_chat_invite_link failed: {e}")
                                return await message.reply_text(
                                    _["call_3"].format(app.mention, type(e).__name__)
                                )

                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")

                    myu = await message.reply_text(_["call_4"].format(app.mention))
                    try:
                        await asyncio.sleep(1)
                        await userbot.join_chat(invitelink)
                    except InviteRequestSent:
                        try:
                            await app.approve_chat_join_request(chat_id, userbot.id)
                        except Exception as e:
                            return await message.reply_text(
                                _["call_3"].format(app.mention, type(e).__name__)
                            )
                        await asyncio.sleep(3)
                        await myu.edit(_["call_5"].format(app.mention))
                    except UserAlreadyParticipant:
                        pass
                    except Exception as e:
                        logger.error(f"userbot.join_chat failed: {traceback.format_exc()}")
                        return await message.reply_text(
                            _["call_3"].format(app.mention, type(e).__name__)
                        )

                    links[chat_id] = invitelink
                    try:
                        await userbot.resolve_peer(chat_id)
                    except Exception as e:
                        logger.warning(f"userbot.resolve_peer after join failed: {e}")

            logger.info(
                f"▶️ Play Command Triggered in {message.chat.title} [{chat_id}] by {message.from_user.first_name} [{message.from_user.id}]"
            )

            return await command(
                client,
                message,
                _,
                chat_id,
                video,
                channel,
                playmode,
                url,
                fplay,
            )

        except Exception as ex:
            logger.exception(f"Unhandled error in PlayWrapper: {ex}")
            try:
                await message.reply_text(
                    "🚫 <b>Unexpected Error:</b>\n<code>{}</code>".format(str(ex)),
                    disable_web_page_preview=True,
                )
            except:
                pass

    return wrapper
