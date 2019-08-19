import requests
import json
import random

api_url = 'https://openexchangerates.org/api/latest.json?app_id=b9979f9b0f334acc9cf366dcabaf4192'
r = requests.get(api_url)
data = json.loads(r.text)

money_type = {'BTC':'💰',
              'EUR':'💶',
              'USD':'💵'}
rub_value = data['rates']['RUB']
l = []
for i in money_type:
    money_value = (1/float(data['rates'][i]) * float(rub_value))
    money_text = '{} : {}'.format(money_type[i],round(money_value,2))
    l.append(money_text)
money_data = '\n'.join(map(str,l))
print(money_data
      )


