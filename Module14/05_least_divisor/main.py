num = int(input('Введите число: '))
def min_diff(num):
    n = num
    for i in range(num+1,1,-1):
        if num % i == 0:
            count = i
            if count < n:
                n = count
    print(f'Наименьший делитель, отличный от единицы: {n}')

min_diff(num)