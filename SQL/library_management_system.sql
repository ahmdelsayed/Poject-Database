-- 1. جدول الكتب
CREATE TABLE L_books (
    book_id     NUMBER PRIMARY KEY,
    title       VARCHAR2(100) NOT NULL,
    author      VARCHAR2(50),
    category    VARCHAR2(30),
    price       NUMBER(8, 2)
);

INSERT INTO L_books (book_id, title, author, category, price) 
VALUES (101, 'DataBase Basics', 'Ahmed Mahmoud', 'Technology', 150.50);

INSERT INTO L_books (book_id, title, author, category, price) 
VALUES (102, 'Learn SQL', 'Sara ALi', 'Technology', 220.00);

INSERT INTO L_books (book_id, title, author, category, price) 
VALUES (103, 'History of the Middle East', 'Mohamed Hassan', 'History', 90.00);

INSERT INTO L_books (book_id, title, author, category, price) 
VALUES (104, 'Java', 'Khaled Abdallah', 'Technology', 180.75);

INSERT INTO L_books (book_id, title, author, category, price) 
VALUES (105, 'Modern Psychology', 'Mona Farouk', 'Human sciences', 110.00);


-- 2. جدول الأعضاء
CREATE TABLE L_members (
    member_id   NUMBER PRIMARY KEY,
    full_name   VARCHAR2(50) NOT NULL,
    join_date   DATE DEFAULT SYSDATE,
    phone       VARCHAR2(15)
);

INSERT INTO L_members (member_id, full_name, join_date, phone) 
VALUES (1, 'Ahmed Hassan', TO_DATE('15-01-2025', 'DD-MM-YYYY'), '01012345678');

INSERT INTO L_members (member_id, full_name, join_date, phone) 
VALUES (2, 'Mariam Ali', TO_DATE('10-03-2025', 'DD-MM-YYYY'), '01123456789');

INSERT INTO L_members (member_id, full_name, join_date, phone) 
VALUES (3, 'Omar Ibrahim', TO_DATE('05-05-2025', 'DD-MM-YYYY'), '01234567890');

INSERT INTO L_members (member_id, full_name, join_date, phone) 
VALUES (4, 'Hana Mahmoud', TO_DATE('20-07-2025', 'DD-MM-YYYY'), '01543210987');


-- 3. جدول الاستعارات
CREATE TABLE L_borrows (
    borrow_id   NUMBER PRIMARY KEY,
    member_id   NUMBER,
    book_id     NUMBER,
    borrow_date DATE DEFAULT SYSDATE,
    return_date DATE,
    fine_amount NUMBER(6, 2),

    -- العلاقات
    CONSTRAINT fk_borrows_member 
        FOREIGN KEY (member_id) 
        REFERENCES L_members(member_id) 
        ON DELETE CASCADE,

    CONSTRAINT fk_borrows_book 
        FOREIGN KEY (book_id) 
        REFERENCES L_books(book_id) 
        ON DELETE CASCADE
);

INSERT INTO L_borrows (borrow_id, member_id, book_id, borrow_date, return_date, fine_amount) 
VALUES (501, 1, 101, TO_DATE('01-08-2026', 'DD-MM-YYYY'), TO_DATE('10-08-2026', 'DD-MM-YYYY'), 0);

-- حفظ التغييرات نهائياً في قاعدة بيانات أوراكل
COMMIT;



-- 1) إنشاء VIEW تعرض اسم العضو، عنوان الكتاب، وتاريخ الاستعارة

CREATE OR REPLACE VIEW v_borrow_details AS
SELECT 
    m.full_name,
    k.title,
    b.borrow_date
FROM L_borrows b
JOIN L_members m ON b.member_id = m.member_id
JOIN L_books k   ON b.book_id = k.book_id;

-- الاستعلام من الـ VIEW:
SELECT * FROM v_borrow_details;



-- 2) عرض بيانات الاستعارات مع استبدال غرامات الـ NULL بصفر باستخدام NVL

SELECT 
    borrow_id,
    member_id,
    book_id,
    borrow_date,
    return_date,
    NVL(fine_amount, 0) AS fine_amount
FROM L_borrows;



-- 3) تصنيف أسعار الكتب إلى فئات (High, Medium, Low) باستخدام CASE

SELECT 
    title,
    price,
    CASE 
        WHEN price >= 200 THEN 'High'
        WHEN price >= 100 AND price < 200 THEN 'Medium'
        ELSE 'Low'
    END AS price_category
FROM L_books;



-- 4) حساب عدد استعارات كل عضو وعرض من استعار أكثر من كتاب واحد

SELECT 
    m.member_id,
    m.full_name,
    COUNT(b.borrow_id) AS total_borrowed_books
FROM L_members m
JOIN L_borrows b ON m.member_id = b.member_id
GROUP BY m.member_id, m.full_name
HAVING COUNT(b.borrow_id) > 1;


--INSERT INTO L_borrows (borrow_id, member_id, book_id, borrow_date, fine_amount) 
--VALUES (502, 1, 102, SYSDATE, 0);
--COMMIT;


-- 5) عرض أسعار الكتب مقربة لأقرب رقم صحيح باستخدام ROUND

SELECT 
    title,
    price AS original_price,
    ROUND(price) AS rounded_price
FROM L_books;



-- 6) عرض تاريخ الاستعارة مقطوعاً منه الوقت باستخدام TRUNC

 SELECT 
    borrow_id,
    borrow_date AS full_date,
    TRUNC(borrow_date) AS date_without_time
FROM L_borrows;



-- 7) قائمة الكتب التي سعرها أعلى من متوسط سعر كل الكتب (Subquery)

SELECT 
    title,
    price
FROM L_books
WHERE price > (SELECT AVG(price) FROM L_books);
