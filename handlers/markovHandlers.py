import os
from api.shineMainApi import get_bot_instance
from markovchain.MarkovC import generateResponse
from googletrans import Translator
from handlers.mainHandlers import user_languages  

bot = get_bot_instance()
translator = Translator()

messages_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mensagens.txt')

@bot.message_handler(commands=['markov'])
def markovResposta(message):
    question = message.text
    response = generateResponse(question)
    if response:
        language = user_languages.get(message.from_user.id, 'pt')
        translated_response = translator.translate(response, dest=language).text
        bot.reply_to(message, translated_response)
    else:
        bot.reply_to(message, "Não consegui gerar uma resposta. Tente novamente.")

@bot.message_handler(func=lambda message: True)
def save_messages(message):
    if not os.path.exists(messages_file):
        open(messages_file, 'w').close()
    with open(messages_file, 'a', encoding='utf-8') as file:
        file.write(message.text + '\n')
