import telebot
from api.shineMainApi import get_bot_instance
import handlers.mainHandlers
import handlers.markovHandlers
import handlers.languageHandlers


bot = get_bot_instance()  

if __name__ == "__main__":
    bot.polling(none_stop=True)
