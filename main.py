import telebot
import os
from markovchain.MarkovC import generateResponse
from api.shineMainApi import botApi

bot = botApi()  # Carrega o bot usando o token descriptografado

messages_file = 'mensagens.txt'

@bot.message_handler(commands=['github'])
def send_github_link(message):
    github_url = "https://github.com/Shine-Kun-Bot/ShineKunBot"
    bot.reply_to(message, f"Acesse o repositório do projeto no GitHub: {github_url}")

@bot.message_handler(commands=['ia'])
def markovResposta(message):
    # Chama a função para gerar uma resposta com a cadeia de Markov treinada
    question = message.text  # Usa a mensagem recebida como pergunta
    response = generateResponse(question)
    if response:
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Não consegui gerar uma resposta. Tente novamente.")

@bot.message_handler(commands=['start'])
def respostaPadrao(message):
    texto = """
Olá, sou o shine kun bot! Como vai? Escolha uma das opções do que você precisa:
/ia gera uma resposta aleatória com base nas mensagens que ela foi treinada.
/github manda o link do nosso projeto.
    """
    bot.reply_to(message, texto)

@bot.message_handler(func=lambda message: True)
def save_messages(message):
    with open(messages_file, 'a', encoding='utf-8') as file:
        file.write(message.text + '\n')

if __name__ == "__main__":
    if not os.path.exists(messages_file):
        open(messages_file, 'w').close()

    bot.polling(none_stop=True)
