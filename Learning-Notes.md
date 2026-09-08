# Learning Notes
> Baseball Stats Analyzer Project
> Personal IT Dictionary (JP & KR)

---

# Flask

Python으로 웹 애플리케이션을 만들기 위한 프레임워크이다.
Python과 HTML을 연결하여 브라우저에 웹페이지를 표시할 수 있다.


---

# localhost

내 컴퓨터에서만 실행되는 웹사이트이다.
이번 프로젝트에서 사용한 주소
http://127.0.0.1:5000
인터넷에는 공개되지 않는다.


---

# templates

HTML파일을 저장하는 폴더이다.
Flask는 templates 폴더 안의 HTML 파일을 자동으로 찾아 화면에 표시한다.


---

# static

CSS와 이미지 등을 저장하는 폴더이다.
화면 디자인과 관련된 파일을 관리한다.


---

# HTML

웹페이지의 구조를 만드는 언어이다.


---

# CSS

웹페이지의 디자인과 모양을 꾸미는 언어이다.


---

# Form

사용자가 입력한 데이터를 서버로 전송하기 위한 입력 폼이다.


---

# label

입력창의 이름을 표시하는 태그이다.


---

# input

데이터를 입력하는 태그이다.
type="text"    - 문자를 입력한다.
type="number"  - 숫자를 입력한다.


---
# button

누르면 작업을 실행하는 버튼이다.


---

# POST

HTML 폼의 데이터를 Flask 서버로 전송하는 방식이다.
<form method="POST">


---

# name

HTML과 Python을 연결하는 이름이다.
ex: <input name="hits"> -> request.form["hits"]


---

# request

브라우저에서 전송된 데이터를 받아오는 기능이다.


---

# request.form

HTML에서 입력한 값을 Python으로 가져온다.
ex: request.form["hits"]


---

# int()

문자열을 정수로 변환한다.
ex: int("20") -> 20


---

# if 

조건이 참일 때만 코드를 실행한다.
ex: if at_bats > 0:


---

# round()

소수점을 원하는 자리까지 반올림한다.
ex: round(8 / 20, 3) -> 0.4


---

# render_template()

Python의 데이터를 HTML에 전달하여 화면을 출력하는 함수이다.
ex: return render_template("index.html")


---

# Jinja2

Python 변수를 HTML에 표시하기 위한 템플릿 엔진이다.
ex: {{ average }}


---

# Git

파일의 변경 이력을 관리하는 도구이다.
게임의 저장 지점과 비숫한 역할을 한다.


---

# GitHub

Git 프로젝트를 저장하고 공유하는 서비스이다.


---

# README.md

프로젝트를 설명하는 파일이다.
GitHub에서 가장 먼저 표시된다.


---

# value

입력창에 값을 표시하는 속성이다.
ex: <input value="{{ player }}">
전송 후에도 입력한 내용을 유지할 수 있다.


---

# User Experience (UX)

사용자가 서비스를 이용하면서 느끼는 사용 경험이다.
입력한 내용을 유지하면 더 편리한 웹 애플리케이션이 된다.


---

# Multiple Variables

render_template()는 여러  개의 데이터를 HTML로 전달할 수 있다.
ex: plyer=plyer
    average=average


---

# Variable Initialization

변수를 사용하기 전에 초기값을 설정하는 것이다.
ex: obp = None
    walks = ""
미리 초기화하면 변수가 없어서 발생하는 오류를 방지할 수 있다.


---

# UnboundLocalError

초기화되지 않은 지역 변수를 사용할 때 발생하는 오류이다.
변수를 사용하기 전에 반드시 초기화해야 한다.


---

# Validation

Validation(입력 검증)은 사용자가 입력한 데이터가 올바른지 확인하는 과정이다.
잘못된 데이터를 막고 프로그램을 안전하게 실행하기 위해 사용한다.
ex:
'python'
if int(hits) > int(at_bats):
    error = "Hits cannot be greater than At Bats."


