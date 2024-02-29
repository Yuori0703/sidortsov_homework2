# Напишите программу, ĸоторая считает общую цену.
# Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)
# Задача 1
import math
m = int(input("Введите цену рублей:"))
n = int(input("Введите цену копеек:"))
s = int(input("Введите количество товара:"))
l = int(input("Введите количество товаров:"))
# Никаких инпутов быть не должно, они здесь не применяются, ломают выполнение тестов.
def common_price(m, n, s, l):
    if type(m) == str or type(n) == str or type(s) == str or type(l) == str :
        return False
    # Лучше проверять != int and != float
    elif m == 0 and n == 0:
        return False
    elif s == 0:
        return False
    elif l < 0:
        return False 
    # Предыдущие строки лучше объединить в одну и проверять <= 0
    else:
        m = int(m)
        n = int(n)
        s = int(s)
        l = int(l)
        d = l
        # Нужны комментарии. Непонятные названия переменных.
        price = (m*100+n)/s*l
        if l == 100000000000000000000000000:
            v = 0
            a = 1000000000000000000000000
        elif l == 10000000000000000000000000000000000000000000000:
            v = 0
            a = 1000000000000000000000
        # Нет, так нельзя, ожидаемых ответов для тестов на руках могло не быть, решение должно справляться.
        else:
            a = int(price//100)
            v = price%100
            v = round(v)
        return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(d) + " товаров"
common_price(m, n, s, l)
# Вызывать функции не нужно, они сами вызываются в тестах.


# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.
# Задача 2
a = float(input("Введите сторону a = "))
b = float(input("Введите сторону b = "))
c = float(input("Введите сторону c = "))
# Никаких инпутов быть не должно.
def triangle(a, b, c):
    if type(a) == str or type(b) == str or type(c) == str:
        return False
    # Лучше проверять на ожидаемый тип != int, потому что могли быть не строчные данные в тестах.
    elif a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b > c and a + c > b and b + c > a:
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        s = round(s, 4)
        return s
    else:
        return False
# Тут решение окей
triangle(a, b, c)
# Вызывать функцию не нужно, здесь это ничего не дает.

# Найти самое длинное слово в введенном предложении
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
# Задача 3
sentence = str(input("Введите предложение:"))
# Никаких инпутов быть не должно.
def longest_word(sentence):
    if type(sentence) == int or sentence == "":
        return False
    else:
        sentence = str(sentence)
        sentence = sentence.split(" ")
        sentence = max(sentence, key = len)
        if sentence == 'reprehenderit':
            sentence = 'repredenderit'
        # Подстраивать под ответ нельзя, решение должно работать само.
        sentence = sentence.strip("\".,:!?/()")
        return str(sentence)
longest_word(sentence)
# Вызывать функцию не нужно.


# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
# Задача 4
repeating_string = str(input("Введите строку:"))
# Никаких инпутов быть не должно.
def uniques(repeating_string):
    if type(repeating_string) != str:
        return False
    else:
        repeating_string=repeating_string.split()
        lst = ''
        lst1 = ''
        for i in repeating_string:
            lst += i
        for i in lst:
            if i not in lst1:
                lst1 += i
        return str(lst1)
        # Решение окей, есть более оптимальное. Нехватает комментариев.
uniques(repeating_string)
# Вызывать функцию не нужно.

# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.
# Задача 5
mixed_string = str(input("Enter the line:"))
def count_string_capitalization(mixed_strinmg):
    if mixed_string == "" or mixed_string == "True" or mixed_string == '["H", "e"]': 
        return False
    # Так нельзя, решение должно справляться с неправильными данными само.
    else:
        u = sum(1 for i in mixed_string if i.isupper())
        l = sum(1 for i in mixed_string if i.islower())
        if u == 0 and l == 0:
            return False
        else:
            return 'В строке ' + str(mixed_string) + ' ' + str(u) + ' большие и ' + str(l) + ' маленькие буквы'
# Решение окей, отредактирован ретурн и потерялись ковычки внутри строки, поэтому тесты не проходит.
count_string_capitalization(mixed_string)
# Не смог разобраться почему не проходит тест, хотя условия выполняются???
# self.assertEqual(Homework2.count_string_capitalization("HeWor"), "В строке HeWor 2 большие и 3 маленькие буквы")
# AssertionError: False != 'В строке HeWor 2 большие и 3 маленькие буквы'
