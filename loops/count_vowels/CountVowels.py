# **Требования:**
# - Функция должна принимать один аргумент: строку **`string`**.
# - Используйте цикл **`for`** для перебора символов строки.
# - Гласные буквы могут быть как в нижнем, так и в верхнем регистре.
# - Верните результат из функции.
# - Выведите результат с помощью функции **`print()`**.

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for s in string:
        if s in vowels:
            total += 1
    return total

user_input_str = input("Введите строку: ").capitalize()
print(count_vowels(user_input_str))