---

# Error Handling

Error Handling(오류 처리)은 오류가 발생했을 때 적절한 메시지를 표시하거나 프로그램이 
중단되지 않도록 하는 방법이다.
사용자가 문제의 원인을 쉽게 이해할 수 있도록 도와준다.
ex: 
'python'
error = "Hits cannot be greater than At Bats."


---

# Jinja2 if Statement

Jinja2에서는 'if' 문을 사용하여 조건에 따라 HTML을 표시할 수 있다.
ex:
'HTML'
{% if error %}
<p class="error">{{ error }}</p>
{% endif %}


---

# Honver

Hover는 마우스를 요소 위에 올렸을 때 스타일을 변경하는 CSS 가능이다.
웹페이지의 사용성과 디자인을 향상시킨다.
ex:
'CSS'
button:hover {
    background-color: #0056b3;
}


---

# Form Field Name

HTML의 'name' 속성은 Flask에서 폼 데이터를 받을 때 사용하는 이름이다.
HTML과 Python에서 같은 이름을 사용해야 한다.
ex:
'HTML'
<input name="home_runs">

'python'
home_runs = request.form["home_runs"]


---

# Debugging

Dibugging(디버깅)은 프로그램의 오류를 찾고 수정하는 과정이다.
오류 메시지를 읽고 원인을 찾는 것이 중요하다.


---

# List

List(리스트)는 여러 개의 데이터를 순서대로 저장할 수 있는 자료형이다.
ex:
'python'
players = []


---

# Dictionary

Dictionary(딕셔너리)는 키(key)와 값(value)을 한 쌍으로 저장하는 자료형이다.
ex:
'python'
players_data = {
    "player": player,
    "average": average,
    "obp": obp,
    "slg": slg
}


---

# append()

append()는 리스트의 마지막에 새로운 데이터를 추가하는 메서드이다.
ex:
'python'
players.append(player_data)


---

# Jinja2 for Loop

Jinja2의 for 문은 리스트의 데이터를 하나씩 반복하여 HTML에 표시할 때 사용한다.
ex:
'HTML'
{% for p in players %}
    <h3>{{ p.player }}</h3>
    <p>AVG : {{ p.average }}</p>
    <p>OBP : {{ p.obp }}</p>
    <p>SLG : {{ p.slg }}</p>
{% endfor %}


---

# render_template()

render_template()는 Python의 데이터를 HTML로 전달하는 함수이다.
리스트도 HTML로 전달할 수 있다.
ex:
'python'
return render_template(
    "index.html",
    players=players
)


---

# SQLite

SQLite는 데이터를 파일에 저장할 수 있는 가벼운 데이터베이스이다.
Python에서는 sqlite3 모듈을 사용하여 SQLite를 사용할 수 있다.


---

# sqlite3.connect()

sqlite3.connect()는 SQLite 데이터베이스에 연결하는 함수이다.
ex:
'python'
conn = sqlite3.connect("players.db)


---

# Cursor

Corsor(커서)는 SQLite 데이터베이스에 SQL 명령ㅇ을 실행하기 위한 객체이다.
ex:
'python'
cursor = conn.corsor()


---

# CREATE TABLE

CREATE TABLE은 새로운 테이블을 생성하는 SQL문이다.
IF NOT EXISTS를 사용하면 이미 테이블이 있어도 오류가 발생하지 않는다.
ex:
'SQL'
CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player TEXT,
    average TEXT,
    obp TEXT,
    slg TEXT
    )


---

# commit()

commit()은 데이터베이스의 변경 사항을 저장하는 메서드이다.
ex:
'python'
conn.commit()


---

# SELECT

SELECT는 데이터베이스에서 원하는 데이터를 조회하는 SQL 명령어이다.
ex:
'SQL'
SELECT player, average, obp, slg FROM players


---

# fetchall()

