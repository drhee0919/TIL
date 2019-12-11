import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
#실시간 검색어 긁어온거 그대로 
#한두개 코드 긁어서 전체적으로 긁어오려면 어떻게 써야할지 고민 
# → li 태그 전체를 뽑아오게끔 손질해보자( li:nth-child(1) → li )
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

print(names)

#태그들을 제거해보자 
print(f'{datetime.now()} 기준 실시간 검색어') #fstring 기능 사용(3.6버전 이상부터)
for name in names:
    print(name.text)
