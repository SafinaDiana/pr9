numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены минимального и максимального элемента:", numbers)


