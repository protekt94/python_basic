print('Задача 8. Часы')

# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа. 
# Входные и выходные данные — действительные числа.
# 
# При решении этой задачи нельзя пользоваться условными операторами и циклами.

alfa = int(input('Введите угол α: '))
hourse = alfa / 30
minutes = int(0.6 * int((hourse - int(hourse))* 100))
degree = int(360/60 * minutes)
print('С последнего часа минутная стрелка сдвинулась на {} градусов'.format(degree))

