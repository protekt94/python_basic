print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######
number = int(input('Введите высоту треугольника: '))
for row in range(number):
  for col in range(number + number - 1):
    if col == number - 1:
      print('#', end = '')
    elif col > -row + number - 2 and col < number -1 :
      print('#', end = '')
    elif col <= row + number -1 and col > number -1:
      print('#', end = '')
    else:
      print(' ', end = '')
  print()