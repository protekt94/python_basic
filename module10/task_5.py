print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.


count = 0
sum_count = 0
sum_number = int(input('Введите длину последовательности: '))
for i in range(sum_number):

  number = int(input('Введите число: '))
  for num in range(2, number//2+1):
    if number % num == 0:
      count += 1
  if count == 0:
    sum_count += 1
  count = 0

print('Количество простых чисел', sum_count)
