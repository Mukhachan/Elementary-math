n = int(input('Количество спичек: '))

if (n-1)%4!=0:
    print('Хожу Я')
    n -= (n-1)%4
    print(f'n = {n}')

while n>1:
    print('Ходит игрок ', end='')
    hod_igroka = int(input())
    if 1 < hod_igroka <=3:
        n -= hod_igroka
        print(f'n = {n}')
        
        n -= (4-hod_igroka)
        print(f'Я выбираю {4-hod_igroka}')
        print(f'n = {n}')
    else:
        print('Ты ввёл не подходящее значение')

print('Я выйграл')