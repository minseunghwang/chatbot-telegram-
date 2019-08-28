"""
python으로 telegram message 보내기
"""

import requests

base_url = 'https://api.telegram.org/'
token = '841679492:AAFkqsNCOUwvCqQ_K9ABMxg0qHvaC072ovk'

# (1) getUpdates를 통해 내 id를 가져옴
# url = f'{base_url}bot{token}/getUpdates'
response = requests.get(url)
res_dict = response.json()

chat_id ='chat_id=' + str(res_dict['result'][0]['message']['chat']['id'])

# chat_id = 'chat_id='+str(955340098) 

# # (2)

method = '/sendMessage?'
msg = '&text=같은곳에서'
url = base_url +'bot'+ token + method + chat_id + msg
print(url)


requests.get(url)