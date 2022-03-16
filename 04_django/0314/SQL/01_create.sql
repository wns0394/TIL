-- SQLite
INSERT INTO classmates (name, age) VALUES('배준식', 26);

INSERT INTO classmates VALUES('홍길동', 30, '서울');

SELECT rowid, * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT  NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
)

INSERT INTO classmates (name, age, address) VALUES('배준식', 26, '부산');

CREATE TABLE classmates (
    name TEXT  NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
)

INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '경주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address = '서울';

SELECT DISTINCT age FROM classmates;