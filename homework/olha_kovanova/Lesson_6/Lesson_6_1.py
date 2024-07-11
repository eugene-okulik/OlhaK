# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat, quis
# # molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого
# выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая
# или точка, этот знак препинания должен идти после того же слова, но уже преобразованного.
text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, ' \
       'dignissim vitae libero'
words = text.split()
print(words)
fin_word = []
for word in words:
    if ',' in word:
        ing_word = word.replace(',', 'ing,')
    elif '.' in word:
        ing_word = word.replace('.', 'ing.')
    else:
        ing_word = word + 'ing'
    fin_word.append(ing_word)
print(' '.join(fin_word))
