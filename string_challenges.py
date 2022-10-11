# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(word.lower().count('а') + word.lower().count('е'))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split()
a=sentence[0]
b=sentence[1]
c=sentence[2]
d=sentence[3]
print(a[0],b[0], c[0], d[0], sep='\n')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
print(f'Средняя длина слов составляет:', ((len(sentence[0])+len(sentence[1])+len(sentence[2])+len(sentence[3]))/4))

