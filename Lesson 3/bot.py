import telebot
    
bot = telebot.TeleBot("8146895436:AAFbfafbJdP2cp6sqgZGRmDeFrljtKNBKGk")

from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Привет! Я твой Telegram бот.\n Список команд:\n /start - запустить бота\n /hello - поприветствовать\n /bye - попращаться\n /password - сгенерировать 10-ти значный пароль\n /emodji -сгенерировать рандомный эмоджи\n /coin - бросить монетку")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
  bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
  bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['password'])
def send_bye(message):
  bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['emodji'])
def send_bye(message):
  bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['coin'])
def send_bye(message):
  bot.reply_to(message, flip_coin())
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "Извините, я не понимаю вашу команду!")
    
bot.polling()
