import os
from dotenv import *
from pyrogram import *
from pyrogram.types import *
from database import *
from functions import *
import sqlite3


load_dotenv("config.env")
bot_name = os.getenv("bot_name")
bot_username = os.getenv("bot_username")
bot_token = os.getenv("bot_token")
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

user_state = {}
user_fullname_signup = {}



app = Client(name=bot_name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))
def start_handler(client: Client, message: Message):
    if check_userid_exists(str(message.from_user.id)):
        user_state[message.from_user.id] = "loggedin"
        bot_services(client=client, message=message)
    else:
        message.reply_text(text="شما در پنل کاربری ما حسابی ندارید. برای استفاده از آن یک پروفایل کاربری درست کنید.",
                           reply_markup=InlineKeyboardMarkup(
                               [[InlineKeyboardButton(text="ساخت پروفایل کاربری", callback_data="signup")]])
                           )


@app.on_message(filters.text)
def message_handler(client: Client, message: Message):
    if user_state[message.from_user.id] == "nameInput":
        user_fullname_signup[message.from_user.id] = message.text
        user_state[message.from_user.id] = "phonenumberInput"
        message.reply_text("شماره ی تلفن خود را وارد کنید.")
    elif user_state[message.from_user.id] == "phonenumberInput":
        if len(message.text) == 11 and message.text.startswith('09') and message.text.isdigit():
            userid = message.from_user.id
            sign_up_user(user_fullname_signup[userid],message.text, userid)
            user_state[message.from_user.id] = "loggedin"
            message.reply_text("پروفایل کاربری شما با موفقیت ثبت شد.")
            bot_services(client=client, message=message)
        else:
            message.reply_text("شماره ی تلفن خود را به نادرستی وارد کرده اید، لطفا آن را به درستی وارد کنید!")
    elif user_state[message.from_user.id] == "contactingSupport":
        register_message_to_support(userid=message.from_user.id, messageText=message.text)
        message.reply_text(text="پیام شما با موفقیت ثبت و به پشتیبانی ارسال شد.")
        user_state[message.from_user.id] = "loggedin"


@app.on_callback_query()
def callback_handler(client: Client, callback: CallbackQuery):
    if callback.data == "signup":
        user_state[callback.from_user.id] = 'nameInput'
        callback.message.reply_text("نام و نام خانوادگی خود را وارد کنید.")
    elif callback.data == "contactSupport":
        user_state[callback.from_user.id] = "contactingSupport"
        print(callback.from_user.id)
        callback.message.reply_text(text="لطفا پرسش خود از پشتیبانی را در قالب یک پیام بنویسید.")




app.run()