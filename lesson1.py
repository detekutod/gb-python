def first():
    a = int(input('enter num:$'))
    print('result:',a + 2)
#
def second():
    a = 1000
    while not ((a > 0) and (a < 10)):
        a = int(input('enter num a: 0 < a < 10:$'))
    print('power 2 of the number: ',a ** 2)
#
def anketa():
    name = str(input('enter name:'))
    surname = str(input('enter lastname:'))
    age = int(input('enter age:'))
    weight = int(input('enter weight:'))
    print('results for',name,surname,':')
    if age < 30 and (weight > 50 and weight < 120):
        print('Health condition is good')
        
    elif ((age > 40) != (weight < 50 or weight > 120)):
        print('Physical education required')
        
    elif age > 40 and (weight < 50 or weight > 120):
        print('Medical healthcare required')

anketa()

