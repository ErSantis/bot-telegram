from telebot import TeleBot
from telebot.types import Message

from tgbot.commands.constellations import read_stars, grafico_estrellas


def stars(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    stars = read_stars()
    bot.send_message(
        message.chat.id, "Aqui esta un grafico con todas las estrellas.")
    image = 'tgbot/out/estrellas.png'
    # enviamos la imagen, teniendo en cuenta que es un archivo local
    bot.send_photo(message.chat.id, open(image, 'rb'))


