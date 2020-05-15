# встроенные типы и операции с ними
# range и его применение

# 1 application
# 2 ways
# 3 'for in range' cicle
# 4 which use: while / for / for k in range

# winners = ['Max','Leo','Kate']

# простой перебор
'''
for winner in winners:
    print(winner)
'''
# что делать если нужно вывести место победителя?
# использовать while?
# или есть способ лучше?

# вывести нечетные цифры от 1 до 5
'''
numbers = [1,3,5]

for number in numbers:
    print(number)
'''

# how to do this if we have 100 numbers? 1000 numbers?
# use while?
# is there a better way?

# i wouldn't like to just increment checked number as it's advised to us
# instead: let's checked if number is really odd or not

'''
print('part u.1')
numbers = [1,5,4,19,23,35,31,324,234,325,87,101,102,108]
for number in numbers:
    if number % 2 != 0:
        print(number)
'''
'''
numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))
'''
# using range
winners = ['Max','Leo','Kate']
for i in range(len(winners)):
    print(i+1,')',winners[i])
