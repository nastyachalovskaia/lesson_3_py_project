# **Требования:**
# - Функция должна принимать один аргумент: список чисел **`numbers`**.
# - Используйте цикл **`for`** для поиска минимального числа.
# - Верните результат из функции.
# - Выведите результат с помощью функции **`print()`**.

def find_min(numbers):

    min_number = numbers[0]
    for i in numbers:
        if i < min_number:
            min_number = i
    return min_number

user_input = input("Введите числа через запятую: ").replace(" ", "")

nums = []
for num in user_input.split(","):
    nums.append(int(num))

print(f"Минимальное число в списке {nums}: {find_min(nums)}")
