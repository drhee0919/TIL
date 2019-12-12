import requests

# 1. 요청 보내기 
# result = requests.get('https://naver.com')
# print(result)


# 2. Response 객체를 문자열로 변환해서 받아보기 
#result = requests.get("https://naver.com").text
#print(result)
#print(type(result)) #str형태로 네이버 메인화면 받아온 것을 확인 


# 3. Response 객체를 통해 상태 코드 받아보기 
result = requests.get('https://naver.com').status_code
print(result)
if result == 200:
    print('접속성공!')
elif result == 404:
    print('페이지가 없네요...')
