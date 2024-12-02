import random

# Генерация списка случайных чисел
numbers = [random.randint(1, 100) for _ in range(10)]
print("Сгенерированный список:", numbers)

# Вывод элементов, которые больше предыдущего
greater_numbers = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

print("Элементы больше предыдущего:", greater_numbers)
