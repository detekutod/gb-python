friend_name = 'Max'
friends = ['Max','Leo','Kate']
roles = ('admin','guest','user')

if 'M' in friend_name:
    print('+')

# for
for friend in friends:
    print(friend)
print('end')

# while
'''
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
'''

for letter in friend_name:
    print(letter)
print('end')

for role in roles:
    print(role)
print('end')
