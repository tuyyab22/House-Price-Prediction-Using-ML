import  constants as key
from telegram.ext import *
import responses as r

print("Bot as started!!")

def start_command(update,context):
    update.message.reply_text('click 1 to search!!!')



def handle_message(update,context):
    text=str(update.message.text).lower()
    responses=r.sample_responses(text)

    update.message.reply_text(responses)


def main():
    updater=Updater(key.API_KEY,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling()
    updater.idle()

main()

