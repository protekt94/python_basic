print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
# 
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
# 
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
# 
# 
# Пример 1:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
# 
# Пример 2:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
# 
# Пример 3:
# 
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
if boys > girls:
  N = girls
else:
  N = boys
summ = ''
same = 'BG'
girl = 'GBG'
boy = 'BGB'
for man in range(N):
  if boys / 2 > girls or girls / 2 > boys:
    print('Нет решения!')
    break
  elif boys == girls:
    summ += same
  elif boys > girls:
    summ += boy
    boys -= 1
  elif  girls > boys:
    summ += girl
    girls -= 1
print(summ)
