num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

def integer(num):
    number = ''
    for a in num:
        if a == '.':
            break
        else:
            number += a
    number = int(number)
    return number
def frac(num):
    number = ''
    flag = True
    for a in num:
        if a =='.':
            flag = False
        elif not flag:
            number += a
    number = int(number)
    return number
def rotation(num):
    count = 0
    figure = num
    while figure > 0:
        count += 1
        figure //= 10
    q = count
    numer = 0
    summ = 0
    while num > 0:
        numer = num % 10
        temp = numer
        summ += temp * 10 ** (q - 1)
        temp = 0
        q -= 1
        num //= 10
    return summ
def con(num_1,num_2):
    return float(str(num_1) + '.' + str(num_2))
sum_1 = con(rotation(integer(num_1)),rotation(frac(num_1)))
sum_2 = con(rotation(integer(num_2)),rotation(frac(num_2)))

print('Сумма:',sum_1 + sum_2)

# while num % 10 != 0:
#     print(num % 10)
#     num *= 10

