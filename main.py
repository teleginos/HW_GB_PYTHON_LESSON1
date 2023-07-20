from decimal import Decimal, getcontext
import random
import time


def case1():
    print("Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите\n"
          "минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той\n "
          "же стороной. Выведите минимальное количество монет, которые нужно перевернуть")

    n_0 = 0
    n_1 = 0
    n = int(input('Какое кол-во монет будем рассматривыать: '))
    tuple_n = tuple(random.choices([0, 1], k=n))
    for i in tuple_n:
        if i == 0:
            n_0 += 1
        else:
            n_1 += 1
    print(f"{tuple_n}\nМинимальное значение монет которое требуется перевернуть = {min(n_0, n_1)}")


def case2():
    def find_number(n, m):
        for number1 in range(1, n + 1):
            if m % number1 == 0:
                number2 = m // number1
                if number1 + number2 == n:
                    return number1, number2

    print("Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по\n"
          "математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого\n"
          "Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать \n"
          "задуманные Петей числа.\n")

    x = random.randint(1, 1000)
    y = random.randint(1, 1000)

    s = x + y
    p = x * y
    print(f"Сумма загаданных чисел = {s}\nПроизведение загадынных чисел = {p}")

    result = find_number(s, p)
    print(f"Загаданые числа {result[0]} и {result[1]}")


def case3():
    print("Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.",
          end='\n')
    n = int(input("Введите число: "))
    count = 1
    while 1:
        if pow(2, count) < n:
            print(pow(2, count), end="\t")
            count += 1
        else:
            break


def case4():
    def sum_digits(num):
        if isinstance(num, int):
            return sum_digits_int(num)
        elif isinstance(num, float):
            num = Decimal(str(num))
            int_part, float_part = int(num), num - int(num)
            getcontext().prec = len(str(num))
            return sum_digits_int(int_part) + sum_digits_float(float_part)
        else:
            raise ValueError("Число должно быть целым или вещественным.")

    def sum_digits_int(n):
        n = abs(n)
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    def sum_digits_float(n):
        total = 0
        while n > 0:
            n *= 10
            digit = int(n)
            total += digit
            n -= digit
        return total

    number = float(input("Введите число: "))
    print(sum_digits(number))


def case5():
    def check_statement(predicates):
        return not any(predicates) == all(not p for p in predicates)

    start_time = time.time()

    for _ in range(100):
        num_predicates = random.randint(3, 15)
        predicates = [random.choice([True, False]) for _ in range(num_predicates)]
        print(f"Предикаты: {predicates} - Утверждение {'верно' if check_statement(predicates) else 'ложно'}")

    end_time = time.time()

    print(f"Общее время выполнения: {end_time - start_time} секунд")


def case6():
    def all_divisors(number):
        divisors = set()
        for i in range(1, int(number ** 0.5) + 1):
            if number % i == 0:
                divisors.add(i)
                divisors.add(number // i)
        return sorted(list(divisors))

    print(all_divisors(int(input("Введите целое число: "))))


def default():
    print("\nВы выбрали неизвестный случай")


switch_case = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
    5: case5,
    6: case6
}

user_input = int(input("1: Задача про монетки\n2: Задача про Петю и Катю\n"
                       "3: Задача про степени числа 2\n4: Задача про сумму цифр числа\n5: Задача Де Моргана\n"
                       "6: Поиск положительных целых делителей\n\nВыберите номер задания для запуска кода: "))

print("=" * 50)
switch_case.get(user_input, default)()
