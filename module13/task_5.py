print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

first_n = int(input("Введите первое число: "))  
second_n = int(input("\nВведите второе число: "))

def num_count(num):
  count = 0
  temp = num
  while temp > 0:
    count += 1
    temp //= 10
  return count

def change(number):
  last_digit = number % 10
  first_digit = number // 10 ** (num_count(number) - 1)
  between_digits = number % 10 ** (num_count(number) - 1) // 10
  number = last_digit * 10 ** (num_count(number) - 1) + between_digits * 10 + first_digit
  return number

if num_count(first_n) < 3:
  print("В первом числе меньше трёх цифр.")
else:
  print('Изменённое первое число:', change(first_n))
  
if num_count(second_n) < 4:
  print("Во втором числе меньше четырёх цифр.")
else:
  print('Изменённое второе число:', change(second_n))
  print('\nСумма чисел:', change(first_n) + change(second_n))

  
