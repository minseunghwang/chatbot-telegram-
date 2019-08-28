from flask import Flask
import random
import Lotto
import requests


app = Flask(__name__)

@app.route('/')     # path
def home():
    return 'hello'


# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을때 무엇을 할 지 정의

@app.route('/hello/<name>')
def hello(name):
    # return 'hello' + name
    # return 'hello {}'.format(name)
    return f'hello {name}'  # 오늘날 가장 모던한 파이썬스타일 (3.7버젼 부터 가능)

@app.route('/square/<int:number>')
def square(number):
    # number를 제곱하여 반환
    # 1. 글자 number를 숫자로 변환
    return str(number ** 2)

@app.route('/menu')
def menu():
    foods =['바스버거','대우식당','진가와','고갯마루']
    food = random.choice(foods)
    # foods안에 있는 항목중 하나를 무작위로 선택해준다.
    return food

@app.route('/lotto')
def lotto():
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    res_dict = response.json()     # 이 결과물이 파이썬 딕셔너리로 나오게 되요(string형태였던게 )

    result = []
    for i in range(1,7):
        result.append(res_dict[f'drwtNo{i}'])

    winner =[3,5,12,13,33,39]
    # result = sorted(random.sample(range(1,46),6))
 
    # cnt = len(set(winner) & set(result))
    cnt = len(set(winner) & set(result))

    rank = '꽝'
    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'

    # 만약 6개가 모두 일치하면
    # -> 1등
    # 만약 5개가 일치하면
    # -> 3등
    # 만약 4개가 일치하면
    # -> 4등
    # 만약 3개가 일치하면
    # -> 5등
    
    # return str(result) + str(winner) + rank + str(cnt)
    return rank
