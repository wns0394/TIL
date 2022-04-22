# REST API

### HTTP

- Hyper Text Transfer Protocol
- 웹상에서 전송할 때 리소스를 전송하기위한 약속
- 웹에서 이루어지는 모든 데이터 교환의 기초
  - 요청(request)
    - 클라이언트에 의해 전송되는 메세지
  - 응답(response)
    - 서버에서 응답으로 전송되는 메세지
- 기본 특성
  - Stateless 무상태
  - Connectionless 비연결성
- 이러한 특성을 해결하기위해 쿠키와 세션을 배움
- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



#### HTTP request methods

- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
- HTTP Method 예시
  - GET(조회), POST(작성), PUT(수정), DELETE(삭제)



#### URL, URN

- URL(Uniform Resource Locator)
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디에 있는지 알려주기 위한 약속
  - 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
  - '웹주소', '링크' 라고도 불림

- URN(Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역활을 함

- 예를 들면 멀티 캠퍼스가 있다 이게 주소가 역삼인데 이전해서 잠실에 있다하면
- 위치(URL)은 변경되었지만 이름(URN)은 그대로이다
- 우리는 보통 주소를 사용한다



#### URl

- Uniform Resource ldentifier
- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소(`정보의 자원을 표현`)
- 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 단단한 문자열



- URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함







###  RESTful API

### REST

- REpresentational State Transfer
- API Sever를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 규약이나 약속은 아니다



- REST의 자원과 주소의 지정 방법
  1. 자원
     - URI
  2. 행위
     - HTTP Method
  3. 표현
     - 자원과 행위를 통해 궁극적으로 표현되는(추상화된)결과물
     - JSON으로 표현된 데이터를 제공
- - 자원에 대한 주소는 URL로 표기하고 URL를 통한 행위는 HTTP Method를 통해서 결정하고 그거에 대한 응답 데이터는 JSON으로 표현할것이다



### Serialization

serializer해주는게 단일객체면 many 옵션이 필요없지만 queryset이나 그런것들은 many=True 옵션을 추가해주어야지 에러가 안뜬다



- JSON 방법으로 주는 첫번째 방법

```python
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)
```

에서 JsonResponse는 값으로 articles_json를 넣어주는데 이거는 리스트다. 여기에 데이터는 반복문으로 각각의 값을 딕셔너리로 append되고있다.



- 두번째 방법