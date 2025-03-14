# Напишите функцию **`check_string_length(string, length)`**, которая принимает строку и число.
# Если длина строки больше указанного числа,
# выведите **`"Длина строки достаточная"`**, иначе – **`"Строка слишком короткая"`**. Используйте **`if-else`**.
# **Требования:**
# - Функция должна принимать два аргумента: строку **`string`** и число **`length`**.
# - Используйте **`if-else`** для сравнения длины строки с числом.
# - Верните результат из функции.
# - Выведите результат с помощью функции **`print()`**.
# **Вывод результата:**
# Длина строки "Python" достаточная.
# Строка "Hi" слишком короткая.

def check_string_length(string, length):
    if len(string) >= length:
        return f"Длина строки {string} достаточная"
    else:
        return f"Строка {string} слишком короткая"

user_input_str = input("Введите строку: ")
user_input_num = int(input("Введите число: "))
result = check_string_length(user_input_str, user_input_num)

print(result)
