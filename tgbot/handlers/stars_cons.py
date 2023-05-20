from telebot import TeleBot
from telebot.types import Message
from tgbot.commands.stars_cons import grafico_constelacion
from tgbot.commands.constellations import read_stars, grafico_estrellas, read_constellations

def send_image(message: Message, bot: TeleBot,r):
    
    # Guardar el valor ingresado por el usuario en una variable
    try:
        conste = int(message.text)
        while conste < 0 or conste > 7:
                bot.send_message(message.chat.id, "El número debe estar entre 0 y 7. Por favor, ingrese otro número.")
                bot.register_next_step_handler(message, send_image, bot,r)
                return
        # Hacer algo con el valor, por ejemplo, enviar una respuesta al usuario
        stars = read_stars()
        image1 = f'tgbot/out/stcons{conste}.png'
        image2 = f'tgbot/out/cons{conste}.png'
        # enviamos la imagen, teniendo en cuenta que es un archivo local
       
        bot.send_message(message.chat.id,f'Grafico de la constelacion {list(r.keys())[int(conste)]}')
        bot.send_photo(message.chat.id, open(image1, 'rb'))
        bot.send_message(message.chat.id,f'Aqui un mejor avistamiento de la constelacion.')
        bot.send_photo(message.chat.id, open(image2, 'rb'))
    except:
        bot.send_message(message.chat.id, "La entrada debe ser un número entero. Por favor, inténtelo de nuevo.")
        bot.register_next_step_handler(message, send_image, bot,r)


def stars_cons(message: Message, bot: TeleBot):
    """
    You can create a function and use parameter pass_bot.
    """
    bot.send_message(
        message.chat.id, "Elige la constelacion")
    r = read_constellations()
    res = ''
    for i, constelacion in enumerate(r):
        res += f'{i}.{constelacion}\n'
    bot.send_message(message.chat.id,f'Las constelaciones disponibles son:\n{res}')
    # Registrar un manejador para el siguiente mensaje del usuario
    bot.register_next_step_handler(message, send_image, bot, r)
  

    