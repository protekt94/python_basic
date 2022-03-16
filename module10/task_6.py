print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

num = int(input('Введите число: '))
count = 1
summ = 0
for number in range(1,num+1):
  for i in range(1,number+1):
    count *= i
  summ += count
  count = 1
print(summ)