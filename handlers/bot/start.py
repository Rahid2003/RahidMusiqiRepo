# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 | 
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**Salam๐ {}\n\nMษn {} \n\nSษsli sรถhbษtlษrdษ musiqi oxuya bilษn bir botam\n\nMษni qrupunuza ษlavษ edin sonra admin edษrษk musiqi dinlษyษ bilษrsiniz๐ฅฐ**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="โMษni qrupuna ษlavษ etโ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim ๐๐ป", url=f"https://t.me/Rahid_2003"),
                    InlineKeyboardButton(text="Digษr Botlar", url="https://t.me/Rahid_44"),
                ],                
                [                    
                    InlineKeyboardButton(text="Kanalฤฑm ๐โค๏ธ", url="https://t.me/qruzdaa")
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """Salam๐ {}\nKรถmษk  \nqrupuna ษlavษ edษrษk musiqi dinlษyษ bilษrsiniz @{} Sualฤฑnฤฑz nษdir? """
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="๐น๏ธ Tษmษl ษmrlษri", callback_data="basic_"),
            InlineKeyboardButton(text="๐น๏ธ Admin ษmrlษri", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="๐ Baฤla", callback_data="close_"),
            InlineKeyboardButton(text="โฌ๏ธ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Salam burada yardฤฑm menyusu istษdiyiniz seรงimi seรงin vษ araลdฤฑrฤฑn \nฤฐstษnilษn kรถmษk vษ ya problem รผรงรผn qoลulun @{SUPPORT_GROUP} Sualฤฑnฤฑz nษdir?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="๐น๏ธ Tษmษl ษmrlษri", callback_data="bcd"),
                InlineKeyboardButton(text="๐น๏ธ Admin ษmrlษri", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="๐ Baฤla", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Salam, Mษn {BOT_NAME} \nBu sadษ vษ gecikmษsiz bir botdur\nProblem olanda qoลulun ๐ @{SUPPORT_GROUP}\nvษ ya /help basฤฑn"""
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="๐ Support", url=f"https://t.me/Rahid_Support"),
                    InlineKeyboardButton(text="Mษni qrupa ษlavษ et โ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim ๐๐ป", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sahibim ๐๐ป", url="https://t.me/Rahid_2003"),
                ],                
                [                    
                    InlineKeyboardButton(text="ฦmrlษr ๐น๏ธ", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`ฦsas ษmrlษr:- `

/play (Sorฤu, YouTube linki, audio fayl) - bu ษmrdษn istifadษ edin vษ musiqidษn hษzz alฤฑn
/ytp (Sorgu) - Daha tษkmil musiqi axtarmaq รผรงรผn istifadษ edin
/song (Sorgu) - Bu ษmrlษ sevimli mahnฤฑlarฤฑnฤฑzฤฑ yรผklษyษ bilษrsiniz
/ara (Sorgu) - YouTube-da axtarmaq
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="๐ Baฤla", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin ษmrlษr:-`

/durdur - Musiqinin ifasฤฑnฤฑ dayandฤฑrฤฑr
/devam - Dayandฤฑrฤฑlmฤฑล musiqini davam etdirir
/skip - Nรถvbษti mahnฤฑya keรงir
/end - Mahnฤฑnฤฑ bitir
/katil - Qrupa kรถmษkรงi ษlavษ edin


`Sudo ษmrlษr:-`

/rmf - Faylฤฑ verilษnlษr bazasฤฑndan tษmizlษyir
/rmw - Data fayllarฤฑ verilษnlษr bazasฤฑndan tษmizlษyir
/clean - Fayllarฤฑ serverdษn tษmizlษyir
/gcast - Qlobal mesaj yayฤฑmlamaq
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="๐ Baฤla", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
