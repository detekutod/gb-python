# программа должна спрашивать число участников в соревнованиях
# после происходит ввод участников от N до 1 места с клавиатуры
# сортирует всех участников по имени, вывод
# выводит на печать первые три места

#my solution
print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите число участников:'))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место?'.format(i))
    members.append(name)
    i -= 1

members.reverse()

winners = ''
i = 2
while i >= 0:
    winners += members[i]
    if i != 0:
        winners += ','
    i -= 1

#print('check')
#print(winners)

temp = 'Поздравляем победителей {} с победой!'
print(temp.format(winners))

#function sorted() allows to sort list

#example = ['Kate','John','Kot','Anna','Ron','Harry','Boris']
#print(example)
#example = sorted(example)
#print(example)
