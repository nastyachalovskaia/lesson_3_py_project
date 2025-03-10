# **Задание:**
# Напишите программу, которая:
# 1. Реализует основную функцию `calculator()`, которая:
#     - Спрашивает у пользователя два числа.
#     - Спрашивает операцию (`+`, , , `/`).
#     - Использует вложенные функции для выполнения каждой операции.
# 2. Возвращает результат выбранной операции.

def calculator(user_num_a, user_num_b):
    choose_operation = input("Введите операцию (+, -, *, /): ")

    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def division(a, b):
        try:
            res = a / b
        except ZeroDivisionError:
            res = "Деление на ноль запрещено"
        return res

    if choose_operation == "+":
        return addition(user_num_a, user_num_b)
    elif choose_operation == "-":
        return subtraction(user_num_a, user_num_b)
    elif choose_operation == "*":
        return multiply(user_num_a, user_num_b)
    elif choose_operation == "/":
        return division(user_num_a, user_num_b)
    else:
        return "Некорректная операция"

user_int1 = float(input("Введите первое число: "))
user_int2 = float(input("Введите второе число: "))

total_result = calculator(user_int1, user_int2)
print("Результат:", total_result)
