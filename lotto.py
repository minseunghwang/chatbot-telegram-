"""
request를 통해 동행복권 API 요청을 보내어,
1등 번호를 가져와 python list로 만듬
"""

import requests
import app
def lottorequest():
    # 1. requests 통해 요청 보내기
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    # print(response.text)
    res_dict = response.json()     # 이 결과물이 파이썬 딕셔너리로 나오게 되요(string형태였던게 )
    # print("\n")
    # print(res_dict)

    result = []
    for i in range(0,6):
        if 'drwtNo'+str(i) in res_dict:
            result.append(str(res_dict['drwtNo'+str(i)]))
    return result
    # app.lotto(result)
    # 1등번호 6개가 담긴 result 라는 list를 출력하세요

print(lottorequest())