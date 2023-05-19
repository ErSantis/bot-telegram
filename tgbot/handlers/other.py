from telebot import TeleBot
from telebot.types import Message

def other(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(message.chat.id, "No entiendo lo que me quieres decir.\nUsa el comando /help para ver que puedo hacer.")