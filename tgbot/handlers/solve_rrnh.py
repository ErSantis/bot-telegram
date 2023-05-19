from telebot import TeleBot
from telebot.types import Message
import numpy as np
from tgbot.commands.rrnh import get_gn, open_cases


def resolver_nh_handler(message: Message, bot: TeleBot):
    # Enviar un mensaje al usuario solicitando la relación de recurrencia homogénea
    bot.send_message(
        message.chat.id, "Por favor, ingresa el grado de la relación de recurrencia.")

    # Registrar un manejador para procesar la respuesta del usuario y solicitar el grado de la relación
    bot.register_next_step_handler(message, process_relacion_no_homogenea, bot)


def process_relacion_no_homogenea(message: Message, bot: TeleBot):
    # Almacenar la relación de recurrencia homogénea del usuario en una variable llamada relacion
    grado = message.text
    try:
        int(grado)
        bot.send_message(
        message.chat.id, "Escribe la relación de recurrencia \nNO USES * PARA LA MULTIPLICACIÓN \nEjemplo: 4f(n-2) - 4f(n-1) + n  \nf(n) = ")
        # Registrar un manejador para procesar la respuesta del usuario y solicitar las condiciones iniciales
        bot.register_next_step_handler(message, process_grado, bot, grado)
    except:
        bot.send_message(message.chat.id, "El grado debe ser un numero. Por favor digitelo nuevamente.")
        return bot.register_next_step_handler(message, process_relacion_no_homogenea, bot)
    


def process_grado(message, bot, grado):
    # Almacenar el grado de la relación de recurrencia del usuario en una variable llamada grado
    relacion = message.text

    # Solicitar las condiciones iniciales
    bot.send_message(
        message.chat.id, "Por favor, ingresa las condiciones iniciales separadas por comas (por ejemplo, 'a0,a1,a2').")

    # Registrar un manejador para procesar la respuesta del usuario y resolver la relación de recurrencia homogénea
    bot.register_next_step_handler(
        message, process_condiciones_iniciales, bot, grado,relacion)


def process_condiciones_iniciales(message, bot, grado,relacion):
    # Almacenar las condiciones iniciales del usuario en una lista llamada condiciones_iniciales

    # Responder al usuario con la solución de la relación de recurrencia homogénea
    try:
        cond = np.array(list(map(float, message.text.split(","))))
    except:
        bot.send_message(message.chat.id, "Error en las condiciones iniciales, Digitelas de nuevo")
        return bot.register_next_step_handler(
        message, process_condiciones_iniciales, bot, grado,relacion)
    
    try:
        response = open_cases(get_gn(relacion, int(grado)),
                          relacion, int(grado), cond)
        bot.send_message(message.chat.id, str(response))
    except:
        bot.send_message(message.chat.id, "Error en la relacion, empezemos de nuevo")
        return bot.register_next_step_handler(
        message, resolver_nh_handler, bot)

