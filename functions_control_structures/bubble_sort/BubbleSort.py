# **Задание:**
# Напишите программу, которая:
# 1. Запрашивает у пользователя список чисел через запятую.
# 2. Реализует функцию `bubble_sort(numbers)`, которая сортирует список чисел методом пузырька.
# 3. Выводит отсортированный список.

def bubble_sort(numbers):
    n = len(numbers)
    for run in range(n-1): # обход на единицу меньше, чем кол-во элементов
        for i in range(n-1-run):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers

user_input = input("Введите числа через запятую: ").replace(" ", "")

try:
    user_numbers = list(map(int, user_input.split(",")))
    result = bubble_sort(user_numbers)
    print("Отсортированный массив:", result)
except ValueError:
    print("Введите числа, разделённые запятыми.")
