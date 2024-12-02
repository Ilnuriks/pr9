import random
# Генерация случайного списка чисел
numbers = [random.randint(1, 200) for _ in range(10)]
print("Список до сдвига:", numbers)

if len(numbers) > 0:  # Проверка на пустой список
    last_element = numbers[-1]  # Сохраняем последний элемент
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]  # Сдвигаем элементы вправо
    numbers[0] = last_element  # Вставляем последний элемент на первое место

print("Список после циклического сдвига вправо:", numbers)