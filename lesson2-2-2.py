# вывести все простые числа до введённого включительно

# функция is_simple возвращает 0 если число простое
# и возвращает -1 если число не является простым

def is_simple(a):
    flag = True
    for i in range(2,a):
        if (i != 1) and (a % i == 0):
            flag = False
            return -1
    if flag:
        print('NUMBER',a,'== SIMPLE ==')
        return 0

limit = int(input('Введите верхнее число диапазона:'))
c = 0
s = 0

for k in range(2,limit+1):
    #is_simple(k)
    if is_simple(k) == 0:
        #print('Число',k,'- простое')
        c += 1
        s += k

# upd 1
# выводит количество простых чисел
# выводит сумму простых чисел

print('Простых чисел в диапазоне:',c)
print('Сумма простых чисел в диапазоне:',s)
    
    
