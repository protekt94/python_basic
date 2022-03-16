print('Задача 1. Календарь')

# Мы продолжаем разрабатывать удобный календарь для смартфона.
# Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
# 
# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
# 
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2


weekday = input('Введите день недели: ')
count = 0

for day in ('понедельник','вторник','среда','четверг','пятница','суббота','воскресенье'):
  count += 1
  if day == weekday:
    break
print('Номер дня недели:',count)