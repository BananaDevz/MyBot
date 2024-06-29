import json
import os
from googletrans import Translator
from api.shineMainApi import get_bot_instance
from .languageHandlers import user_languages  # Adicione o ponto aqui

translator = Translator()
bot = get_bot_instance()

'''

SERA FEITA ALGUMAS ALTERAÇÕES, VEJA SE GOSTA...

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

# OPÇÃO 1

@bot.message_handler(func= lambda, message: True)
def analise(msg):
    if len(msg.text()) >= 1:
        bot.reply_to(msg, "Hello, I am ShineKumBot, I'm here to help you with whatever you need!")
    if github in msg.text():
        bot.reply_to(msg, "https://github.com/ShineKunBot/MyBot")

# OPÇÃO 2

@bot.message_handler(func= lambda, message: True)
def analise(msg):
    match msg.text():
        case "github":
            bot.reply_to(msg, "https://github.com/ShineKunBot/MyBot")
        case _:
            bot.reply_to(msg, "Hello, I am ShineKumBot, I'm here to help you with whatever you need!")

# seu criterio
