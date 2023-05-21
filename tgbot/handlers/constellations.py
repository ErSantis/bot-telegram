from telebot import TeleBot
from telebot.types import Message

from tgbot.commands.constellations import read_stars, grafico_estrellas


def stars(message: Message, bot: TeleBot):
    stars = read_stars()
    bot.send_message(
        message.chat.id, "Aqui esta un grafico con todas las estrellas.")
    image = 'tgbot/out/estrellas.png'
    bot.send_photo(message.chat.id, open(image, 'rb'))


