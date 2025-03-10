# Напишите функцию **`check_grade(score)`**, которая принимает оценку и возвращает текстовое описание:
# - 90–100: "Отлично".
# - 75–89: "Хорошо".
# - 50–74: "Удовлетворительно".
# - Меньше 50: "Неудовлетворительно".

def check_grade(score):
    if 90 <= score <= 100:
        return "Отлично"
    elif 75 <= score <= 89:
        return "Хорошо"
    elif 50 <= score <= 74:
        return "Удовлетворительно"
    elif 0 <= score < 50:
        return "Неудовлетворительно"
    else:
        raise ValueError("Введите оценку от 0 до 100")

try:
    grade = int(input("Введите оценку: "))
    result = check_grade(grade)
    print(f"Оценка за {grade} баллов: {result}")
except ValueError:
    print("Введите целое число")

