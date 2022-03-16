print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Степендия равна: '))
expenses = int(input('Аренда жилья равна: '))
summ = 0
percent = 0.03 * expenses
for month in range(2,11):
  summ += percent + expenses
educational_grant_sum = month * educational_grant
income = summ - educational_grant_sum
print('Для оплаты {} месяцев нужно: {}'.format(month, income))