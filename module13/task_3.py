print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

def summ_num(number):
  count = 0
  figure = number
  while figure > 0:
    count += 1 
    figure //= 10
  q = count
  numer = 0
  summ = 0
  while number > 0:  
    numer = number % 10
    temp = numer
    summ += temp * 10 ** (q - 1)
    temp = 0
    q -= 1
    number //= 10
  print('Число наоборот: ',summ)
  return summ

total_sum = summ_num(first_number) + summ_num(second_number)

print('Сумма: ',total_sum)
summ_num(total_sum)

