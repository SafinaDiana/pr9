a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

start = min(a, b) + 1
end = max(a, b)

squares = [x**2 for x in range(start, end)]

print("Список квадратов чисел между a и b:", squares)



