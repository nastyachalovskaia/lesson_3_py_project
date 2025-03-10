# **Описание:**
# Напишите функцию **`check_number(number)`**, которая сначала проверяет, является ли число положительным.
# Если число положительное, проверьте, является ли оно чётным. Выведите соответствующее сообщение для каждого случая.
# **Требования:**
# - Функция должна принимать один аргумент: число **`number`**.
# - Используйте вложенные условия (**`if`** внутри **`if`**) для проверки.
# - Верните строку с результатом проверки.
# - Выведите результат с помощью функции **`print()`**.

def check_number(number):

    if number >=0:
        if number % 2 == 0:
            return f"число {number} положительное и чётное"
        else:
            return f"число {number} положительное, но нечётное"
    else:
        return f"число {number} отрицательное"

user_int = int(input("Введите число: "))
result = check_number(user_int)
print(result)
