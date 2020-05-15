# def принимает имя, возраст и город
# returns string of view: 'Name, n years old, lives in town <town name>'
'''
desc = ['Иван',28,'Ангарск']

def testdef(a):
    name = a[0]
    age = a[1]
    city = a[2]
    temp = '{}, {} лет, проживает в городе {}'
    print(temp.format(name,age,city))

testdef(desc)
'''

# def принимает 3 числа и возвращает наибольшее из них

def oneof3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        print('there is at least 1 pair of equal numbers')
        return 0

x = int(input('enter x:'))
y = int(input('enter y:'))
z = int(input('enter z:'))

print(oneof3(x,y,z))

# см. урок 9 "разбор домашнего задания"
