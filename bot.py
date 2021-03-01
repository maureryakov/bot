from sys import path

import config
import telebot # pip install telebot
from telebot import types # pip install pyTelegramBotAPI
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):
    sti = open(path+'stiker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Приложения")
    item2 = types.KeyboardButton("Мероприятия")
    item1 = types.KeyboardButton('О нас')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\\n\\nЯ - <b>{1.first_name}</b>, бот команды Projector в НГТУ, "
                     "создан для того, "
                     "чтобы помочь Вам влиться в нашу команду,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\\n\\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    # RUN
    if __name__ == "__main__":
        try:
            bot.polling(none_stop=True)
        except ConnectionError as e:
            print('Ошибка соединения: ', e)
        except Exception as r:
            print("Непридвиденная ошибка: ", r)
        finally:
            print("Здесь всё закончилось")

            @bot.message_handler(content_types=["text"])
            def go_send_messages(message):
                if message.chat.type == 'private':
                    if message.text == 'Приложения':

                        keyboard = types.InlineKeyboardMarkup(row_width=1)
                        itemboo = types.InlineKeyboardButton(text="Тыщ на кнопку и ты уже в Google",
                                                             url="<https://www.google.ru>")
                        itemboo1 = types.InlineKeyboardButton('Рандомное число', callback_data='good2')
                        itemboo2 = types.InlineKeyboardButton("Калькулятор", callback_data='bad2')
                        itemboo3 = types.InlineKeyboardButton("Хочу узнать погоду в моем городе/стране",
                                                              callback_data='good3')
                        itemboo4 = types.InlineKeyboardButton("Как твои дела?", callback_data='bad4')

                        keyboard.add(itemboo, itemboo1, itemboo2, itemboo3, itemboo4)

                        bot.send_message(message.chat.id,
                                         "{0.first_name}, окей, смотри, что у нас есть тут:\\n".format(
                                             message.from_user),
                                         reply_markup=keyboard)

                    elif message.text == "Мероприятия":
                        one_markup = types.InlineKeyboardMarkup(row_width=1)
                        ite1 = types.InlineKeyboardButton("Ближайшие мероприятия", callback_data="one")
                        ite2 = types.InlineKeyboardButton("Проведенные мероприятия", callback_data="two")
                        ite3 = types.InlineKeyboardButton("Волонтерство на мероприятие", callback_data="three")
                        ite4 = types.InlineKeyboardButton("Действующие проекты в НГТУ", callback_data="fourth")
                        ite5 = types.InlineKeyboardButton("Мероприятия Межвузовского центра", callback_data="five")
                        one_markup.add(ite1, ite2, ite3, ite4, ite5)
                        bot.send_message(message.chat.id,
                                         "{0.first_name}, у нас <u>ежемесячно</u> проводится множество "
                                         "мероприятий,\\nмы постарались разбить их на следующие составляющие:".format(
                                             message.from_user), parse_mode="html", reply_markup=one_markup)

                        @bot.callback_query_handler(
                            func=lambda call: call.data in ['one', 'two', 'three', 'fourth', 'five'])  # Мероприятия
                        def callback_inline_one(call):
                            try:
                                if call.message:
                                    if call.data == 'one':  # Ближайшие мероприятия
                                        bot.send_message(call.message.chat.id,
                                                         "Итак,<b>ближайшие мероприятия</b>:\\n\\n"  # Здесь будут ссылки ещё
                                                         "Форум «Байкал»\\n"
                                                         "Конкурс «Цифровой ветер»\\n"
                                                         "PRONETI", parse_mode="html")
                                    elif call.data == 'two':  # Проведённые мероприятия
                                        bot.send_message(call.message.chat.id,
                                                         "Вот список <b>проведённых мероприятий</b>:\\n\\n"
                                                         "МНТК\\n"
                                                         "Семинары по проектной деятельности\\n"
                                                         "Встреча с представителями предприятий", parse_mode="html")
                                    elif call.data == 'three':@bot.message_handler(commands=['stop'])  # Обработка команды для выхода
def bye(message):
    bye_Sti = open(path+'byeMorty.tgs', 'rb')

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!\\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо провел(а) время \\n\\n"
                     "Присоединяйся к нашей команде в <a href='<https://vk.com/projector_neti>'>vk</a>\\n"
                     "Наш <a href='<https://instagram.com/projector_neti>'>inst</a>\\n\\n"
                     "Напиши Координатору проектов (<a href='<https://vk.com/nikyats>'>Никите Яцию</a>) и задай интересующие тебя вопросы по <i>проектной деятельности</i>\\n\\n"
                     "Надеемся, что тебе ответят очень скоро \\n\\n"
                     "<u>Don't be ill and have a nice day</u> \\n\\n\\n"
                     "P.S.: Если есть какие-то пожелания или вопросы по боту, то напиши <a href='<https://vk.com/setmyaddresspls>'>мне</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    exit()