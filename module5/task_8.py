print('Задача 8. Новоселье')

# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении,
# какую же всё-таки купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на нескольких вариантах:

# Первый вариант 
# они готовы взять квартиру попросторнее (не менее 100 квадратных метров),
# но стоимостью не более 10 млн.
 
# Второй вариант — немного расширить круг поиска,
# то есть взять квартиру поменьше (от 80 квадратный метров),
# но и стоимостью не более 7 млн.
 
# Напишите программу,
# которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет

price = int(input('Введите стоимость квартиры: '))
square = int(input('Введите площадь квартиры: '))

if (price <= 10000000 and square >= 100) or (price <= 7000000 and square >= 80):
  print('Квартира подходит')
else:
  print('Квартира не подходит')