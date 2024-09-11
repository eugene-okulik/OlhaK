# Библиотека
# Первый класс
# Создайте класс book с атрибутами:
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

class Books:
    material = 'бумага'
    text_presence = 'yes'

    def __init__(self, name, author, page_amount, reservation):
        self.name = name
        self.author = author
        self.page_amount = page_amount
        self.reservation = reservation


book_1 = Books('Капитанская дочка', 'Пушкин', 200, True)
book_2 = Books('Идиот', 'Достоевский', 100, False)
book_3 = Books('Сказка о золотом петушке', 'Пушкин', 20, False)
book_4 = Books('Кобзар', 'Шевченко', 350, False)
book_5 = Books('Катерина', 'Шевченко', 230, True)
print(f'Название: {book_1.name}, Автор: {book_1.author}, страниц: {book_1.page_amount}, материал: {book_1.material},'
      f' зарезервирована')
print(f'Название: {book_2.name}, Автор: {book_2.author}, страниц: {book_2.page_amount}, материал: {book_2.material}')
print(f'Название: {book_3.name}, Автор: {book_3.author}, страниц: {book_3.page_amount}, материал: {book_3.material}')
print(f'Название: {book_4.name}, Автор: {book_4.author}, страниц: {book_4.page_amount}, материал: {book_4.material}')
print(f'Название: {book_5.name}, Автор: {book_5.author}, страниц: {book_5.page_amount}, материал: {book_5.material}, '
      f'зарезервирована')


class ShoolBooks(Books):
    def __init__(self, name, autor, page_amount, reservation, subject, school_class, tasks):
        super().__init__(name, autor, page_amount, reservation)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def reserve(self):
        reservation = True
        print(reservation)


school_book_1 = ShoolBooks('Aлгебра', 'Иванов', 200, False, 'Математика', 9, True)
school_book_2 = ShoolBooks('История Украины', 'Носов', 200, False, 'История', 8, False)
school_book_3 = ShoolBooks('География Европы', 'Шевченко', 200, False, 'География', 5, True)
school_book_1.reserve()
print(f'Название: {school_book_1.name}, Автор: {school_book_1.author}, страниц: {school_book_1.page_amount}, '
      f'предмет: {school_book_1.subject}, класс: {school_book_1.school_class}, зарезервирована')
print(f'Название: {school_book_2.name}, Автор: {school_book_2.author}, страниц: {school_book_2.page_amount}, '
      f'предмет: {school_book_2.subject}, класс: {school_book_2.school_class}')
print(f'Название: {school_book_3.name}, Автор: {school_book_3.author}, страниц: {school_book_3.page_amount}, '
      f'предмет: {school_book_3.subject}, класс: {school_book_3.school_class}')
