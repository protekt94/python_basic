print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

a = int(input('Введите четырёхзначное число: '))
b,c,d,e = a // 1000,  a // 100, a // 10, a % 10
c = c % 10
d = d % 10
a = str(e)+str(d)+str(c)+str(b)
print('Обратное число:',a)