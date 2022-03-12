def sum_num(num):
    count_sum = 0
    while num > 0:
        count_sum += num % 10
        num //= 10

    return count_sum

def count_num(num):
    count_num = 0
    while num > 0:
        count_num += 1
        num //= 10
    return count_num
num = int(input('Введите число: '))
sum_num(num)
count_num(num)
print(f'Сумма цифра:  {sum_num(num)}')
print(f'Кол-во цифр в числе: {count_num(num)}')
print(f'Разность суммы и кол-во цифр: {sum_num(num) - count_num(num) }')