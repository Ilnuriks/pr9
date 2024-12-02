import random
# Определение лотерейного билета
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
# Функция для выбора чисел пользователем
def user_selection():
    user_numbers = []
    for i, row in enumerate(ticket):
        choice = int(input(f"Выберите число из строки {i + 1} {row}: "))
        while choice not in row:
            choice = int(input(f"Некорректный выбор. Выберите число из строки {i + 1} {row}: "))
        user_numbers.append(choice)
    return user_numbers

# Функция для случайного выбора чисел приложением
def random_selection():
    return [random.choice(row) for row in ticket]

# Функция для подсчета выигрышей
def count_matches(user_numbers, drawn_numbers):
    return len(set(user_numbers) & set(drawn_numbers))

# Главная функция
def main():
    user_numbers = user_selection()
    drawn_numbers = random_selection()
    
    print("Ваши числа:", user_numbers)
    print("Числа, выбранные лотереей:", drawn_numbers)
    
    matches = count_matches(user_numbers, drawn_numbers)
    
    print(f"Количество совпадений: {matches}")

if __name__ == "__main__":
    main()
