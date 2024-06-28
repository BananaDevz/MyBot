import markovify
import os
import random

# Função para treinar a cadeia de Markov com base no arquivo de mensagens
def train_markov_chain(file_path, state_size=2):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.Text(text, state_size=state_size)
    return text_model

# Caminho para o arquivo de mensagens
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'mensagens.txt')

# Inicializa o modelo de cadeia de Markov
text_model = train_markov_chain(file_path, state_size=3)  # Exemplo de aumento do state_size

# Função para gerar uma resposta com base na pergunta
def generateResponse(question):
    # Divide a pergunta em frases para tentar iniciar a resposta
    phrases = question.split('.')
    random.shuffle(phrases)  # Embaralha para tentar diferentes inícios

    response = None
    
    # Tenta várias vezes para garantir uma resposta com base na pergunta
    for phrase in phrases:
        try:
            response = text_model.make_sentence_with_start(phrase.strip())
        except markovify.text.ParamError:
            continue
        if response:
            break
    
    if not response:
        # Se não conseguir gerar com as frases da pergunta, tenta gerar uma sentença qualquer
        response = text_model.make_sentence()
    
    return response
