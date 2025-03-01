import time, threading, schedule
import telebot

from telebot import formatting

from config import gen_pass
from config import gen_emodji
from config import flip_coin
from config import API_TOKEN
from email import message

Token = API_TOKEN

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я твой Telegram бот. Нипишите /help чтобы открыть список команд")
	
@bot.message_handler(commands=['formation'])
def send_formation(message):
	bot.send_message(
        message.chat.id,
        # function which connects all strings
        formatting.format_text(
            formatting.mbold(message.from_user.first_name),
            formatting.mitalic(message.from_user.first_name),
            formatting.munderline(message.from_user.first_name),
            formatting.mstrikethrough(message.from_user.first_name),
            formatting.mcode(message.from_user.first_name),
            separator=" " # separator separates all strings
        ),
        parse_mode='MarkdownV2'
    )
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
	bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
	bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['password'])
def send_password(message):
	bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
	bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['coin'])
def send_coin(message):
	bot.reply_to(message, flip_coin())  

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Список команд:\n /start - запустить бота\n /set <секунды> <сообщение> - поставить таймер\n /unset - сбросить таймер\n /help - открыть список команд\n /hello - поприветствовать\n /bye - попращаться\n /password - сгенерировать 10-ти значный пароль\n /emodji -сгенерировать рандомный эмоджи\n /coin - бросить монетку\n /formation - показать пример форматирования текста")

def beep(chat_id, user_text) -> None:
	"""Send the beep message."""
	bot.send_message(chat_id, text=user_text)

@bot.message_handler(commands=['set'])
def set_timer(message):
	args = message. text. split()
	user_text = message.text.split() [2:]
	if len(args) > 1 and args[1].isdigit():
		sec = int(args[1])
		schedule.every(sec).seconds.do(beep, message.chat.id, user_text).tag(message.chat.id)
	
	else:
		bot.reply_to(message, 'Использование: /set <секунды> <сообщение>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)

bot.send_message(
        message.chat.id,
        formatting.mbold(message.from_user.first_name),
        parse_mode='MarkdownV2'
    )

    # html
bot.send_message(
    message.chat.id,
    formatting.format_text(
        formatting.hbold(message.from_user.first_name),
        formatting.hitalic(message.from_user.first_name),
        formatting.hunderline(message.from_user.first_name),
        formatting.hstrikethrough(message.from_user.first_name),
        formatting.hcode(message.from_user.first_name),
        # hide_link is only for html
        formatting.hide_link('https://telegra.ph/file/c158e3a6e2a26a160b253.jpg'),
        separator=" "
    ),
    parse_mode='HTML'
)

    # just a bold text in html
bot.send_message(
    message.chat.id,
    formatting.hbold(message.from_user.first_name),
    parse_mode='HTML'
)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "Извините, я не понимаю вашу команду!")

bot.infinity_polling()