import math
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    Периметр P = 2 × (a + b), где a и b — соседние стороны
    Площадь S = a × b, где S — площадь; a, b — длина и ширина
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)
    assert perimeter == 60
    # TODO сосчитайте площадь
    area = 10 * 20
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь

    area = math.pi * r ** 2
    assert area == 1661.9025137490005
    # TODO сосчитайте длину окружности
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    Чтобы сгенерировать список случайных чисел, нужно использовать функцию random.sample(population, k),
    которая генерирует список длины k из элементов population без повторений.
    В данном случае population будет диапазон чисел от 1 до 100 включительно, а k - количество элементов в списке.
    random.sample() выбирает 10 случайных чисел, которые сохраняются в переменной l.
    """
    # TODO создайте список
    l = sorted(random.sample(range(1, 101), 10))

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    zipped = zip(first, second)
    d = dict(zipped)
    assert isinstance(d, dict)
    assert len(d) == 5
