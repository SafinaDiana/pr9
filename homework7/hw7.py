numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

if numbers:
    last_element = numbers.pop()  
    numbers.insert(0, last_element)  

print("Список после циклического сдвига вправо:", numbers)


