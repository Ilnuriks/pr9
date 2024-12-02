while True:
    try:
        a = int(input("Введите первое целое число (a): "))
        b = int(input("Введите второе целое число (b): "))
        break
    except ValueError:
        print("Ошибка! Введите целые числа.")

start = min(a, b)
end = max(a, b) 

squares = [x**2 for x in range(start + 1, end)]

print("Список квадратов чисел:", squares)
