# Django 02

## Django Model

### Model

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)

- Django는 model을 통해 데이터에 접속하고 관리
- **일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨**



### Database

- 데이터베이스(DB)
  - 체계화도니 데이터의 모임
- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - "Query를 날린다." -> DB를 조작한다.



### Database의 기본 구조

- 스키마(Schema)
  - 데이터베이스에서 자료의 구조,표현방법, 관계 등을 정의한 구조(structure)
  - ![image-20220416121557998](C:\Users\qowns\AppData\Roaming\Typora\typora-user-images\image-20220416121557998.png)
- 테이블(Table)
  - 열(column) : 필드(field) or 속성
  - 각 열에는 고유한 데이터 형식이 지정된다. INTEGER, TEXT, NULL 등
  - 행(row) : 레코드(record) or 튜플
  - 테이블의 데이터는 행에 저장된다. 즉, user 테이블에 4명의 고객정보가 저장되어 있으며, 행은 4개가 존재
  - PK(기본키) : 각 행(레코드)의 고유값으로 PRIMARY KEY로 불린다.`반드시 설정하여야 하며`데이터베이스 관리 및 관계 설정시 주요하게 활용된다.
  - ![image-20220416121607536](C:\Users\qowns\AppData\Roaming\Typora\typora-user-images\image-20220416121607536.png)



### Model 정리

- "웹 애플리케이션의 데이터를 `구조화`하고 `조작`하기 위한 도구"
- 우리가 데이터 베이스에 관한 구조를 만들게 될것인데 그것을 모델 클래스를 통해서 진행
- 중요한거는 모델 클래스 하나가 데이터베이스 테이블 하나에 매핑되었다



## ORM

### ORM 객체 지향 매핑

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어(우리는 파이썬)를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL) 데이터를 변환하는 프로그래밍 기술
- OOP 프로그래밍에서 RDBMS을 연동할 때 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용함



데이터베이스와 웹 어플리케이션이 소통을 SQL로 할 수 없기 때문에 우리는 Django ORM을 사용

우리는 파이썬을 사용하고 ORM이라는 도구가 그것을 SQL로 해석하고 SQL로 다시 오는것을 다시 파이썬 언어로 바꾸어 준다

​								 										<--- Queryset API 문법에 근거하여 요청을 보냄

SQL statement   <------>     ORM <-------------------------------------------------->Python Object 

​															       Object, queryset -------> 객체로 주거나 쿼리셋 형태로 준다



### ORM의 장점과 단점

- 장점
  - `생산성` !!!!!!1
  - SQL을 잘 알지 못해도 DB 조작이 가능
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는것 (**생산성**)



### ORM 사용하는 이유

**"우리는 DB를 객체(object)로 조작하기 위해서 ORM을 사용한다"**



### models.py

```python
#articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

- 클래스 형태로 작성
- 상속을 받음 (models.Model) 즉 서브 클래스로 표현 -> models 모듈에 Model이라는 클래스가 있다.
- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  - django.db.models 모듈의 Model 클래스를 상속 받음
- models 모듈을 통해 어떠한 타입의 DB컬럼을 정의할 것인지 정의
  - title과 content는 모델의 필드를 나타냄
  - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열과 매핑
- id는 별도로 작성하지 않는다 -> django가 알아서 하기 때문에  



## Migrations

### Migrations

- "Django가 model에 생긴 변화를 반영하는 방법"
- Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어
  - makemigrations
  - migrate
  - sqlmigrate
  - showmigrations



### Migrations Commands

1. makemigrations
   - model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용 
   - 모델에 변경사항이 있으면 반드시 새로운 설계도를 만들어야한다.
2. migrate
   - 마이그레이션을 DB에 반영하기 위해 사용
   - `설계도를 실제 DB에 반영하는 과정`
   - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

3.  sqlmigrate
   - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
   - 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음
4. showmigrations
   - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
   - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있음



### model 수정

추가 필드 작성하면 makemigrations 진행

무슨 1) 이랑 2) 창이 뜬다. 이거는 이미 테이블이 존재하는데 이만큼 더 붙이려고 한다 

그러면 원래 테이블에 대한 기본값은 어찌할거냐????

이럴경우 1)은 그냥 장고가 추천하는 기본값 2)은 나가서 내가 직접 작성

우리는 보통 1을 선택한다

이러거 하다면 migrate해준다.



### 반드시 기억해야 할 migration 3단계

1. models.py 변경사항 발생 시
2. makemigrations 해주기 - 설계도 만들기
3. migrate해주기 - DB에 반영해주기



## Database API (중요)

그래서 우리가 데이터베이스랑 어떻게 소통할건데????

 데이터베이스를 조작하기 위한 도구 --> 이게 장고에서는 DB API라 한다



### DB API 구문 - Making Queries

Article.objects.all()

class name.Manager.QuerySetAPI



### DB API

- Manager
  - 보통 django 모델 클래스에 objects라는거 사용
- QuerySet
  - 데이터베이스로 부터 전달받은 객체 목록
  - queryset 안에는 없을수도 있고 1개 혹은 여러 개일 수 있다
  - 이것을 사용해서 조회 필터 정렬 등 가능하다 



## CRUD

객체 





### READ

- QuerySet API method를 사용해 다양한 조회를 하는것이 중요
- QuerySet API method는 크게 2가지로 분류
  - 새로운 쿼리셋을 받는거
  - 쿼리셋을 받지 않는거 ---> 이런게 있었나??? ---> get()



- all() -> 전체 쿼리셋 반환
- get() - >  쿼리셋을 주지 않음, 객체를 반환한다.





## redirect

- 새 URL로 요청을 다시 보내는 것





### crate하는데 3가지 방법이 있는데 우리가 2번째 방법을 선택한 이유

```python
# 1
article = Article()
article.title = title
article.content = content
article.save()

# 2
article = Article(title=title, content=content)
article.save()

# 3
Article.objects.create(title=title, content=content)
```

- 3번이 1줄이고 더 좋지 않냐????
- 왜 2번째 방식을 하는가??? ----->>> 유효성검사를 위해서
- 3번은 유효성 검사를 하기 위해 코드를 작성할 그게 없다
- 2번은 save 하기 전에 유효성 검사를 할 수있다.



- DTL (django template langauge)
- {{ }} -> 얘는 변수 출력이런 형식이거나 {% %}---> 태그 뭐 이런 형식애들
- order_by('-pk')라는 쿼리셋을 사용하여서 내림차순으로 진행
