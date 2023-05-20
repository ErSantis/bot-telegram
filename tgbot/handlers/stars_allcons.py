from telebot import TeleBot
from telebot.types import Message
from tgbot.commands.stars_allcons import grafico_constelaciones
from tgbot.commands.constellations import read_stars, grafico_estrellas, read_constellations


def stars_allcons(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(
        message.chat.id, "Todas las estrellas y constelaciones.")
    
    stars = read_stars()
    r = read_constellations()
    image1 = 'tgbot/out/stcons.png'
    bot.send_photo(message.chat.id, open(image1, 'rb'))

    bot.send_message(
        message.chat.id, "Aqui una vista mejor de cada una de ellas.")
    r = read_constellations()

    
    for i, constelacion in enumerate(r):
        bot.send_message(message.chat.id,f'{constelacion}')
        image2 = f'tgbot/out/cons{i}.png'
        bot.send_photo(message.chat.id, open(image2, 'rb'))
 
    
  

    