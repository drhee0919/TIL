from datetime import datetime
import random
from flask import Flask, render_template, request

app = Flask(__name__)
#"flask run" 명령어로 실행 
#terminal 에서 ctrl + c 누를 시 서버 탈출가능 


@app.route('/') #routing 하는 주소 경로 
def hello_world():
    #return "HIHIHI~~~~~~~ㄴㅁㅇㅁㄴㅇ~"
    return render_template('index.html') #templates 폴더의 index.html 내용 참조 
                                         #단, app.py와 같은 경로에 templates폴더를 생성 

@app.route('/mulcam') #주소에 다른 경로로 입력 
def mulcam():
    return '20층 스카이라운지'


@app.route('/dday')  
def dday():
    today = datetime.now()
    new_year = datetime(2020, 1, 1)
    result = new_year - today 
    return f'<h1><b>더 성숙해지기 까지 {result.days}일 남았습니다!</b><h1>' 
    #fstring 사용해서 날짜까지만 출력
    #html tag도 먹일 수 있다! 



@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name = name) #greeting html 참조 



@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱의 값은 {number**3}입니다.'



@app.route('/cube2/<int:number>')
def cube2(number):
    result = number **3
    return render_template('cube.html', number=number, result=result)



@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈수육정식', '고추잡채덮밥', '돼지불백', '샐러드', '히레카츠', '그냥 굶어라']
    
    order = random.sample(menu, people)
    return str(order) 
    #ex/ ['고추잡채덮밥', '돼지불백', '그냥 굶어라', '보쌈수육정식']



@app.route('/movie')
def movie():
    movies = ['나이브스 아웃', '조커', '엔드게임','어떤어떤 영화']
    return render_template('movie.html', movie_list=movies)




@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)    




@app.route('/naver')
def naver():
    return render_template('naver.html') 

@app.route('/google')
def google():
    return render_template('google.html') 





## vonvon 앱을 만들어보자!
## 사용자로부터 입력받을 페이지를 렌더링 해줌 
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

##요청을 받은 뒤 데이터를 가공해서 사용자에게 응답해줌
@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')

    #데이터 리스트 풀 생성
    first_options = ['잘생김','못생김','존잘','존못','쏘쏘']
    second_options = ['친절함','싹수','애교','잘난척']
    third_options = ['돈복','코딩력','물욕','식욕']
    
    sentence1 = ['을 한스푼', '을 두스푼']
    sentence2 = ['도 한컵','은 조금만']
    sentence3 = ['도 조금... 억ㅋ.. 쏟았네..', '는 조금만 으어어어어어', '는 필요없겠다']
    #각 데이터 리스트 별로 요소를 하나씩 무작위로 뽑음 
    first = random.choice(first_options)
    second = random.choice(second_options)
    third = random.choice(third_options)
    
    s1 = random.choice(sentence1)
    s2 = random.choice(sentence2)
    s3 = random.choice(sentence3)
    # 뽑은 데이터를 템플릿에 넘겨줌
     
    return render_template('godmademe.html', name=name, first=first, second=second, third=third,
                                             s1=s1, s2=s2, s3=s3  )

#app.py 가장 하단에 위치 시킬 것 
# 앞으로 flask run 으로 서버를 켜는게 아니라, python app.py로 서버를 실행한다. 
# 앞으로 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다. 

if __name__=='__main__':
    app.run(debug=True)