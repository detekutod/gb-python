#example concat1
#way 1: using % operand

name = 'Leo'
age = 30
mys = 'hello %s you are %d years old'%(name,age)
print('1st call:')
print(mys)

#way2:using .format method

mys = 'hello {} you are {} years old'.format(name,age)
print('2d call:')
print(mys)
	

#example 1
#нужно:
#вывести строку Поздравляем 1.ИВАНОВ 2.СИДОРОВ 3.ПЕТРОВ с успехом!

top5 = 'Первые 5 мест на соревнованиях: 1.Иванов 2.Петров 3.Сидоров 4.Орлов 5.Соколов'

print('example start here:')
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
top3 = top3.upper()
#print(top3)
s = 'Поздравляем {} с успехом!'
print(s.format(top3))
