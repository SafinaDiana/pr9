import random
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def user_selection(ticket):
    user_numbers = []
    for i, row in enumerate(ticket):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} {row}: "))
                if number in row:
                    user_numbers.append(number)
                    break
                else:
                    print("Выберите число, которое есть в строке!")
            except ValueError:
                print("Пожалуйста, введите корректное число.")
    return user_numbers


def random_selection(ticket):
    return [random.choice(row) for row in ticket]

print("Добро пожаловать в приложение-лотерею!")

user_numbers = user_selection(ticket)
print("Ваш выбор:", user_numbers)

app_numbers = random_selection(ticket)
print("Выбор приложения:", app_numbers)

matches = len(set(user_numbers) & set(app_numbers))
print(f"Количество совпадений: {matches}")
