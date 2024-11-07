import mysql.connector as mysql
import csv
import os
import dotenv

dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
Lesson_16_path = os.path.dirname(os.path.dirname(homework_path))
hw_data_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(hw_data_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    csv_data = []
    for row in file_data:
        csv_data.append(row)
print("Content of the csv file: ")

for row in csv_data:
    print(row)
print("")

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
select_query = '''
    SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, sb.title AS subject_title,
    l.title AS lesson_title, m.value AS mark_value
    FROM students s
    INNER JOIN `groups` g ON s.group_id = g.id
    INNER JOIN books b ON s.id = b.taken_by_student_id
    INNER JOIN marks m ON s.id = m.student_id
    INNER JOIN lessons l ON m.lesson_id = l.id
    INNER JOIN subjets sb ON sb.id = l.subject_id
    '''
cursor.execute(select_query, ())
# print("Content of the Database: ")
db_data = cursor.fetchall()

# for row in db_data:
#     print(row)


def row_exists_in_db(row, db_data):
    for db_row in db_data:
        # Compare value with the same keys
        if all(row.get(key) == db_row.get(key) for key in row):
            return True
    return False


# List for missing data
missing_data = []
# Check which data is missing from the csv file in the database
for row in csv_data:
    if not row_exists_in_db(row, db_data):
        missing_data.append(row)


cursor.close()
db.close()

if missing_data:
    print("The following data is missing in the database:")
    for item in missing_data:
        print(item)
else:
    print("All data from the CSV file is present in the database.")