fetchall()은 SQL 쿼리로 조회한 모든 데이터를 가져오는 메서드이다.
ex:
'python'
players = for문과 인덱스를 사용하여 데이터베이스에서 가져온 데이터를 HTML에 표시할 수 있다.
ex:
'html'
{% for p in players %}
    <p>{{ p[0] }}</p>
    <p>{{ p[1] }}</p>
{% endfor %}


---

# 디버깅

개발 중 SQL과 Jinja2에서 발생한 문법 오류를 확인하고 수정할 수 있다.
ex:
'python'
SELECT player, average, obp, slg FROM players

'html'
{{ p[3] }}


---

# 오류가 없을 때만 실행하기

'if not error'를 사용하면 error가 없을 때만 코드를 실행할 수 있다.
ex:
'python'
if not error:
    cursor.execute(...)
    conn.commit()
오류가 있는 경우에는 데이터를 저장하지 않도록 할 수 있다.


---

# 입력값 검증

사용자가 입력한 값이 올바른지 확인한 후 계간이나 데이터 저장을 실행해야 한다.
ex:
'python'
if hit_total != int(hits):
    error = "Invalid input"


---

# URL Parameter

URL에 값을 포함하여 특정 데이터를 구분할 수 있다.

ex:

'python'
@app.route("/player/<int:player_id>")


---

# WHERE

WHERE를 사용하면 조건에 맞는 데이터만 조회할 수 있다.

ex:

'python'
SELECT player, average, obp, slg
FROM players
WHERE id = ?


---

# fetchone()

fetchone()은 조회 결과에서 하나의 데이터를 가져오는 메서드이다.

ex:

'python'
player = cursor.fetchone()


---

# Flask Route

Route를 사용하면 URL에 따라 다른 함수를 실행할 수 있다.

ex:

'python'
@app.route("/player/<int:player_id>")
def player_detail(player_id):
    ...


---

# DELETE

DELETE는 데이터베이스에서 데이터를 삭제할 때 사용하는 SQL 명령어이다.

ex:

'python'
DELETE FROM players WHERE id = ?


---

# WHERE

WHERE를 사용하면 특정 조건에 맞는 데이터만 삭제할 수 있다.

ex:

'python'
DELETE FROM players WHERE id = ?


---

# POST

POST는 서버에 데이터를 보내거나 데이터를 변경할 때 사용할 수 있다.

ex:

'python'
@app.route("/player/<int:player_id>/delete", methods=["POST"])


---

# redirect()

redirect()는 작업이 완료된 후 다른 URL로 이동할 때 사용한다.

ex:

'python'
return redirect("/")


---

# 데이터 삭제

Flask에서 SQL 쿼리를 실행하고 commit()하면 데이터베이스의 내용을 변경할 수 있다.

ex:

'python'
cursor.execute("DELETE FROM players WHERE id = ?", (player_id,))
conn.commit()


---

# CSS Design

CSS를 사용하여 웹페이지의 색상과 레이아웃을 꾸밀 수 있다.
배경, 카드, 버튼 등의 스타일을 설정하여 UI를 개선할 수 있다.

ex:
'CSS'
body {
    background-color: #eef7f1;
    color: #243b2f;
}


---

# background-color

background-color는 요소의 배경색을 설정하는 CSS 속성이다.

ex:
'CSS'
body {
    background-color: #eef7f1;
}


---

# border-radius

border-radius는 요소의 모서리를 둥글게 만드는 CSS 속성이다.

ex:
'CSS'
.card {
    border-radius: 18px;
}


---

# box-shadow

box-shadow는 요소에 그림자를 추가하는 CSS 속성이다.
카드나 버튼을 입체적으로 보이게 만들 수 있다.

ex:
'CSS'
.card {
    box-shadow: 0 6px 18px rgba(23, 107, 58, 0.12);
}


---

# CSS Card Design

background-color, border, border-radius, box-shadow 등을 사용하면
HTML 요소를 카드 형태로 디자인할 수 있다.

