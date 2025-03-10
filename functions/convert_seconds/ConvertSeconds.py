# **Требования:**
# - Функция должна принимать один аргумент: количество секунд.
# - Вычислите количество полных часов и оставшихся минут.
# - Верните результат в виде кортежа **`(hours, minutes)`**.
# - Выведите результат в формате: "В 3672 секундах содержится 1 час(ов) и 2 минут(ы)."

def convert_seconds(seconds):
  total_hours = seconds // 3600
  remaining_seconds = seconds % 3600
  total_minutes = remaining_seconds // 60
  time_tuple = (total_hours, total_minutes)

  return time_tuple

seconds_input = int(input("Введите количество секунд: "))
hours, minutes = convert_seconds(seconds_input)

print(f"В {seconds_input} секундах содержится {hours} час(ов) и {minutes} минут(ы).")
