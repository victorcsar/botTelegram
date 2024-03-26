from dotenv import load_dotenv
import telebot
import os

load_dotenv()

CHAVE_API = os.getenv('chave_api')

bot = telebot.TeleBot(CHAVE_API)

id_permitido = int(os.getenv('user_permitido'))

lista_user_permitidos = {id_permitido}

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@balbalba.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Até mais")



def verificar(mensagem):
    user_id=mensagem.from_user.id
    print("ID do usario:",user_id)
    if(user_id in lista_user_permitidos):
        print ("true")
    
    return user_id in lista_user_permitidos

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Reclamar de um pedido
     /opcao3 Finalizar atendimento
     Responder qualquer outra coisa não vai funcionar, clique em uma das opções""" 
    bot.reply_to(mensagem, texto)

bot.polling()