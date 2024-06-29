import json
import os
from googletrans import Translator
from api.shineMainApi import get_bot_instance
from .languageHandlers import user_languages  # Adicione o ponto aqui

translator = Translator()
bot = get_bot_instance()

'''
@bot.message_handler(commands=['github'])
def send_github_link(message):
    github_url = "https://github.com/ShineKunBot/MyBot"
    response = f"Access the project repository on GitHub: {github_url}"
    language = user_languages.get(message.from_user.id, 'pt')
    translated_response = translator.translate(response, dest=language).text
    bot.reply_to(message, translated_response)

@bot.message_handler(commands=['start', 'help'])
def respostaPadrao(message):
    texto = """
Hello, I'm Shine Kun bot! How are you? Choose one of the options for what you need:
/markov generates a random response based on the messages it was trained on.
/github sends the link to our project.
/setlang [language code] sets the preferred language.
    """
    bot.reply_to(message, texto)
    '''

@bot.message_handler(func= lambda message: True)
def analisy(msg):
    switch msg.text:
        case "/github":
            bot.reply_to(msg, "https://github.com/ShineKunBot/MyBot")
        case "/kick", "/ban":
            if  bot.get_chat_administrators(chat_id):
                bot.reply_to(msg, "Voce não possui a permissão de administrador")
            
        case _:
            bot.reply_to(msg, "text")