ex:
'CSS'
.history-card {
    background-color: #f7fbf8;
    border: 2px solid #d5eadc;
    border-radius: 14px;
}


---

# UI Design

UI는 사용자가 웹페이지를 보고 조작하는 화면이다.
색상, 크기, 간격, 버튼 등을 조절하여 보기 쉽고 사용하기 편한 화면을 만들 수 있다.

오늘은 Scoreboard와 Player History를 카드 형태로 디자인하여
웹페이지의 UI를 개선했다.


---

# CSS Transition

transition은 CSS 속성이 변경될 때 부드럽게 변화하도록 만드는 속성이다.

ex:
'CSS'
button {
    transition: 0.3s;
}


---

# transform

transform은 요소의 위치나 크기 등을 변경할 수 있는 CSS 속성이다.

ex:
'CSS'
button:hover {
    transform: translateY(-2px);
}


---

# CSS Grid


CSS Grid는 요소를 행과 열로 배치할 수 있는 CSS 레이아웃 기능이다.


ex:
'css'
.input-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

입력창을 2열로 배치하여 긴 폼을 더 깔끔하게 만들 수 있다.


---

# grid-column

grid-column은 Grid 요소가 차지하는 열의 범위를 지정하는 CSS 속성이다.

ex:
'css'
.input-grid div:last-child {
    grid-column: 1 / 3;
}

Home Runs 입력창처럼 특정 요소를 여러 열에 걸쳐 배치할 수 있다.


---

# linear-gradient()

linear-gradient()는 CSS에서 색상이 자연스럽게 변하는 배경을 만드는 기능이다.

ex:
'css'
background: linear-gradient(
    to bottom,
    #dff3e5 0%,
    #eef7f1 45%,
    #b8d99c 45%,
    #8fbd70 100%
);

위에서 아래로 색상이 바뀌는 배경을 만들 수 있다.


---

# box-shadow

box-shadow는 요소에 그림자 효과를 추가하는 CSS 속성이다.
ex:
'css'
box-shadow: 0 8px 20px rgba(23, 107, 58, 0.12);

카드나 버튼에 그림자를 추가하여 입체적인 느낌을 만들 수 있다.


---

# CSS border

border는 요소의 테두리를 설정하는 CSS 속성이다.
ex:
'css'
border: 3px solid #d5eadc;

입력 폼이나 Scoreboard의 영역을 구분하고 디자인을 꾸밀 수 있다.


---
# Scoreboard UI

Scoreboard UI는 중요한 데이터를 한눈에 볼 수 있도록 표시하는 디자인이다.
이번 프로젝트에서는 AVG, OBP, SLG를 각각의 stat-box에 표시하여 야구 스코어보드처럼 디자인했다.
ex:
'html'
<div class="stat-box">
    <h3>AVG</h3>
    <p>{{ average }}</p>
</div>


---

# UI Layout

UI Layout은 웹페이지의 요소를 보기 좋게 배치하는 것이다.
입력창을 2열로 배치하고 Scoreboard의 크기와 간격을 조정하여 화면의 균형을 개선할 수 있다.


---

# Input Value

HTML의 value 속성을 사용하면 입력창에 값을 표시할 수 있다.
'html'
ex:
<input type="text" name="player" value="{{ player }}">

Flask에서 전달한 값을 입력창에 다시 표시할 수 있다.
입력값을 모두 유지하려면 Flask에서 각 변수를 render_template()으로 HTML에 전달해야 한다.


---

# CSS Linear Gradient

linear-gradient()를 사용하면 배경의 색상을 자연스럽게 변화시킬 수 있다.

ex:
'CSS'
background: linear-gradient(
    to bottom,
    #cfe9f7 0%,
    #eef7f1 57.5%,
    #b8d99c 57.5%,
    #8fbd70 100%
);


---

# Repeating Linear Gradient

