# ================= Импорт важных модулей=======================================
import requests
import json
import random

# ================= Получение URL для гифов ====================================
def get_gif_url(choice):
    main_key = 'https://yadi.sk/d/DtY9v-i9C4vZdw'
    main_limit = 100
    main_payload = {'public_key': main_key, 'limit': main_limit}
    main_url = 'https://cloud-api.yandex.net/v1/disk/public/resources'
    r = requests.get(main_url, params=main_payload)
    d = r.json()
    d1 = d.get('_embedded')
    d2 = d1.get('items')
    for i in d2:
        folder_key = i.get('public_url')
        folder_name = i.get('name')
        if folder_name == choice:
            if folder_key != None:
                folder_payload = {'public_key': folder_key, 'limit': main_limit}
                folder_url = main_url
                r = requests.get(folder_url, params=folder_payload)
                d = r.json()
                d1 = d.get('_embedded')
                d2 = d1.get('items')
                l = []
                for i in d2:
                    file_url = i.get('file')
                    l.append(file_url)
                    # print(file_count)
            else:
                print('sas1')
        else:
            pass
    gif_url = random.choice(l)
    return (gif_url)

# ================= Получение данных о  погоде =================================
def get_weather_data():
    city_icon = {
        'ЕКБ':'🏢',
        'ВЛГ':'🏘',
        'МСК':'🏪'}
    city_id = {
        'ЕКБ':'1486209',
        'ВЛГ':'472757',
        'МСК':'524901'}
    app_id = 'a0e42ea7fc5e40f37b2919d0858a77ca'
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    l = []
    for i in city_id:
        api_payload = {'id':city_id.get(i),'appid':app_id,'lang':'ru'}
        r = requests.get(api_url,params=api_payload)
        data = json.loads(r.text)
        temp = int(data['main']['temp'] - 273)
        desc = data['weather'][0]['description']
        data_text = '{} {}: {}°C | {} '.format(city_icon.get(i),i,temp,desc)
        l.append(data_text)
    weather_data = '\n'.join(map(str,l))
    return (weather_data)

# ================= Получение ахуенного совета =================================
def get_advice_text():
    api_url = 'http://fucking-great-advice.ru/api/random'
    r = requests.get(api_url)
    data = json.loads(r.text)
    advice = data['text']
    return(advice)

# ================= Получение курса валют ======================================
def get_money_courses():
    api_url = 'https://openexchangerates.org/api/latest.json?app_id=b9979f9b0f334acc9cf366dcabaf4192'
    r = requests.get(api_url)
    data = json.loads(r.text)

    money_type = {'BTC': '💰',
                  'EUR': '💶',
                  'USD': '💵'}
    rub_value = data['rates']['RUB']
    l = []
    for i in money_type:
        money_value = (1 / float(data['rates'][i]) * float(rub_value))
        money_text = '{} : {}'.format(money_type[i], round(money_value, 2))
        l.append(money_text)
    money_data = '\n'.join(map(str, l))
    return (money_data)
