numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")

# Выводим только нечетные элементы списка
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Нечетные элементы списка:", odd_numbers)
