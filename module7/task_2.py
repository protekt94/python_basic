print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# 
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.
summ = 0
for client in range(10):
  client = int(input('Введите число: '))
  if client % 2 == 0 and client > 0:
    summ += 1
print(summ,'чисел положительных и четных')