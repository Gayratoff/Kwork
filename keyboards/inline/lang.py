from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

laguage =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="๐ฌ๐ง English", callback_data="en"),
        InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha", callback_data="uz"),

    ]
]
)

laguageuz =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="๐ฌ๐ง English", callback_data="en"),
        InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน", callback_data="ru"),

    ],
    [
        InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha โ", callback_data="uz"),
    ]
]
)

laguageen =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="๐ฌ๐ง English โ", callback_data="en"),
        InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha", callback_data="uz"),
    ]
]
)

laguageru =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="๐ฌ๐ง English", callback_data="en"),
        InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน โ", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha", callback_data="uz"),
    ]
]
)
