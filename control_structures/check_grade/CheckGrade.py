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

def grade_input():
    try:
        grade = int(input("Введите оценку: "))
        return grade
    except ValueError:
        print("Введите целое число")
        exit()

user_grade = grade_input()
result = check_grade(user_grade)
print(f"Оценка за {user_grade} балла/ов: {result}")