import requests

# 1. 요청 보내기 
# result = requests.get('https://naver.com')
# print(result)


# 2. Response 객체를 문자열로 변환해서 받아보기 
#result = requests.get("https://naver.com").text
#print(result)
#print(type(result))

# 3. Response 객체를 통해 상태 코드 받아보기 
result = requests.get('https://naver.com').status_code
print(result)

