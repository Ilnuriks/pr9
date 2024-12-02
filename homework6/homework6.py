import random
# Генерируем случайный список из 10 чисел от 1 до 100
numbers = [random.randint(1, 200) for _ in range(15)]

# Выводим сгенерированный список
print("Сгенерированный список:", numbers)

# Находим индексы минимального и максимального элементов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Меняем местами минимальный и максимальный элементы
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после обмена минимального и максимального:", numbers)
