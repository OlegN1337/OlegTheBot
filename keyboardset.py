from telebot import types
def keyboard_main():
# ================= Вся клавиатура =============================================
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    siski_btn = types.KeyboardButton(text='🔞🍓')
    popki_btn = types.KeyboardButton(text='🔞🍑')
    meow_btn = types.KeyboardButton(text='🐱')
    popugi_btn = types.KeyboardButton(text='🐦')
    sovi_btn = types.KeyboardButton(text='🦉')
    rndmgif_btn = types.KeyboardButton(text='🔀')
    song_btn = types.KeyboardButton(text='🎙')
    weather_btn = types.KeyboardButton(text='🌤')
    advice_btn = types.KeyboardButton(text='❗️')
    answer_btn = types.KeyboardButton(text='❓')
    wisdom_btn =  types.KeyboardButton(text='©️')
    course_btn =  types.KeyboardButton(text='📊')
    kbrd.row(siski_btn, popki_btn, meow_btn)
    kbrd.row(popugi_btn, sovi_btn, rndmgif_btn)
    kbrd.row(advice_btn, answer_btn,song_btn)
    kbrd.row(weather_btn,wisdom_btn, course_btn)
    return kbrd

def keyboard_game_KNB():
# ================= Камень ножницы бумага ======================================
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kamen_btn = types.KeyboardButton(text="💎")
    nozhnicu_btn = types.KeyboardButton(text="✂️")
    bymaga_btn = types.KeyboardButton(text="📄")
    kbrd.row(kamen_btn,nozhnicu_btn,bymaga_btn)
    return kbrd

def keyboard_YN():
# ================= Да/Нет =====================================================
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes_btn = types.KeyboardButton(text="✅")
    no_btn = types.KeyboardButton(text="❌")
    kbrd.row(yes_btn,no_btn)
    return kbrd