# **Описание:**
# Напишите функцию **`count_items`**, которая принимает произвольное количество аргументов и возвращает их количество.
# **Требования:**
# - Функция должна принимать произвольное количество аргументов с помощью **`args`**.
# - Подсчитайте количество переданных аргументов.
# - Верните результат из функции.
# - Выведите результат в формате: "Количество переданных элементов: 5."

def count_items(*args):
   return len(args)

user_input = input("Введите аргументы через пробел: ")
arguments = user_input.split()
result = count_items(*arguments)

print(f"Количество переданных элементов: {result}")
