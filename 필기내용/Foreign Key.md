## Foreign Key

### Foreign Key 개념

- 외래 키
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 속성(필드)에 해당하고 이는 참조되는 테이블의 기본키(primary key)를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응됨
  - 이 때문에 참조하는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조할 수 없음
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음



### Foreign Key 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
- `외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함`



- [참고] 참조 무결성
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
  - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함



### ForeignKey field

- 1:N 관계
- 2개의 위치 인자가 `반드시` 필요
  - 참조하는 모델 클래스
  - on_delete 옵션
- migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만듦



### ForeignKey arguments - 'on_delete'

- 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어째 처리할 지
- 이것은 데이터 무결성을 위해서 매우 중요하다
- on_delete 옵션에 사용 가능한 값들
  - CASCADE :
  - PROTECT
  - SET_NULL
  - SET_DEFAULT
  - SET()
  - DO_NOTHING
  - RESTRICT



### [참고] 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것을 가리키며, 데이터베이스나 RDBMS 시스템의 중요한 기능임
- 무결성 제한의 유형
  - 개체 무결성(Entity integrity)
    - pk의 개념과 관련
    - 모든 테이블이 PK를 가져야 하므로 PK로 선택된 열은 고유한 값이어야 하고 빈 값은 허용치 않음을 규정
  - 참조 무결성(Referential integrity)
    - FK(외래 키) 개념과 관련
    - FK 값이 데이터베이스의 특정 테이블의 PK값을 참조하는 것
  - 범위(도메인) 무결성(Domain integrity)
    - 정의된 형식(범위)에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정



### 데이터베이스의 ForeignKeyField 표현

- 만약 ForeignKey 인스턴스를 abcd로 생성 했다면 abcd_id로 만들어짐
- 하지만 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 바람직함(1:N)





### 1:N 관계 related manager

- 역참조(`'commnet_set'`)
  - Article(1) -> Comment(N)
  - `article.comment` 형태로는 사용할 수 없고, `article.comment_set` manager가 생성됨
  - 게시글에  몇 개의 댓글이 작성 되었는지 Django ORM이 보장할 수 없기 때문
    - article은 comment가 있을 수도 있고, 없을 수도 있음
    - 실제로 Article 클래스에는 Comment 와의 어떠한 관계도 작성되어 있지 않음



- 참조(`'article'`)
  - Comment(N) -> Article(1)
  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로, `comment.article`과 같이 접근할 수 있음
  - 실제 ForeignKeyField 또한 Comment 클래스에서 작성됨



- dir()함수를 통해서 dir(article)을 해서 article 인스턴스가 사용할 수 있는 모든 속성, 메소드를 직접 확인하기 --> `'comment_set'` 이 있다.
- article의 입장에서 모든 댓글 조회하기(역참조, 1-> N)       `article.comment_set()`
- `comments = article.comment_set.all()` 조회한 모든 댓글 출력하기 모든 댓글이니까 0개일 수도 1개일수도 여러개일 수도 있다 소문자 복수형으로 작성하나 그래서/???
- comment 입장에서 참조하는 게시글 조회하기 (참조, N->1)

```python
comment = Comment.objects.get(pk=1)

comment.article
>>> <Article: title>
comment.article.content
>>> 'content'
comment.article_id
>>> 1
```



### THE 'save()' method :star::star::star::star::star::star:

- save(commit=False)
  - Create, but don't save the new instance
  - `아직 데이터베이스에 저장되지 않은 인스턴스를 반환`
  - 저장하기 전에 `객체에 대한 사용자 지정 처리를 수행할 때` 유용하게 사용



### User 모델 대체하기

- 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
  - ex) username 대신 email을 식별 토큰으로 사용하는 것이 더 적합한 사이트
- Django는 User를 참조하는데 사용하는 AUTH_USER_MODEL 값을 제공하여, default user model을 재정의(override)할 수 있도록 함
- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장
  - 단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함



### AUTH_USER_MODEL

- User를 나탄내는데 사용하는 모델
- 프로젝트가 진행되는 동안 변경할 수 없음
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함
- 기본값 : 'auth.User' (auth 앱의 User 모델)



### Custom User 모델 정의하기

- 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스인 AbstractUser를 상속받아 새로운 User 모델 작성

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser)
```

​	