import os
import json
from googletrans import Translator
from api.shineMainApi import get_bot_instance

translator = Translator()
user_languages = {}
bot = get_bot_instance()

# Path to the JSON file that will store users' languages
user_languages_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_languages.json')

# Function to load users' languages ​​from JSON file
def load_user_languages():
    global user_languages
    if os.path.exists(user_languages_file):
        with open(user_languages_file, 'r', encoding='utf-8') as file:
            user_languages = json.load(file)

# Função para salvar os idiomas dos usuários no arquivo JSON
def save_user_languages():
    with open(user_languages_file, 'w', encoding='utf-8') as file:
        json.dump(user_languages, file)

# Carrega os idiomas dos usuários ao iniciar
load_user_languages()

@bot.message_handler(commands=['setlang'])
def set_language(message):
    try:
        language = message.text.split()[1]
        user_languages[message.from_user.id] = language
        save_user_languages()
        bot.reply_to(message, f"Language defined for {language}")
    except IndexError:
        bot.reply_to(message, "Please provide a valid language code. Example: /setlang en")
