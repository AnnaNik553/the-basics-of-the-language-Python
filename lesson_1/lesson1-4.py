# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))

while number <= 0:
    number = int(input('Введите целое положительное число: '))

s = 0
max = 0
while number > 0:
    s = number % 10
    if s > max:
        max = s
    number = number // 10
print(f'Самая большая цифра в числе: {max}')
