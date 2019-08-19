# ================= Импорт =====================================================
# ================= Импорт важных модулей=======================================
import telebot
import random
import urllib.request
import os
import requests
import json
import time
import threading
from datetime import datetime
# ================= Импорт своих модулей =======================================
import keyboardset
import gettingurls
import listoflists

# ================= Токен ======================================================
telegram_token = 'токен тут'
bot = telebot.TeleBot(telegram_token)

# ================= Команды ====================================================
# ================= Информация о боте ==========================================
@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    txt_name = "/help.txt"
    f = open (os.getcwd() + txt_name)
    bot.send_message(
        chat_id = message.chat.id,
        text = f.read())
# ================= Отразить клавиатуру ========================================
@bot.message_handler(commands=['go'])
def cmd_keyboard(message):
    kbrd = keyboardset.keyboard_main()
    bot.send_message(
        chat_id=message.chat.id,
        text='Нажми на кнопку, получишь результат',
        reply_markup=kbrd)
# =====================Узнать id ===============================================
@bot.message_handler(commands=['id'])
def cmd_id (message):
    bot.send_message(
        chat_id = message.chat.id,
        text = message.chat.id)
# =====================Для разных тестов========================================

# ==============Реакция на текст ===============================================
@bot.message_handler(content_types=["text"])
def text_msg (message):
    try:
# =============== Отправка гифок ===============================================
        if message.text in listoflists.gif_words:
            user_choice = listoflists.gif_words[message.text]
            user_url = gettingurls.get_gif_url(user_choice)
            bot.send_video(message.chat.id, user_url)
# =================== Классный совет ===========================================
        elif message.text.startswith('❗'):
            advice_text = gettingurls.get_advice_text()
            bot.send_message(
                chat_id= message.chat.id,
                text = 'Мой тебе совет: {}'.format(advice_text))
# =================== Погода ===================================================
        elif message.text.startswith('🌤'):
            weather_data = gettingurls.get_weather_data()
            bot.send_message(
                chat_id = message.chat.id,
                text = weather_data)
# =================== Валюты ===================================================
        elif message.text.startswith('📊'):
            money_courses = gettingurls.get_money_courses()
            bot.send_message(
                chat_id = message.chat.id,
                text = money_courses)
# =================== Ответ да/нет =============================================
        elif message.text.startswith('❓'):
            ANSWER_LIST = open('8ball.txt')
            ANSWER_LINE = ANSWER_LIST.readlines()
            bot.send_message(message.chat.id, "Мой тебе ответ: " + random.choice(ANSWER_LINE))
# ================== Рандомная гифка ===========================================
        elif message.text.startswith('🔀'):
            bot.send_message(message.chat.id, 'В разработке (」°ロ°)」')
# =================== Цитата ===================================================
        elif message.text.startswith('©️'):
            QUOTE_LIST = open('quote.txt')
            QUOTE_LINE = QUOTE_LIST.readlines()
            bot.send_message(message.chat.id, "Как говорил один мудрый человек: " + random.choice(QUOTE_LINE))
        elif message.text.startswith('🎙'):
            SONGS_LIST = open('songs.txt')
            SONGS_LINE = random.choice(SONGS_LIST.readlines())
            SONGS_LINE_EDIT = SONGS_LINE[:SONGS_LINE.find(';')] + '\n' + SONGS_LINE[SONGS_LINE.find(';') + 1:]
            bot.send_message(message.chat.id, "Хм, как насчет этой песни? " + "\n" + (SONGS_LINE_EDIT))
# ===================== Pey respect ============================================
        elif message.text.startswith("F"):
            bot.send_message(message.chat.id,"F")
# ===================== СПС - НЗ ===============================================
        elif message.text.lower() == "спс":
            bot.send_message(message.chat.id,"нз")
# ==================Реакция на мяу =============================================
        elif message.text.lower() in listoflists.meow_words:
            bot.send_message(message.chat.id, 'В разработке (」°ロ°)」')
        elif message.text.startswith("Олег, "):
            answer = open('how_are_you_answers.txt').readlines()
            bot.send_message(message.chat.id, random.choice(answer))
        else:
            pass
    except Exception as e:
        bot.send_message(
            message.chat.id,
            "Что-то пошло не так, @NIkolaiGavrilov ٩(ఠ益ఠ)۶:{}".format(e))

bot.polling(none_stop=True)
