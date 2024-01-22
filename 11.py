import math

# 1. Вычисление значений выражений
# a) (101 + 0) / 3
result_a = (101 + 0) / 3
print("a) Результат:", result_a)

# b) 3.0e-6 * 10000000.1
result_b = 3.0e-6 * 10000000.1
print("b) Результат:", result_b)

# c) true && true
result_c = True and True
print("c) Результат:", result_c)

# d) false && true
result_d = False and True
print("d) Результат:", result_d)

# e) (false && false) || (true && true)
result_e = (False and False) or (True and True)
print("e) Результат:", result_e)

# f) (false false) && (true && true)
result_f = (False or False) and (True and True)
print("f) Результат:", result_f)

# 2. Сравнение четырех целых чисел
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
number4 = int(input("Введите четвертое число: "))

if number1 == number2 == number3 == number4:
    print("Числа равны")
else:
    print("Числа не равны")

# 3. Поиск k самых больших элементов в массиве
def find_top_k(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:k]

numbers = [10, 5, 8, 20, 15, 3]
k = int(input("Введите количество элементов k: "))
result_top_k = find_top_k(numbers, k)
print(f"{k} самых больших элементов:", result_top_k)

# 4. Поиск k наименьших элементов в массиве
def find_bottom_k(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[:k]

result_bottom_k = find_bottom_k(numbers, k)
print(f"{k} наименьших элементов:", result_bottom_k)

# 5. Поиск чисел, превышающих среднее значение чисел массива
average = sum(numbers) / len(numbers)
result_above_average = [num for num in numbers if num > average]
print("Числа, превышающие среднее значение:", result_above_average)

# 6. Умножение двух целых чисел без использования оператора умножения(*)
num1 = int(input("Введите первое целое число для умножения: "))
num2 = int(input("Введите второе целое число для умножения: "))
result_multiply = sum(num1 for _ in range(num2))
print("Результат умножения:", result_multiply)

# 7. Разбиение массива целых чисел на четные и нечетные
def split_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    return even_numbers, odd_numbers

result_even, result_odd = split_even_odd(numbers)
print("Четные числа:", result_even)
print("Нечетные числа:", result_odd)

# 8. Преобразование температуры из градуса Фаренгейта в градус Цельсия
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
result_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print("Температура в градусах Цельсия:", result_celsius)

# 9. Вычисление индекса массы тела (ИМТ)
weight = float(input("Введите вес в килограммах: "))
height = float(input("Введите рост в метрах: "))
bmi = weight / height**2
print("Индекс массы тела (ИМТ):", bmi)

# 10. Вывод квадрата, куба и четвертой степени числа
number_for_powers = float(input("Введите число для вычисления степеней: "))
square = number_for_powers**2
cube = number_for_powers**3
fourth_power = number_for_powers**4
print(f"Квадрат числа: {square}, Куб числа: {cube}, Четвертая степень числа: {fourth_power}")

# 11. Проверка возможности образования треугольника по трем сторонам
side1 = float(input("Введите длину первой стороны треугольника: "))
side2 = float(input("Введите длину второй стороны треугольника: "))
side3 = float(input("Введите длину третьей стороны треугольника: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("Треугольник возможен")
else:
    print("Треугольник невозможен")
