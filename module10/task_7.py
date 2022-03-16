print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

count_num = int(input('Введите кол-во чисел: '))
max_num = 0
count = 0
for num in range(count_num):
  number = int(input('Введите число: '))
  answer = number
  while number != 0:
    k = number % 10
    count += k
    number //= 10
  print(count)
  if max_num < count:
    max_num = count
    count = 0
  else:
    count = 0
print('Самое большое число: ',answer, 'сумма цифр', max_num)
