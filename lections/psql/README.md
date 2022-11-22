# hello
* hello
> hello
```py
def hello(a, b):
    # print(a,b)
```
```sql
-- create database test;
```

*hello*
**hello**

# Slash commands

* \c - показывает к какой базе данных мы подключены и через какого юзера
* \c name_of_db - подключаемся к этой базе данных(бд)
* \q - выход из субд (система управления базами данных) (psql)
* \l - список всех бд
* \dt - показывает список таблиц в текущей бд
* \du - поквзывает список юзеров с их правами
* \d+ - показывает более подробную инфо о таблицах
* \d+ name_of_table - показывает более подробную инфо о таблице

# Создание баз данных и таблиц
```sql
CREATE DATABASE name_of_db;
-- создает базу данных
```
```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создает таблицу с полями
```
```sql
* DROP TABLE name_of_table; 
-- - удаляет таблицу
```
```sql
DROP DATABASE name_of_db;
-- удаление бд
```

# Заполнение таблиц

```sql
INSERT INTO name_of_table VALUES(val1,val2),
(val2.1,val2.2);
-- запись данных в таблицу(заполнение всех полей)
```
```sql
INSERT INTO name_of_table (column1,column2) VALUES
(val1.1, val1.2),
(val2.1, val2.2);
-- запись определенных полей в таблицу
```
# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- получение всех записей с таблицы(всех полей)
```
# Удаление записей из таблицы
```sql
DELETE FROM name_of_table;
-- удаление всех записей из таблицы
```

# Обновление записей в таблице
```sql
UPDATE name_of_table SET column = new_val;
-- обновление всех записей в таблице
UPDATE name_of_table SET column = new_val WHERE id < 10;
-- обновление нескольких записей
```


# Условия
```sql
DELETE FROM name_of_table WHERE column1 = value1;
-- удаление всех записей, соответствующих этому условию
```
```sql
SELECT * FROM name_of_table WHERE column1 like '%world%'
-- в данном случае выбирает все записи, у которых в поле title есть названия, содержащие слово "word"
-- hello world
-- world
-- world hello
-- like - чувствителен к регистру (World - не пройдет)
```
```sql
SELECT * FROM name_of_table WHERE column1 ilike '%world%'
-- в данном случае выбирает все записи, у которых в поле title есть названия, содержащие слово "word"
-- WORLD
-- World
-- worLD
-- Hello WORLD hello
-- hello world
-- world
-- world hello
-- ilike - не чувствителен к регистру
```
```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка по определенному полю(по умолчанию сортирует по возрастанию asc)
```
```sql
SELECT * FROM name_of_table ORDER BY column1 DESC;
-- сортировка по определенному полю(сортирует по убыванию desc)
```
```sql
SELECT * FROM name_of_table LIMIT 10;
<!-- выводит первые 10 записей) -->
```
```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускает первые 10 записей
```
```sql
SELECT * FROM name_of_table LIMIT 5 OFFSET 10;
-- пропускает первые 10 записей, выбирает следующие 5 записей
```
```sql
SELECT * FROM name_of_table WHERE column1 ~* '%word%'
```
<!-- ~* находит во всех регистрах -->
<!-- ~ находит только в нижнем регистре -->

# Связи
## pk fk
> **primary key (pk)** - первичный ключ, ограничение, которое накладывается на поле, которое будет использоваться в связях (создает btree для быстрого поиска)
> **foreign key (fk)** - внешний ключ, ограничение, которое накладывается на поле, которое ссылается на первичный ключ (pk) в другой таблице

```sql
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR (50),
);
CREATE TABLE book(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    published YEAR,
    author_id INT,

    CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author (id)
);
```
## Виды связей
> One to one - один к одному
* один пользователь - одна почта
* один человек - один ID
* один автор - одна автобиография

> One to many - один ко многим
* один блогер - много постов
* один куратор - много студентов
* один продукт - много комментариев

> Many to many - многие ко многим
* один ментор - много студентов. один студент - много менторов
* один разработчик - много проектов. один проект - много разработчиков
* один банк - много клиентов. один клиент - много банков

## Виды связей(практика)
### One to one
```sql
create table author (
    id serial primary key,
    name varchar(50),
    age int
);
create table autobiography (
    id serial primary key,
    body text,
    created_at date,
    author_id int unique, --unique мы ставим, чтобы сделать o2o (one to one)
    constraint fk_author_bio foreign key (author_id) references author(id)
);
```
### One to many
```sql
create table curator (
    id serial primary key,
    name varchar (50)
);
create table student (
    id serial primary key,
    name varchar (50),
    email varchar(100),
    language varchar (2),
    curator_id int,
    constraint fk_student_curator foreign key (curator_id) references curator (id)
);
```
### Many to many
```sql
create table developer (
    id serial primary key,
    name varchar (50),
    experience int
);

