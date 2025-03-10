# **Требования:**
# - Функция должна принимать один аргумент: число **`number`**.
# - Используйте тернарный оператор для проверки чётности числа. // a if condition else b
# - Верните результат из функции.
# - Выведите результат с помощью функции **`print()`**.

def check_is_even(number):
    result = "Четное" if number % 2 == 0 else "Нечетное"
    return result

user_num = int(input("Введите число: "))
total_result = check_is_even(user_num)
print(f"Число {user_num}: {total_result}")