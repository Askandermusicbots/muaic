import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/11cbf59181715ef67624f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━
💖¦انا بوت تشغيل وتنزيل الاغاني والفديو 
💖¦اضفني مشرف في مجموعتك لأعمل
💖¦اتبع مايلي لمعرفه كيفيه الاستخدام
💖¦اضغط علي ذر الاوامر
💖مميزات الروبوت يعمل بجودة فائقه
مطوري [ELLIOT](https://t.me/DAD_A_S_K_A_N_D_E_R)...
━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ اضفني الي مجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📝 الاومر", url="https://te.legra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-06-26"),
            InlineKeyboardButton("⚕️ المطور", url="https://t.me/DAD_A_S_K_A_N_D_E_R")
        ],
        [
            InlineKeyboardButton("👥 جروب الدعم", url="https://t.me/SOURCELORD"),
            InlineKeyboardButton("📣 قناة السورس", url="https://t.me/SOURCE_LORD")
        ],
        [
            InlineKeyboardButton("💠 سورس لورد 💠", url="https://t.me/SOURCE_LORD")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "Sumit", "تنصيب"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/3752041b671e0afc6ada2.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="👥 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/SOURCELORD"),
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/SOURCE_LORD"),
            ]
        ]
     ),
  ) 


@Client.on_message(commandpro(["/updates", "Channel", "/openbaby"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e866cd93108978ef6faef.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "انضم لقناة سورس لورد", url=f"https://t.me/SOURCE_LORD")
                ]
            ]
        ),
    )