repeating-linear-gradient()를 사용하면 반복되는 줄무늬나 패턴을 만들 수 있다.

ex:
'CSS'
background:
    repeating-linear-gradient(
        to right,
        rgba(255, 255, 255, 0.08) 0px,
        rgba(255, 255, 255, 0.08) 35px,
        transparent 35px,
        transparent 70px
    );


---

# CSS Background

CSS의 background를 사용하면 웹페이지의 배경 색상이나 패턴을 설정할 수 있다.

이번 프로젝트에서는 하늘과 잔디를 표현하여 야구장 같은 분위기를 만들었다.


---

# rgba()

rgba()는 색상에 투명도를 추가할 수 있는 CSS 함수이다.

ex:
'CSS'
rgba(255, 255, 255, 0.08)

마지막 숫자가 작을수록 색상이 더 투명하게 표시된다.


---

# box-shadow

box-shadow는 요소에 그림자 효과를 추가하는 CSS 속성이다.

ex:
'CSS'
box-shadow: 0 5px 12px rgba(0, 0, 0, 0.2);

카드나 버튼을 입체적으로 보이게 만들 수 있다.


---

# CSS Gradient Design

Gradient와 색상, 패턴을 조합하면 웹페이지에 원하는 분위기를 만들 수 있다.

이번 프로젝트에서는 하늘과 잔디 색상을 사용하여 야구장 느낌의 배경을 만들었다.


---

# Variable Initialization

변수를 사용하기 전에 초기값을 설정해야 한다.

ex:
'python'
singles = ""
doubles = ""
triples = ""

초기화하지 않은 변수를 사용하면 UnboundLocalError가 발생할 수 있다.


---

# CSS UI Design

CSS를 사용하면 웹페이지의 색상, 크기, 간격, 그림자 등을 변경하여 사용자에게 더 보기 좋은 UI를 만들 수 있다.

이번 프로젝트에서는 scoreboard를 야구장의 전광판처럼 디자인했다.


---

# Player Card

Player History를 선수 카드 형태로 표시하는 디자인을 추가했다.

선수 이름뿐만 아니라 AVG・OBP・SLG도 카드 안에 표시하여 선수의 성적을 한눈에 확인하기 쉽게 만들었다.

ex:

<div class="history-card">

    <h3>⚾ {{ p[1] }}</h3>

    <div class="player-stats">

        <div>
            <span>AVG</span>
            <strong>{{ p[2] }}</strong>
        </div>

        <div>
            <span>OBP</span>
            <strong>{{ p[3] }}</strong>
        </div>

        <div>
            <span>SLG</span>
            <strong>{{ p[4] }}</strong>
        </div>

    </div>

    <a href="/player/{{ p[0] }}">View Stats →</a>

</div>


---

# display: flex

CSS에서 여러 요소를 가로 방향으로 배치하기 위해 사용하는 속성이다.

ex:

.player-stats {
    display: flex;
    justify-content: center;
    gap: 12px;
}


---

# justify-content

Flexbox에서 요소의 정렬 위치를 설정하는 CSS 속성이다.

ex:

justify-content: center;

요소를 가운데에 정렬한다.


---

# gap

Flexbox에서 요소와 요소 사이의 간격을 설정하는 CSS 속성이다.

ex:

gap: 12px;

요소 사이에 12px의 간격을 만든다.


---

# transform: translateY()

요소를 위아래 방향으로 이동시키는 CSS 속성이다.

ex:

transform: translateY(-4px);

요소를 위쪽으로 4px 이동시킨다.
이번 프로젝트에서는 Scoreboard의 stat-box에 hover했을 때 요소가 조금 위로 올라가도록 사용했다.


---

# transition

CSS 속성의 변화를 부드럽게 만들어주는 속성이다.

ex:

transition: 0.3s;

hover와 같은 변화가 0.3초 동안 부드럽게 적용된다.


---

# CSS box-shadow

