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