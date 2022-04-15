# Django 과목평가 대비

### Static web page (정적 웹 페이지)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- 일반적으로 HTML, CSS, JavaScript로 작성됨
- flat page라고도 함



### Dynamic web pate (동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
- 서버 사이드 프로그래밍 언어(Python, Java, C++등) 가 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



### Frmaework

- 프로그래밍엣 ㅓ특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework 라고도 함



### Web framework

- `웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는것이 주 목적`으로 데이터베이스 연동, 템플릿 형태의 표준, 세션관리, 코드 재사용등의 기능을 포함
- 동적인 웹 페이지나 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 application framework의 일종



### Framework Architecture

- MVC Design Pattern (model - view - controller)
- Django는 MTV Pattern 이라고 함



### MTV Pattern **

- Model (데이터베이스를 관리)
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  - MVC Pattern에서 model
- Template (인터페이스, 화면)
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는데 사용(presentation)
  - MVC Pattern에서 view
- View (중심 컨드롤러)
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template 에게 응답의 서식 설정을 맡김
  - MVC Pattern에서 controller



### Django

####  프로젝트 구조

- 생성 : django-admin startproject  __(pjt_name)__ .
  - 프로젝트 이름에는 -(하이픈) 사용 불가능

- urls.py
  - 사이트의 url과 적절한 views의 연결을 지정

#### Application

- 생성 : python manage.py startapp __app_name__(복수형)
  - 일반적으로 application명은 복수형으로 하는것을 권장
- application 구조
  - models.py
    - 앱에서 사용하는 Model을 정의하는곳
  - views.py
    - view 함수들이 정의 되는 곳

#### Project & Application

- Project
  - Project는 Application의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역활을 담당
  - 하나의 프로젝트는 여러 앱을 가짐
  - 일반적으로 앱은 하나의 역활 및 기능 단위로 작성함



## Django Templates

### Django Template Language(DTL)

- Django template에서 사용하는 built-in-template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- 단순히 Python이 HTML에 포함 된 것이 아니며, 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
  - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만, 이것이 해당 Python 코드로 실행된느것이 아님



### DTL Syntax

1. Variable      {{ variable }}
   - render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는것
   - 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
   - dot(.)을 사용하여 변수 속성에 접근할 수 있음
   - render()의 세번째 인자로 {'key' : value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨 보통 우리는 context형태로 만들어서 넘겨주었음

2. Filters       {{ variable|filter }}
   - 표시할 변수를 수정할 때 사용
   - ex)     name 변수를 모두 소문자로 출력 ->   {{ name|lower }}

3. Tags               {% tag %}
   - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
   - 일부 태그는 시작과 종료 태그가 필요 {% if %}{% endif %}   {% for %}{% endfor %}

4. Comments  {#      #}
   - Django templates에서 라인의 주석을 표현하기 위해 사용
   - 여러 줄 주석은 {% comment %}{% endcomment %} 사이에 입력



### 코드 작성 순서 **

- 데이터의 흐름에 맞추어 작성
- urls.py - views.py - tempates



### Tempate inheritance(템플릿 상속)

- Template inheritance - "tags"            
  - {% extends ' ' %}
    - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
    - `반드시 템플릿 최상단에 작성 되어야 함`
  - {% block content %}       {% endblock content %}
    - 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
    - 즉, 하위 템플릿이 채울 수 있는 공간
- Template Tag - "include"
  - {% include ' ' %}
    - 템플릿을 로드하고 현재 페이지로 렌더링
    - 템플릿 내에 다른 템플릿을 "포함(including)" 하는 방법

### Django template system (feat. Django 설계 철학)

- 표현과 로직(view)을 분리
  - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다.
  - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야한다
- 중복을 배제
  - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 가짐
  - djano 템플릿 시스템은 이러한 요소를 한곳에 저장하기 쉽게하여 중복 코들르 없애야한다
  - 이것이 템플릿 상속의 기초가 되는 철학이다





## HTML Form

### HTML "form" element

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역활을 담당
- 핵심 속성(attribute)
  - action : 입력 데이터가 전송될 URL 지정
  - method : 입력 데이터 전달 방식 지정



### HTML "input" element

- 사용자로부터 데이터를 입력 받기 위해 사용
- type 속성에 따라 동작 방식이 달라짐
- 핵심 속성(attribute)
  - name
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
  - GET 방식에서는 URL에서 ?key=value&key=value 형식으로 데이터를 전달함



### HTML "label" element

- 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄
- label을 input요소와 연결하기
  1. input에 id 속성 부여
  2. label에는 input의 id와 동일한 값의 for 속성 필요
- label과 input 요소 연결의 주요 이점
  - 시각적인 기능 뿐만 아니라 화면 리더기에서 label을 읽어 사용자가 입력해야 하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점도 있음
  - label을 클릭해서 input에 초점(focus)를 맞추거나 활성화(activate) 시킬 수 있음



### HTML "for" attribute

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어
  - 연결 된 요소가 labelable element인 경우 이 요소에 대한 labelable control이 됨
- "labelable elements"
  - label 요소와 연결할 수 있는 요소
  - button, input(not hidden type), select, textarea



### HTML "id" attribute

- 전체 문서에서 고유(must be unique)해야 하는 식별자를 정의
- 사용 목적
  - linking, scriptiong, styling 시 요소를 식별



### HTTPS request method - "GET"

- 서버로부터 `정보`를 `조회`하는데 사용
- 데이터를 가져올 때만 사용해야함
- 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송
- 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데, 이때 사용하는 요청의 방식이 GET



### Django URLs

- Dispatcher(발송자, 운항 관리자)로서의 URL
- 웹 애플리케이션은 URL을 통한 클라ㅣㅇ언트의 요청에서부터 시작 됨



### Variable Routing

- URL 주소를 변수로 사용하는 것
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
- 사용 예시
  - path('accounts/user/`<int: user_pk>`/',........)
    - accounts/user/1 -> (1번 user 관련 페이지)
    - accounts/user/2 -> (2번 user 관련 페이지)



### App URL mapping

- app의 view 함수가 많아지면서 사용하는 path()또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 이제는 각 app에  urls.py를 작성 