HTML 요소에 그림자를 추가하는 CSS 속성이다.

ex:

box-shadow: 0 5px 12px rgba(0, 0, 0, 0.2);

Player Card와 Scoreboard에 입체적인 느낌을 주기 위해 사용했다.


---

# CSS border

HTML 요소의 테두리를 설정하는 CSS 속성이다.

ex:

border: 3px solid #52665a;

Scoreboard의 바깥쪽 테두리를 설정하는 데 사용했다.
처음에는 골드 색상의 테두리를 사용했지만, 너무 강한 느낌이 있어서 그린 계열의 테두리로 변경했다.


---

# Scoreboard Design

AVG・OBP・SLG를 야구 Scoreboard처럼 표시하는 디자인을 개선했다.
어두운 그린을 기본 색상으로 사용하고 골드 색상을 포인트로 사용했다.
바깥쪽 테두리는 골드에서 그린 계열로 변경하여 전체적인 디자인을 더 부드럽게 만들었다.


---

# Hover Effect

마우스를 요소 위에 올렸을 때 디자인이 변화하는 기능이다.

ex:

.stat-box:hover {
    transform: translateY(-4px);
}

Scoreboard의 성적 박스에 마우스를 올리면 박스가 조금 위로 올라가도록 만들었다.


---

# URL Parameter

URL에 선수 ID를 포함하여 특정 선수의 상세 페이지를 표시하는 방법이다.

ex:

<a href="/player/{{ p[0] }}">View Stats →</a>

p[0]에는 데이터베이스에서 가져온 선수 ID가 들어 있다.


---

# Player ID

데이터베이스에서 각각의 선수를 구분하기 위한 ID이다.
Player Card의 View Stats를 클릭하면 Player ID를 URL로 전달하여 특정 선수의 상세 페이지를 열 수 있다.


---

# UPDATE

UPDATE는 데이터베이스에 이미 저장된 데이터를 변경할 때 사용하는 SQL 명령어이다.
이번 프로젝트에서는 앞으로 같은 선수를 다시 입력했을 때 기존 선수의 성적을 업데이트하는 기능에 사용할 예정이다.

ex:

UPDATE players
SET hits = ?
WHERE id = ?


---

# UI Design

UI Design은 사용자가 보는 화면의 구조와 디자인을 만드는 것이다.
이번 프로젝트에서는 Player Card와 Scoreboard의 디자인을 개선하고, 색상・간격・테두리・그림자 등을 조정하여 야구 느낌이 나는 UI를 만들었다.


---

# Cumulative Data

Cumulative Data(누적 데이터)는 이전에 저장된 데이터에 새로운 데이터를 더해서 계속 업데이트하는 것이다.

이번 프로젝트에서는 같은 선수의 At Bats, Hits, Singles, Doubles, Triples, Walks, Home Runs를 기존 데이터에 더해서 누적했다.

ex:

'python'
total_at_bats = old_at_bats + new_at_bats
total_hits = old_hits + new_hits


---

# Existing Player Check

Existing Player Check는 데이터베이스에 같은 선수가 이미 존재하는지 확인하는 과정이다.

이번 프로젝트에서는 SELECT를 사용하여 같은 이름의 선수가 있는지 확인한 후, 기존 선수이면 UPDATE를 사용하고 새로운 선수이면 INSERT를 사용하도록 만들었다.

ex:

'python'
cursor.execute(
    "SELECT id FROM players WHERE player = ?",
    (player,)
)

existing_player = cursor.fetchone()

if existing_player:
    UPDATE
else:
    INSERT


---

# Recalculate

Recalculate는 기존 데이터를 바탕으로 계산 결과를 다시 계산하는 것이다.

이번 프로젝트에서는 새로운 데이터를 기존 선수의 통계에 누적한 후 AVG, OBP, SLG를 다시 계산했다.


---

# Total Bases

