## Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 웹 페이지를 작성(구조화)하기 위한 언어



### HTML 기본구조

- html: 문서의 최상위 요소
- head: 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용



### head 예시

- `<title>` :  브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>`: 외부 리소스 연결 요소(CSS파일, favicon 등)
- `<script>`: 스크립트 요소(JavaScript 파일/코드)
- `<style>`: CSS직접 작성



### DOM(Document Object Model)트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드를 제공함
- 마크업 스타일 가이드(2 space)



### 요소(element)

- HTML 요소는 시작태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)을 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들( 닫는 태그가 필요없는애들)
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질  수 있음



### 속성

<a href(속성명)=(띄어쓰기 사용안함)"(쌍따옴표사용)https://google.com(속성값)"></a>

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Atrribute)들도 있음



### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
  - id: 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록
  - data-* : 페이지에 개인 사용자 정의 데이터를 지정하기 위해 사용
  - style: inline 스타일
  - title : 요소에 대한 추가 정보 지정
  - tabindex : 요소의 탭 순서



### 시맨틱 태그

- HTML5에서 의미론적으로 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
  - header: 문서 전체나 섹션의 헤더(머리말 부분)
  - nav: 내비게이션
  - aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer: 문서 전체나 섹션의 푸터(마지막 부분)

- Non semantic 요소는 div, span등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함





## CSS

스타일을 지정하기 위한 언어 선택하고 스타일을 지정한다

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성(Property) : 어떤 스타일 기능을 변경할지 결정
  - 값(Value) : 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인(inline)
- 내부 참조(embedding) - <style>
- 외부 참조(link file) - 분리된 CSS 파일



### 선택자(selector 유형)

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(combinations)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- 전체 선택자 *
- 요소 선택자 h2, h3, h4...
- 클래스 선택자 .green
- id 선택자 #purple
- 자식 결합자 .box > p
- 자손 결합자 .box p
- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용, 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



### CSS 적용 우선순위

- 1. 중요도(Importance) - 사용시 주의  !important
  2. 우선순위(Specificity)
     1.  인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
  3. CSS 파일 로딩 순서 



### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다
  - 상속 되는 것 예시
    - 예) Text 관련 요소(font, color, text-align), opacity,visibility 등
  - 상속 되지 않는 것 예시
    - 예)  Box model 관련 요소(width, height, margin, padding, border, box-sizing,display), position 관련 요소(position, top/right/bottom/left, z-index) 등



### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠 영역(디바이스 화면
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax



### 색상 단위

- 색상 키워드
  - 대소문자를 구분하지 않음
  - red, blue, black과 같은 특정 색을 직ㅈ접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식



### 결합자(Combinators)

- 자손 결합자 div span
  - selector A 하위의 모든 selector B 요소
- 자식 결합자 div > span
  - selector A 바로 아래의 selector B 요소
- 일반 형제 결합자 p ~ span
  - selector A의 형제 요소 중 뒤에 위치하는 selector B 요소를 모두 선택
- 인접 형제 결합자 p + span
  - selector A의 형제 요소 중 바로 뒤에 위치하는 selector B 요소를 선택



## Box model

모든 요소는 네모(박스모델)이고 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

- 모든 HTML 요소는 box 형태로 이루어짐

- 하나의 박스는 네 부분(영역)으로 이루어짐
  - content : 글이나 이미지 등 요소의 실제 내용
  - padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  - border : 테두리 영역
  - margin : 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.



### 영역 주는거

.margin-1 { margin: 10px;} --> 상하좌우 다 10px

.margin-2 { margin: 10px 20px;} --> 상하 10px 좌우 20px

.margin-3 { margin: 10px 20px 30px; } ---> 상10px 좌우 20px 하 30px **주의하기**

.margin-4 { margin : 10px 20px 30px 40px;} --> 시계방향으로 상 10px 우20px 하 30px 좌40px

border에도 shorthand가 있다



### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box으로 설정



### CSS display

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치
- display에 따라 크기와 배치가 달라진다.



### 대표적으로 활용되는 display

- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다



### 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분(HTML 4.1까지)
- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong 등



### block

- block의 기본 너비는 가질 수 있는 너비의 100%
- 너비를 가질 수 없담녀 자동으로 부여되는 margin



### inline

- inline의 기본 너비는 컨텐츠 영역만큼



### display

- display : inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display : none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표식만 하지 않는다.



### CSS position

- 문서 상에서 요소를 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative
  - absolute
  - fixed
- relative : 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음(normal position 대비 offset)
- absolute : 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
- fixed : 고정 위치
  -  요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤시에도 항상 같은 곳에 위치함



### CSS 원칙

-  CSS 원칙 1,2 : Normal flow
  - 모든 요소는 네모(박스모델), 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐
- CSS 원칙 3
  - position으로 위치의 기준을 변경
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치



### CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 구성 요소
  - Flex Container(부모 요소)
  - Flex Item (자식 요소)



### Flexbox 구성 요소

- Flex Container(부모 요소)
  - flexbox 레이아웃을 형성하는 가장 기본적인 모델
  - Flex Item 들이 놓여있는 영역
  - display 속성을 flex 혹은 inlin-flex로 지정
- Flex Item(자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)



### Flex 속성

- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - justify-content( main axis)
  - align-content (cross axis)
- 정렬
  - align-items ( 모든 아이템을 cross axis 기준으로)
  - align-self (개별 아이템)



### flex 속성 : flex-direction

- Main axis 기준 방향 설정
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의
- row, row-reverse, column, column-reverse



### flex 속성 : flex-wrap

- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
- wrap, nowrap



### flex 속성 : flex-direction & flex-wrap

- flex-direction : Main axis의 방향을 설정
- flex-wrap : 요소들이 강제로 한줄에 배치 되게 할 것인지 여부 설정
  - nowrap (기본값) : 한 줄에 배치
  - wrap : 넘치면 그 다음 줄로 배치
- flex-flow
  - flex-direction과 flex-wrap의 shorthand
  - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
  - 예시) flex-flow: row nowrap;



### flex 속성 : justify-content

- Main axis를 기준으로 공간 배분
- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly



### flex 속성 : align-content

- cross axis를 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인할 수 없음)
- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly



### flex 속성 : justify-content & align-content

- 공간 배분
- flex-start (기본 값) : 아이템들을 axis 시작점으로
- flex-end : 아이템들을 axis 끝 쪽으로
- center : 아이템들을 axis 중앙으로
- space-between : 아이템 사이의 간격을 균일하게 분배
- space-around : 아이템을 둘러싼 영역을 균일하게 분배 ( 가질 수 있는 영역을 반으로 나눠서 양쪽에)
- space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배



### flex 속성 : align-items

- 모든 아이템을 cross axis를 기준으로 정렬
- stretch (기본값) : 컨테이너를 가득 채움
- flex-start : 위
- flex-end : 아래
- center : 가운데
- baseline : 텍스트 baseline에 기준선을 맞춤



### flex 속성 : align-self

- 개별 아이템을 cross axis 기준으로 정렬
- 주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용



### flex에 적용하는 속성

- 기타 속성
  - flex-grow : 남은 영역을 아이템에 분배
  - order : 배치 순서



## Bootstrap

### CDN

- Content Delivery(Distribution) Network
- 컨텐츠(CSS, JS, Image, Text등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
- 개별 end-user의 가까운  서버를 통해 빠르게 전달 가능(지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐



### spacing

- .mt-1 {

    margin-top: 0.25rem !important;

  }

| class name | rem  |  px  |
| :--------: | :--: | :--: |
|    m-1     | 0.25 |  4   |
|    m-2     | 0.5  |  8   |
|    m-3     |  1   |  16  |
|    m-4     | 1.5  |  24  |
|    m-5     |  3   |  48  |

|  m   | margin  |
| :--: | :-----: |
|  p   | padding |

|  t   |     top     |
| :--: | :---------: |
|  b   |   bottom    |
|  s   |    left     |
|  e   |    right    |
|  x   | left, right |
|  y   | top, bottom |

|  0   |  0 rem   | 0px  |
| :--: | :------: | :--: |
|  1   | 0.25 rem | 4px  |
|  2   | 0.5 rem  | 8px  |
|  3   |  1 rem   | 16px |
|  4   | 1.5 rem  | 24px |
|  5   |  3 rem   | 48px |



### color

- primary 파란색
- secondary 회색
- success 초록색
- info 하늘?
- warning 노란색
- danger 빨강
- light 흰색
- dark 검정



### Grid system (web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - Column : 실제 컨텐츠를 포함하는 부분
  - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container : Column들을 담고 있는 공간
- Bootstrap Grid system은 flexbox로 제작됨
- container, rows, column으로 컨텐츠를 배치하고 정렬
- 반드시 기억해야 할 2가지 !
  -  12개의 column
  -  6개의 grid breakpoints









### ! important - Inline style - id 선택자 - class 선택자 - 요소 선택자 - 소스 선택자

