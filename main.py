import telebot
import types
import sqlite3

#bot123
bot = telebot.TeleBot('5302426258:AAG_Wf4XOLf4lkWdRBzmKca3PcwRQWDU1FQ')

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

#check and add in fields
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже существует !', parse_mode='html')

#delete if fields
@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()



@bot.message_handler(commands=['website'])
def website(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Посетить вебсайт", url="https://www.instagram.com/tsapenkovaleriya.photo/"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    website = telebot.types.KeyboardButton('Инстаграм')
    start = telebot.types.KeyboardButton('Старт')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

bot.polling(none_stop=True) 