import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# 1. Создайте студента (student):
cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Kostya', 'Koldun')")
student_id = cursor.lastrowid
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())
db.commit()

# 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Kobzar part3', student_id),
        ('Pyhon basics part3', student_id),
        ('API testing part3', student_id)
    ]
)
db.commit()

# 3. Создайте группу (group) и определите своего студента туда
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group_AP5C', 'sep 2024', 'sep 2025')")
group_id = cursor.lastrowid
cursor.execute(f'SELECT * from `groups` g where id = {group_id}')
cursor.fetchone()
db.commit()

cursor.execute(f'UPDATE students SET group_id = {group_id} where students.id = {student_id}')
cursor.execute(f'SELECT * from students where id = {student_id}')
print("Update the group for student")
print(cursor.fetchone())
db.commit()

# 4. Создайте несколько учебных предметов (subjects)
insert_query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    insert_query, [
        ('Python_basic part3',),
        ('Python_OOP part3',),
        ('Python_Automation part3',)
    ]
)
db.commit()
cursor.execute("SELECT id FROM subjets ORDER BY id DESC LIMIT 1")
subject_id_1 = cursor.fetchone()['id']
cursor.execute("SELECT id FROM subjets ORDER BY id DESC LIMIT 1, 1")
subject_id_2 = cursor.fetchone()['id']
cursor.execute("SELECT id FROM subjets ORDER BY id DESC LIMIT 2, 1")
subject_id_3 = cursor.fetchone()['id']

# 5. Создайте по два занятия для каждого предмета (lessons)
insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Valiables_types 3', subject_id_1),
        ('Loops 3', subject_id_1),
        ('Classes 3', subject_id_2),
        ('OOP_princeples 3', subject_id_2),
        ('Set up and start the browsers 3', subject_id_3),
        ('API testing 3', subject_id_3)
        ]
)
db.commit()
cursor.execute(f'SELECT * from lessons order by id desc limit 1')
lesson_id_1 = cursor.fetchone()['id']
cursor.execute(f'SELECT * from lessons order by id desc limit 1,1')
lesson_id_2 = cursor.fetchone()['id']
cursor.execute(f'SELECT * from lessons order by id desc limit 2,1')
lesson_id_3 = cursor.fetchone()['id']
cursor.execute(f'SELECT * from lessons order by id desc limit 3,1')
lesson_id_4 = cursor.fetchone()['id']
cursor.execute(f'SELECT * from lessons order by id desc limit 4,1')
lesson_id_5 = cursor.fetchone()['id']
cursor.execute(f'SELECT * from lessons order by id desc limit 5,1')
lesson_id_6 = cursor.fetchone()['id']

# 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

insert_query = "INSERT INTO marks (value, lesson_id , student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (10, lesson_id_1, student_id),
        (11, lesson_id_2, student_id),
        (12, lesson_id_3, student_id),
        (9, lesson_id_4, student_id),
        (8, lesson_id_5, student_id),
        (11, lesson_id_6, student_id)
    ]
)
db.commit()
# Получите информацию из базы данных:
# 1. Все оценки студента
cursor.execute(f'SELECT * FROM marks m WHERE student_id = {student_id}')
print("1. Все оценки студента:")
print(cursor.fetchall())

# 2. Все книги, которые находятся у студента

cursor.execute(f'SELECT * FROM books b WHERE taken_by_student_id = {student_id}')
print("2. Все книги, которые находятся у студента:")
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)
select_query = '''
SELECT s.name, s.group_id, b.title, sb.title, l.title, m.value
FROM students s
INNER JOIN books b ON s.id = b.taken_by_student_id
INNER JOIN marks m ON s.id = m.student_id
INNER JOIN lessons l ON m.lesson_id = l.id
INNER JOIN subjets sb ON sb.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(select_query, (student_id,))
print("Для вашего студента выведите всё, что о нем есть в БД: группа, книги, оценки с названиями занятий и предметов:")
print(cursor.fetchall())
db.commit()
db.close()
