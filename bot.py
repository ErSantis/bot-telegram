# filters
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user
from tgbot.handlers.constellations import stars
from tgbot.handlers.stars_cons import stars_cons
from tgbot.handlers.stars_allcons import stars_allcons
from tgbot.handlers.help import help
from tgbot.handlers.other import other
from tgbot.handlers.solve_rrnh import resolver_nh_handler

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func

# states
from tgbot.states.register_state import Register

# utils
# from tgbot.utils.database import Database

# telebot
from telebot import TeleBot

# config
from tgbot import config

# db = Database()

# remove this if you won't use middlewares:
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
bot = TeleBot(config.TOKEN, num_threads=5)

def register_handlers():
    bot.register_message_handler(admin_user, commands=['start'], admin=True, pass_bot=True)
    bot.register_message_handler(any_user, commands=['start'], admin=False, pass_bot=True)
    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)
    bot.register_message_handler(help, commands=['help'], pass_bot=True)
    bot.register_message_handler(stars, commands=['stars'], pass_bot=True)
    bot.register_message_handler(stars_cons, commands=['allstars_onecons'], pass_bot=True)
    bot.register_message_handler(stars_allcons, commands=['allstars_allcons'], pass_bot=True)
    bot.register_message_handler(resolver_nh_handler, commands=['solve'], pass_bot=True)
    bot.register_message_handler(other, content_types=['text'],pass_bot=True)

register_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])


# custom filters
bot.add_custom_filter(AdminFilter())

def run():
    print('Bot is running...')
    bot.infinity_polling()

run()
