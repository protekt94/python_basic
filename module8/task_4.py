print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите число кротности: '))
summ = 0
count = 0
mean_summ = 0
for number in range(a,b+1):
  if number % c == 0:
    summ += number
    count += 1
mean_summ += summ / count
print('Среднее арифметическое: ', mean_summ)