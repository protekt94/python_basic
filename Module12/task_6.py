print('Задача 6. Метеостанция')
import math
# Для удобства работы сотрудников международной метеостанции
# каждый день нужно распечатывать различные таблицы
# соответствия градусов по шкале Цельсия и Фаренгейта.
#
# Напишите программу,
# которая принимает на вход три целых числа
# в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран
# таблицу соответствия градусов Цельсия градусам Фаренгейта
# от нижней до верхней границы с указанным шагом.
#
# Обеспечьте контроль ввода.
# Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее.
# Известно, что 0С соответствует 32F,
# а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.
#
# Пример:
#
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
#
# Вывод:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122

start = int(input('Нижняя граница: '))
end = int(input('Верхняя граница: '))
step = int(input('шаг: '))
celsius = 0
fahrenheit = 32
print('celsius','fahrenheit')
print(celsius,fahrenheit)
for num in range(0,math.ceil(end/step)):
  celsius +=step
  if celsius > end:
    celsius = end
    step //= 2
  fahrenheit += int(step * 1.8)
  print(celsius,fahrenheit)