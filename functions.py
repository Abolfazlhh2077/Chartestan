from pyrogram import *
from pyrogram.types import *


def bot_services(client: Client, message: Message):
    message.reply_text(text="به ربات ما خوش آمدید، چه کاری میتوانیم برایتان انجام دهیم؟", reply_markup=InlineKeyboardMarkup([
                                   [InlineKeyboardButton(text="درخواست تحلیل سهم", callback_data="analysisReq")],
                                   [InlineKeyboardButton(text="ارتباط با پشتیبانی", callback_data="contactSupport")],
                                   [InlineKeyboardButton(text="درخواست کلاس رفع اشکال", callback_data="coachingclsReq")]
                                ])
                        )
    

