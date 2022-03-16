print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

line = int(input('Введите число: '))
for row in range(line):
  for col_left in range(line,line - row-1,-1):
    print(col_left, end = '')
  point_count = 2 * (line - row - 1)  
  print('.' * point_count, end = '')
  for col_right in range(line - row, line + 1 ):
    print(col_right, end = '')
  print()