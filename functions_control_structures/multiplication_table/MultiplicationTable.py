# Напишите программу, которая выводит таблицу умножения от 1 до 10.

def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end='')
        print()
multiplication_table()
