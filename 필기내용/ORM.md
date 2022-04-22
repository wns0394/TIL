## ORM

```python
# 모든 user 레코드 조회
User.objects.all()

# user 레코드 생성
User.objects.create(first_name='길동', last_name='홍', age=100, country='제주도', phone='010-1234-1231', balance=10000,)
>>> <User: User object (101)>
```