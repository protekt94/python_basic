print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
precision = float(input('Введите точность: '))
x = int(input('Введите х: '))

result = 0
addMember = 1
number = 0

def factorial(number):
  count = 1
  summa = 1
  for num in range(1,number * 2 + 1):
    for i in range(1,num+1):
      count *= i
    summa = count
    count = 1
  return summa
  
while abs(addMember) > precision:
  addMember = (-1) ** number * (x ** (2 * number) / factorial(number))
  result += addMember
  number += 1
print('Сумма ряда равна ', result)
