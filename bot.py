from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن ربات شما
TOKEN = '7277553648:AAGpWMoCSGw1M7-vd7rC0K7SXrctq20BnnI'

# آیدی کانال شما
CHANNEL_ID = '@devil_team_hack'

# آیدی پیام در کانال
MESSAGE_ID = 73  # شماره پیام مورد نظر در کانال

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    # فوروارد کردن پیام از کانال به کاربر
    context.bot.forward_message(chat_id=chat_id, from_chat_id=CHANNEL_ID, message_id=MESSAGE_ID)

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # ثبت دستور /start
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()