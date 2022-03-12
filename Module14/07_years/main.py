year_down = int(input('Введите первый год: '))
year_top = int(input('Введите Второй год: '))
def bad_years(year_down,year_top):
    sym = ''
    count = 0
    n = 1
    for i in range(year_down,year_top+1):
        first_num = str(i // 1000)
        for a in str(i):
            if a == sym:
                count += 1
                if n >= 3 and a == first_num:
                    count += 1
            if count == 2:
                result = i
                print(result)
            n += 1
            sym = a
        count = 0
        sym = ''
print(f'Года от {year_down} до {year_top} с тремя одинаковыми цифрами:')
bad_years(year_down,year_top)

