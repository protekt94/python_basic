print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

x = int(input('Введите число: '))
for number in range(1,7):
  number = 2 ** number - 1
  up = (x - number)
for number in range(1,7):
  number = 2 ** number
  down = (x - number)
res = up / down 
print(res)
