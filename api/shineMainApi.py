from cryptography.fernet import Fernet
import telebot
import os

def load_key():
    current_dir = os.path.dirname(__file__)
    key_path = os.path.join(current_dir, 'secret.key')
    # Carrega a chave do arquivo
    return open(key_path, 'rb').read()

def decrypt_api_key():
    current_dir = os.path.dirname(__file__)
    key = load_key()  # Carrega a chave de criptografia
    fernet = Fernet(key)  # Cria um objeto Fernet com a chave

    # Carrega a API key criptografada do arquivo
    encrypted_api_key_path = os.path.join(current_dir, 'encrypted_api_key.bin')
    with open(encrypted_api_key_path, 'rb') as encrypted_file:
        encrypted_api_key = encrypted_file.read()

    # Descriptografa a API key
    decrypted_api_key = fernet.decrypt(encrypted_api_key)
    return decrypted_api_key.decode()

def botApi():  
    SHINEKUNAPI = decrypt_api_key()
    bot = telebot.TeleBot(SHINEKUNAPI)
    return bot

bot = botApi()

def get_bot_instance():
    return bot