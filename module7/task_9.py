print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

count = 0
summ = 0
for number in range(11):
  income = int(input('Введите число: '))
  if income < summ:
    count += 1
  summ = income
if count == 0:
  print('Зарплата увеличивается')
else: 
  print('Зарплата не увеличивается')
  