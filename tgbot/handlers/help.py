from telebot import TeleBot
from telebot.types import Message

def help(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    #Comandos disponibles
    res = "Estos son los comandos disponibles:\n/start - Inicia el bot\n/stars - Muestra un gráfico de todas las estrellas.\n/allstars_onecons - Muestra un gráfico de todas las estrellas y  una constelación.\n/allstars_allcons - Muestra un gráfico de todas las estrellas y todas las constelaciones.\n/solve - Resolver una relación de recurrencia lineal no homogénea con coeficientes constantes"
    bot.send_message(message.chat.id, res)