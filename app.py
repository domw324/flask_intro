from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <h1>서버를 띄웠습니다.</h1>
    <h2>이동 할 곳을 고르세요</h2></br>
    <table border=1>
        <tr>
            <th colspan=4 width=800 height=100 align=center>Go to<th>
        </tr>
        <tr height=70>
            <td width=200 align=center>
                <a href='http://python-domw324.c9users.io:8080/html_tag'>HTML TAG</a>
            </td>
            <td width=200 align=center>
                <a href='http://python-domw324.c9users.io:8080/html_file'>HTML FILE</a>
            </td>
            <td width=200 align=center>
                <form action="http://python-domw324.c9users.io:8080">
                    <input type="text" name="cube"/>
                    <input type="submit" value="계산"/>
                </form>
            </td>
            <td width=200 align=center></td>
        </tr>
        <tr height=70>
            <td width=200 align=center>
                <a href='http://python-domw324.c9users.io:8080/lunch'>점심 뭐먹지?</a>
            </td>
            <td width=200 align=center>
                <a href ='http://python-domw324.c9users.io:8080/lotto' alt="로또"><img src="/images/lotto.jpg" alt="lotto"></a>
            </td>
            <td width=200 align=center>
                <a href='http://python-domw324.c9users.io:8080/naver'>네이버 검색</a>
            </td>
            <td width=200 align=center>
                <a href='http://python-domw324.c9users.io:8080/google'>구글 검색</a>
            </td>
        </tr>
    </table>
    '''
    
@app.route("/html_tag")
def html_tag():
    return '''
    <h1>첫번째 줄!</h1>
    <h2>두번째 줄!!</h2>
    <h3>세번째 줄!!</h3>
    <p>네번째 줄!!!</p>
    <a href='http://www.google.com'>구글</a>
    '''
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>") #name이란 변수명으로 받는다
def welcome(name):
    return render_template("welcome.html", people = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("cube.html", n = num);
    
@app.route("/lunch")
def lunch():
    menu_list = ["감자탕", "굶는다", "라면", "닭갈비", "등촌"]
    pick = random.choice(menu_list)
    return render_template("lunch.html", lunch = pick)
    
@app.route("/lotto")
def lotto():
    num_list = list(range(0,46))
    pick = random.sample(num_list,6)
    pick.sort()
    return render_template("lotto.html", lotto = pick)
    
@app.route('/naver')
def naver():
    return render_template("naver.html")
    
@app.route('/google')
def google():
    return render_template("google.html")