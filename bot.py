from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(update, context):
    update.message.reply_text("Здравствуй, {} Жопка {}. Нюдсы мои ждешь?!".format(update.message.chat.first_name, update.message.chat.last_name))
    logging.info("Ползователь {} нажал на /start".format(update.message.chat.first_name))


def chat_me(update, context):
    text = update.message.text
    update.message.reply_text(text)
    logging.info(text)

def main():
    upd = Updater(settings.TELEGRAM_API_KEY)

    upd.dispatcher.add_handler(CommandHandler('start', start_bot))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat_me))

    upd.start_polling()
    upd.idle()




if __name__ == "__main__":
    logging.info("bot started")
    main()
     