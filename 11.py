def c_Check():  # обработчик ошибки ввода кол-ва бочонков
    while True:
        try:
            c = int(input())
            return c
        except ValueError:
            print("Нужно ввести цифру!")


f=open("for 11.txt","r+")
s=(f.read())
a=s.split(',')
c = 3
b = 3
while c != 0:
    print ('1 - Найти страну по столице \n2 - Найти столицу по стране \n3 - Закончить \n')
    c = c_Check()
    if c == 1:
        for i in a:
            cap = str(input('Введите столицу (на английском языке с большой буквы): \n'))
            if cap in a:
                index_of_cap = a.index(cap)
                print (cap + ' столица страны ' + a[index_of_cap-1])
            else:
                print ('К сожалению такой столицы нет в списке \n')
            print('1 - Найти еще одну страну по столице \n2 - Вернуться обратно')
            b = int(input())
            if b == 1:
                continue
            if b == 2:
                break
    if c == 2:
        for i in a:
            cap = str(input('Введите страну (на английском языке с большой буквы): \n'))
            if cap in a:
                index_of_cap = a.index(cap)
                print (cap + ' страна со столицей ' + a[index_of_cap+1])
            else:
                print ('К сожалению такой страны нет в списке \n')
            print('1 - Найти еще одну страну по столице \n2 - Вернуться обратно')
            b = int(input())
            if b == 1:
                continue
            if b == 2:
                break
    if c == 3:
        break
