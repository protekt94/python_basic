print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?
ticket = int(input('Введите шестизначный номер билета: '))
first_ticket = ticket // 1000
second_ticket = ticket % 1000
first_summ = first_ticket // 100 + first_ticket % 10 + (first_ticket % 100) // 10
second_summ = second_ticket // 100 + second_ticket % 10 + (second_ticket % 100) // 10
if first_summ == second_summ:
  print('Билет',ticket, '- счастливый')
else:
    print('Билет',ticket, '- несчастливый')
