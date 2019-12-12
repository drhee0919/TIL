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


#app.py 가장 하단에 위치 시킬 것 
# 앞으로 flask run 으로 서버를 켜는게 아니라, pyton app.py로 서버를 실행한다. 
# 앞으로 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다. 

if __name__=='__main__':
    app.run(debug=True)