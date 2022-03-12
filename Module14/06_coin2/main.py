import math

x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
def money(x,y,r):
    hyp = math.sqrt(x**2 + y**2)
    if hyp < r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

money(x,y,r)