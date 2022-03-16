print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

rows = int(input('Введите высоту пирамиды: '))
new_sum = 1
for line in range(rows):
  space_range = rows - line - 1
  print('   ' * space_range, end = '')
  for number in range(line + 1):
    print(new_sum, end = '    ')
    new_sum += 2
  print()