# **Задание:**
# Напишите программу, которая:
# 1. Запрашивает у пользователя число `n`.
# 2. Выводит все числа от 1 до `n` в одной строке, разделяя их пробелами.
# 3. Выводит сумму всех чисел от 1 до `n`.

def sum_of_numbers(num):

    i = 1
    while i <= num:
        print(i, end=" ")
        i += 1

    summa = sum(range(1, num + 1))

    print()
    print(f"Сумма чисел: {summa}")

user_int = int(input("Введите число: "))

sum_of_numbers(user_int)
