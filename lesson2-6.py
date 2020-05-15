# sets

# we can use set based on list to create range of unique objects
# (if there is a chance we have non-unique objects in original list)

userlist = ['Moscow','New York','Irkutsk','Tokio','Moscow','Tokio']
print(userlist)
print(len(userlist))

# now we create set based on the list

cities = set(userlist)
print(cities)
print(len(cities))

# extra 'Tokio' and 'Moscow' were removed from created set

#
# actions with sets
#

# adding new element
cities.add('Burma')
print(cities)

# removing an element
cities.remove('Moscow')
print(cities)

# len(set)
print('length of the set:',len(cities))

# in operand / for cicle
print('Moscow' in cities) # False
print('Burma' in cities) # True

for city in cities:
    print(city)

# actions with multiple sets (объединение, пересечение, ...)


max_things = {'phone','razor','shirt','shorts'}
kate_things = {'phone','shorts','umbrella','makeup'}

# which belongings do they have?
print(max_things | kate_things)
print('- - - - -')
# which repeat
print(max_things & kate_things)
print('- - - - -')
# which taken by Max, not by Kate
print(max_things - kate_things)
print('- - - - -')
# which taken by Kate, not by Max
print(kate_things - max_things)
print('- - - - -')




