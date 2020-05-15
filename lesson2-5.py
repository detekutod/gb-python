'''
friends = ['Max','Leo','Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))
'''

# how to add age to friend?

friend = {
    'name': 'Max',
    'age': 23,
    'sex': 'M'
}

# via keys
'''
for key in friend:
    print(key) #конкретно выводит ключ
    print(friend[key]) #конкретно выводит значение
'''

# по значению
'''
for val in friend.values():
    print(val)
'''

# via pair key:val
# метод items() возвращает список (условно список) кортежей
'''
for item in friend.items():
    print(item)
'''

# есть другой способ, позволяющий получить пару ключ:значение
# в оригинале лектор сделал два принта в цикле for, зачем непонятно
for key, val in friend.items():
    print(key,':',val)




    
'''
print(friend)
print(type(friend))

print('- - - - -')

print(friend['name'])

friend['has_car'] = True
# идентичный ключ не будет добавлен дважды

print(friend)

del friend['has_car']

print(friend)

print('age' in friend)
'''
