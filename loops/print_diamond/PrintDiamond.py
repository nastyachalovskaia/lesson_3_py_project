# **Требования:**
# - Функция должна принимать один аргумент: количество строк **`rows`** (максимальное число звёздочек в центре).
# - Используйте циклы для построения фигуры.
# - Не возвращайте значение, а напрямую выводите фигуру с помощью функции **`print()`**.

def print_diamond(rows):
    if rows % 2 == 0:
        rows -= 1

    for i in range(1, rows + 1, 2):
        spaces = (rows - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(rows - 2, 0, -2):
        spaces = (rows - i) // 2
        print(" " * spaces + "*" * i)

user_input = int(input("Введите желаемое количество *: "))
print_diamond(user_input)
