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

from abc import abstractmethod


class Books:
    material = 'бумага'
    text_presence = 'yes'

    def __init__(self, name, author, page_amount, reserve):
        self.name = name
        self.author = author
        self.page_amount = page_amount
        self.reserve = reserve

    @abstractmethod
    def book_reserve(self):
        pass

    @abstractmethod
    def book_print(self):
        if self.reserve:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_amount}, '
                  f'материал: {self.material},'f' зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_amount}, '
                  f'материал: {self.material}')


book_1 = Books('Капитанская дочка', 'Пушкин', 200, True)
book_2 = Books('Идиот', 'Достоевский', 100, False)
book_3 = Books('Сказка о золотом петушке', 'Пушкин', 20, False)
book_4 = Books('Кобзар', 'Шевченко', 350, False)
book_5 = Books('Катерина', 'Шевченко', 230, True)
book_1.book_print()
book_2.book_print()
book_3.book_print()
book_4.book_print()
book_5.book_print()


class ShoolBooks(Books):
    def __init__(self, name, autor, page_amount, reserve, subject, school_class, tasks):
        super().__init__(name, autor, page_amount, reserve)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def book_reserve(self):
        self.reserve = True
        print(self.reserve)

    def book_print(self):
        if self.reserve:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_amount}, '
                  f'предмет: {self.subject}, класс: {self.school_class}, зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_amount}, '
                  f'предмет: {self.subject}, класс: {self.school_class}')


school_book_1 = ShoolBooks('Aлгебра', 'Иванов', 200, False, 'Математика', 9, True)
school_book_2 = ShoolBooks('История Украины', 'Носов', 200, True, 'История', 8, False)
school_book_3 = ShoolBooks('География Европы', 'Шевченко', 200, False, 'География', 5, True)
school_book_1.book_reserve()
school_book_1.book_print()
school_book_2.book_print()
school_book_3.book_print()
