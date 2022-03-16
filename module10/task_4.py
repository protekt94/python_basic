print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^

in_row = int(input('Введите ширину: '))
in_col = int(input('Введите высоту: '))

for row in range(in_row):
  for col in range(in_col):
    if row == col:
      print('^', end = '')
    elif -row + in_row == col+1:
      print('^', end = '')
    else:
      print(' ', end = '')
  print()