create table project (
    id serial primary key,
    title varchar (50),
    tz text,
    start date,
    finish date
);
create table dev_proj (
    dev_id int,
    proj_id int,
    constraint fk_dev foreign key (dev_id) references developer (id),
    constraint fk_proj foreign key (proj_id) references project (id)
);
```
## Joins
> **JOIN** - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц

> **INNER JOIN (JOIN)** - достаются только те записи, у которых есть связь

> **FULL JOIN**  - достаются абсолютно все записи с обеих таблиц

> **LEFT JOIN (LEFT OUTER JOIN)** - достаются все записи с левой таблицы, и с левой таблицы, у которых есть связь с левой таблицей

> **RIGHT JOIN (RIGHT OUTER JOIN)** - достаются все записи с правой таблицы, и с левой таблицы, у которых есть связь с правой таблицей

> где "левая" таблица - та, которая написана до join
> а "правая" таблица - та, которая написана после join



# Практика
```sql

-- создание таблиц

CREATE TABLE blogger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    blogger_id INT,
    body TEXT,
    created_at DATE,

    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);

-- заполнение таблиц

INSERT INTO blogger (name) VALUES ('blogger 1'), ('blogger 2'), ('blogger 3'); 

INSERT INTO post (blogger_id, body, created_at) VALUES
(1, 'my first blog', '01.08.2020'),
(1, 'today is a good day', '02.09.2020'),
(1, 'it is my b-day!', '30.09.2021');

INSERT INTO post (blogger_id, body, created_at) VALUES
(2, 'my first post', '10.05.2013'),
(2, 'some post', '23.06.2022');

INSERT INTO post (blogger_id, body, created_at) VALUES
(3, 'i am not a blogger', '15.08.2022');
```

## shop
```sql
-- создание таблиц

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    price DECIMAL
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id), 
    CONSTRAINT cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);
-- заполнение таблиц
INSERT INTO customer (name) VALUES ('customer 1'), ('customer 2'), ('customer 3'); 

INSERT INTO product (title, price) VALUES
('product 1', 340),
('product 2', 503),
('product 3', 470),
('product 4', 236),
('product 5', 452);

INSERT INTO cart (customer_id, product_id) VALUES
(1, 1), (1, 2), (1, 4),
(2, 3),
(3, 4), (3, 5);
```

# Агрегатные функции
> SUM  - функция, считающая сумму всех записей в сгруппированном поле
```sql
-- пример из shop
SELECT customer.name, SUM(product.price) AS total_price
FROM product JOIN cart ON product.id = cart.product_id
JOIN customer ON customer.id = cart.customer_id
GROUP BY (customer.name);
--     name    | total_price 
-- ------------+-------------
--  customer 2 |         470
--  customer 3 |         688
--  customer 1 |        1079
-- (3 rows)

```
> ARRAY_AGG - объединяет записи сгруппированного поля в массив
```sql
-- пример из blog
SELECT blogger.name, ARRAY_AGG(post.body) AS posts
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    |                           posts                           
-- -----------+-----------------------------------------------------------
--  blogger 2 | {"my first post","some post"}
--  blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
--  blogger 3 | {"i am not a blogger"}
-- (3 rows)

```
> MIN, MAX - высчитывает минимальное и максимальное значение срези записей в сгруппированном поле

```sql
SELECT blogger.name, MIN(post.created_at) AS first,
MAX(post.created_at) AS last
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    |   first    |    last    
-- -----------+------------+------------
--  blogger 2 | 2013-05-10 | 2022-06-23
--  blogger 1 | 2020-08-01 | 2021-09-30
--  blogger 3 | 2022-08-15 | 2022-08-15
-- (3 rows)

```
> COUNT - считает количество записей в сгруппированном поле
```sql
-- пример из  blog
SELECT blogger.name, COUNT (post.id) AS posts_count 
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    | posts_count 
-- -----------+-------------
--  blogger 2 |           2
--  blogger 1 |           3
--  blogger 3 |           1
-- (3 rows)

```
# Изменение таблиц
```sql
ALTER TABLE name_of_table ADD COLUMN col_name type constraint;
-- добавляет новую колонку в таблицу
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляет колонку из таблицы
```

```sql
ALTER TABLE name_of_table ADD CONSTRAINT constr_name constraint;
-- добавление ограничения на поле
ALTER TABLE test ADD CONSTRAINT col_unq UNIQUE(col); -- example
--test - название таблицы
--col - название поля
ALTER TABLE test ADD CONSTRAINT fk_test_test2 FOREIGN KEY (test2_id) REFERENCES test2 (id);
```

```sql
ALTER TABLE name_of_table RENAME COLUMN old_name TO new_name;
-- переименовать поле
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_data_type;

ALTER TABLE name_of_table ALTER COLUMN col_name TYPE new_data_type;
-- измененение типа данных у поля
```
# Import / export баз данных

write from file to db
```bash
psql db_name < file.sql
# db_name должна существовать в postgresql
```

write from db to file
```bash
pg_dump db_name > file.sql
```
