# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. Создать экземпляры (объекты)
# цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть
# хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(это тоже
# методы). Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это
# тоже метод).

class Flowers:
    def __init__(self, name, color, stem_length, price, freshness):
        self.name = name
        self.colour = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness


class Rose(Flowers):
    def __init__(self, name, color, stem_length, price):
        super().__init__(name=name, color=color, stem_length=stem_length, price=price, freshness=10)


class Tulip(Flowers):
    def __init__(self, name, color, stem_length, price):
        super().__init__(name=name, color=color, stem_length=stem_length, price=price, freshness=7)


class Peony(Flowers):
    def __init__(self, name, color, stem_length, price):
        super().__init__(name=name, color=color, stem_length=stem_length, price=price, freshness=5)


class Bouquet(Flowers):
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def price_bouquet(self):
        return sum(flower.price for flower in self.flowers)

    def bouquet_wilting_time(self):
        avg_lifespan = sum(flower.freshness for flower in self.flowers) / len(self.flowers)
        return avg_lifespan

    def sort_by_stem_length(self):
        print("Sorting flowers by stem length: ")
        for flower in self.flowers:
            print(f"{flower.name} ({flower.stem_length} cm)")

    def sort_by(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def search_by_lifespan(self, threshold):
        print(f"Flowers with live everage >= {threshold}:")
        return [flower for flower in self.flowers if flower.freshness >= threshold]


rose_1 = Rose('Duett rose', 'coral', 1, 3)
rose_2 = Rose('Limbo rose', 'white', 1, 2.5)
tulip_1 = Tulip('Avignon tulip', 'red', 0.4, 1.2)
tulip_2 = Tulip('Batvia tulip', 'yellow', 0.6, 1.1)
peony_1 = Peony('Charies White', 'white', 0.5, 1.6)
peony_2 = Peony('Charies White', 'white', 0.5, 1.6)


bouquet = Bouquet()
bouquet.add_flower(rose_1)
bouquet.add_flower(peony_2)
bouquet.add_flower(tulip_1)

print(f"Bouquet cost: {bouquet.price_bouquet()} EUR")
print(f"Average wilting time: {bouquet.bouquet_wilting_time():.2f}")
bouquet.bouquet_wilting_time()

# Sort by stem length
bouquet.sort_by("stem_length")
print("Sorted by stem length:")
for flower in bouquet.flowers:
    print(f"{flower.name} ({flower.stem_length} cm)")

# Search by freshness threshold
threshold = 6
for flower in bouquet.search_by_lifespan(threshold):
    print(f"{flower.name} ({flower.freshness:.2f})")
