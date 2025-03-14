# Напишите функцию **`countdown()`**, которая выводит обратный отсчёт от 10 до 1 и затем выводит **`"Старт!"`**.
# **Требования:**
# - Функция не принимает аргументов.
# - Используйте цикл **`for`** для реализации обратного отсчёта.
# - Выводите каждое число на новой строке.
# - После завершения отсчёта выведите сообщение **`"Старт!"`**.
# - Не возвращайте значение, а напрямую выводите результат с помощью функции **`print()`**.

def countdown():
    for i in reversed(range(1, 11)):
        print(i)

countdown()
print("Старт!")