Total Bases는 안타의 종류에 따라 타자가 기록한 총 루타를 나타내는 값이다.

Singles는 1루타이므로 1,
Doubles는 2루타이므로 2,
Triples는 3루타이므로 3,
Home Runs는 4루타이므로 4를 곱한다.

ex:

'python'
total_bases = (
    singles
    + doubles * 2
    + triples * 3
    + home_runs * 4
)


---

# Database Record

Database Record는 데이터베이스에 저장되어 있는 하나의 데이터 기록이다.

이번 프로젝트에서는 한 명의 선수가 하나의 record가 되며, 선수 이름과 누적 타격 데이터를 함께 저장한다.


---

# Data Persistence

Data Persistence는 프로그램을 종료하거나 새로운 데이터를 입력한 후에도 데이터가 계속 저장되어 있는 것이다.

이번 프로젝트에서는 SQLite 데이터베이스에 선수의 통계를 저장하기 때문에 Flask를 다시 실행해도 저장된 선수 데이터를 사용할 수 있다.


---

# flex-wrap

Flexbox에서 요소가 한 줄에 모두 들어가지 않을 때
다음 줄로 자동으로 줄바꿈하는 속성이다.

ex:

.player-stats {
    display: flex;
    flex-wrap: wrap;
}

이번 프로젝트에서는 Player Stats의 여러 통계 카드를
화면 크기에 맞게 여러 줄로 배치하기 위해 사용했다.


---

# justify-content: center

Flexbox에서 요소들을 가로 방향의 가운데에 배치하는 속성이다.

ex:

.player-stats {
    display: flex;
    justify-content: center;
}

이번 프로젝트에서는 Player Stats의 통계 카드가
한쪽으로 치우치지 않고 가운데에 오도록 만들기 위해 사용했다.


---

# @media

화면 크기와 같은 조건에 따라 다른 CSS를 적용할 수 있는 기능이다.

ex:

@media (max-width: 600px) {
    .player-stats div {
        width: 85px;
    }
}

이번 프로젝트에서는 화면이 작아졌을 때
Player Stats의 카드 크기를 조정하여 레이아웃이 깨지지 않도록 사용했다.


---

# ALTER TABLE

ALTER TABLE은 기존 데이터베이스 테이블의 구조를 변경할 때 사용하는 SQL문이다.

기존 테이블에 새로운 컬럼을 추가할 수 있다.

ex:
```sql
ALTER TABLE players ADD COLUMN ops TEXT;
```

기존 데이터를 삭제하지 않고 새로운 컬럼을 추가할 때 사용할 수 있다.

---

# CREATE TABLE IF NOT EXISTS의 한계

CREATE TABLE IF NOT EXISTS는 테이블이 존재하지 않을 경우에만 테이블을 생성한다.

이미 테이블이 존재하면 새로운 컬럼을 추가하거나 기존 테이블의 구조를 변경하지 않는다.

따라서 기존 테이블에 새로운 컬럼을 추가해야 할 경우에는 `ALTER TABLE`을 사용해야 한다.

---

# SQL Placeholder 개수

SQL문의 `?` placeholder 개수와 전달하는 값의 개수는 서로 일치해야 한다.

ex:
```python
cursor.execute(
    "INSERT INTO players (player, average, ops) VALUES (?, ?, ?)",
    (player, average, ops)
)
```

3개의 `?`가 있으므로 전달하는 값도 3개가 필요하다.

---

# SQL 결과의 인덱스

SELECT로 여러 개의 컬럼을 조회하면 조회된 데이터는 순서에 따라 인덱스로 접근할 수 있다.

ex:
```sql
SELECT player, average, obp, slg, ops FROM players
```

```html
{{ p[0] }}
{{ p[1] }}
{{ p[2] }}
{{ p[3] }}
{{ p[4] }}
```

SELECT 컬럼을 추가하거나 순서를 변경하면 HTML에서 사용하는 인덱스도 함께 확인해야 한다.