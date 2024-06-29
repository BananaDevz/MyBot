from api.shineMainApi import get_bot_instance
from googletrans import Translator
from handlers.mainHandlers import user_languages 
from handlers.languageHandlers import user_languages
import json
import telebot 

bot = get_bot_instance()  
translator = Translator()

@bot.message_handler(commands=['kick'])
def kick_user(message):
    try:
        chat_id = message.chat.id
        bot_id = bot.get_me().id
        user_id = message.from_user.id

        # Obter a lista de administradores
        administrators = bot.get_chat_administrators(chat_id)
        bot_is_admin = any(admin.user.id == bot_id for admin in administrators)
        user_is_admin = any(admin.user.id == user_id for admin in administrators)

        if not (bot_is_admin and user_is_admin):
            response = f"Você ou o bot não possuem permissões de administrador."
            language = user_languages.get(message.from_user.id, 'pt')
            translated_response = translator.translate(response, dest=language).text
            bot.reply_to(message, translated_response)
            return

        user_to_kick = None

        if message.reply_to_message:
            user_to_kick = message.reply_to_message.from_user
        elif message.entities:
            for entity in message.entities:
                if entity.type == 'mention':
                    username = message.text[entity.offset + 1:entity.offset + entity.length]  # +1 para remover o '@'
                    user_to_kick = bot.get_chat_member(chat_id, username).user
                    break

        if user_to_kick:
            bot.kick_chat_member(chat_id, user_to_kick.id)
            bot.reply_to(message, f"{user_to_kick.first_name} foi expulso do grupo.")
        else:
            bot.reply_to(message, "Responda à mensagem do usuário que você deseja expulsar ou mencione o usuário com @.")
    except Exception as e:
        bot.reply_to(message, f"Ocorreu um erro: {str(e)}")
