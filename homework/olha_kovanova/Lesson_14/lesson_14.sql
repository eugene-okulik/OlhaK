-- Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
-- 1. Создайте студента (student)

SELECT * FROM students s WHERE name = 'Olga'
SELECT id FROM students s WHERE name = 'Olga'

INSERT INTO students (name, second_name) VALUES ('Olga', 'Petrova')

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

SELECT * FROM books b
SELECT * FROM books WHERE taken_by_student_id = 3453

INSERT INTO books (title, taken_by_student_id) VALUES ('Kobzar', 3453)
INSERT INTO books (title, taken_by_student_id) VALUES ('Pyhon basics', 3453)
INSERT INTO books (title, taken_by_student_id) VALUES ('API testing', 3453)

-- 3. Создайте группу (group) и определите своего студента туда

SELECT * FROM `groups` g
SELECT * FROM `groups` g WHERE title = 'Group_AP5B'

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group_AP5B', 'sep 2024', 'sep 2025')

UPDATE students SET group_id = 2151 WHERE students.id = 3453

-- 4. Создайте несколько учебных предметов (subjects)
SELECT * FROM subjets sb
SELECT * FROM subjets sb WHERE title = 'Python_basic' or title = 'Python_OOP' or title = 'Python_Automation'


INSERT INTO subjets (title) VALUES ('Python_basic')
INSERT INTO subjets (title) VALUES ('Python_OOP')
INSERT INTO subjets (title) VALUES ('Python_Automation')


-- 5. Создайте по два занятия для каждого предмета (lessons)

SELECT * FROM lessons l
SELECT  * FROM lessons l WHERE subject_id  = 3148 or subject_id  = 3149 or subject_id = 3150

INSERT INTO lessons (title, subject_id) VALUES ('Valiables_types', 3148)
INSERT INTO lessons (title, subject_id) VALUES ('Loops', 3148)

INSERT INTO lessons (title, subject_id) VALUES ('Classes', 3149)
INSERT INTO lessons (title, subject_id) VALUES ('OOP_princeples', 3149)

INSERT INTO lessons (title, subject_id) VALUES ('Set up and start the browsers', 3150)
INSERT INTO lessons (title, subject_id) VALUES ('API testing', 3150)

-- 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

SELECT * FROM marks m
SELECT * FROM marks m WHERE student_id  = 3453

INSERT INTO marks (value, lesson_id , student_id) VALUES (10, 6447, 3453)
INSERT INTO marks (value, lesson_id , student_id) VALUES (11, 6448, 3453)
INSERT INTO marks (value, lesson_id , student_id) VALUES (12, 6451, 3453)
INSERT INTO marks (value, lesson_id , student_id) VALUES (9, 6452, 3453)
INSERT INTO marks (value, lesson_id , student_id) VALUES (8, 6453, 3453)
INSERT INTO marks (value, lesson_id , student_id) VALUES (11, 6454, 3453)

-- Получите информацию из базы данных:
-- 1. Все оценки студента

SELECT  * FROM marks m WHERE student_id  = 3453

-- 2. Все книги, которые находятся у студента

SELECT * FROM books b WHERE taken_by_student_id = 3453

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
-- (всё одним запросом с использованием Join)

SELECT s.name, s.group_id, b.title, sb.title, l.title, m.value
FROM students s
INNER JOIN books b ON s.id = b.taken_by_student_id
INNER JOIN marks m ON s.id = m.student_id
INNER JOIN lessons l ON m.lesson_id = l.id
INNER JOIN subjets sb ON sb.id = l.subject_id
WHERE s.id = 3453
